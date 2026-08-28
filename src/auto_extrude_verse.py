import argparse
import os
import trimesh
import numpy as np
from manifold3d import Mesh, Manifold

def auto_detect_parting_surface(mesh, inset=2.0):
    """
    Auto-detect the parting surface by slicing the mesh near all 6 bounding box faces.
    Returns the axis name (e.g., 'y-') with the largest cross-sectional area.
    """
    axes = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]]
    names = ['x+', 'x-', 'y+', 'y-', 'z+', 'z-']
    best_area = 0
    best_name = ''

    for name, normal in zip(names, axes):
        idx = np.nonzero(normal)[0][0]
        sign = normal[idx]
        
        if sign > 0: # +
            origin = mesh.bounds[1].copy()
            origin[idx] -= inset
        else: # -
            origin = mesh.bounds[0].copy()
            origin[idx] += inset
            
        slice_3d = mesh.section(plane_origin=origin, plane_normal=np.array(normal) * -1)
        if slice_3d:
            slice_2d, _ = slice_3d.to_2D()
            for poly in slice_2d.polygons_full:
                if poly.area > best_area:
                    best_area = poly.area
                    best_name = name
                    
    return best_name

def create_auto_verse_model(input_path, output_path, padding=5.0, axis=None, handle_length=20.0, split_axis=None):
    print(f"Loading impression model from: {input_path}")
    impression = trimesh.load(input_path)
    
    if not axis:
        print("Auto-detecting parting surface...")
        axis = auto_detect_parting_surface(impression)
        print(f"Detected parting surface at: {axis}")
        
    # Get slice for the handle
    axis_char = axis[0].lower()
    sign = 1 if axis[1] == '+' else -1
    axis_idx = {'x': 0, 'y': 1, 'z': 2}[axis_char]
    
    origin = impression.bounds[1].copy() if sign > 0 else impression.bounds[0].copy()
    origin[axis_idx] -= sign * 1.5 # Slice 1.5mm inwards to get a clean polygon
    
    normal = [0, 0, 0]
    normal[axis_idx] = -sign # Plane normal points inwards
    
    print(f"Slicing mesh to generate handle extension on {axis}...")
    slice_3d = impression.section(plane_origin=origin, plane_normal=normal)
    
    if not slice_3d:
        print("Error: Could not slice the mesh to create a handle.")
        return
        
    slice_2d, to_3d = slice_3d.to_2D()
    poly = max(slice_2d.polygons_full, key=lambda p: p.area)
    
    print(f"Extruding parting surface (Area: {poly.area:.1f} mm2)...")
    prism = trimesh.creation.extrude_polygon(poly, height=handle_length)
    # The prism is extruded in Z+ by default in 2D space.
    # We want it to go OUTWARDS from the cut plane, so we shift it back by height.
    prism.apply_translation([0, 0, -handle_length])
    prism.apply_transform(to_3d)
    
    print("Converting meshes to Manifold objects for robust boolean operations...")
    m_imp = Manifold(Mesh(vert_properties=np.array(impression.vertices, dtype=np.float32), 
                          tri_verts=np.array(impression.faces, dtype=np.uint32)))
    m_handle = Manifold(Mesh(vert_properties=np.array(prism.vertices, dtype=np.float32), 
                             tri_verts=np.array(prism.faces, dtype=np.uint32)))
                             
    # Union the impression and the handle
    m_imp_extended = m_imp + m_handle
    
    # Create bounding block for the flesh, based ONLY on the original impression bounds
    block_extents = impression.extents + (padding * 2)
    block_center = impression.centroid.copy()
    block = trimesh.creation.box(extents=block_extents)
    block.apply_translation(block_center)
    
    m_blk = Manifold(Mesh(vert_properties=np.array(block.vertices, dtype=np.float32), 
                          tri_verts=np.array(block.faces, dtype=np.uint32)))
                          
    print("Executing Boolean Difference (Block - Extended Impression)...")
    m_verse = m_blk - m_imp_extended
    
    # Export logic
    if split_axis:
        print(f"Splitting mold along {split_axis}-axis...")
        split_idx = {'x': 0, 'y': 1, 'z': 2}[split_axis.lower()]
        huge = 500.0
        
        box_pos_center = block_center.copy()
        box_pos_center[split_idx] += huge / 2.0
        m_box_pos = Manifold(Mesh(
            vert_properties=np.array(trimesh.creation.box(extents=[huge, huge, huge]).apply_translation(box_pos_center).vertices, dtype=np.float32),
            tri_verts=np.array(trimesh.creation.box(extents=[huge, huge, huge]).faces, dtype=np.uint32)
        ))
        
        box_neg_center = block_center.copy()
        box_neg_center[split_idx] -= huge / 2.0
        m_box_neg = Manifold(Mesh(
            vert_properties=np.array(trimesh.creation.box(extents=[huge, huge, huge]).apply_translation(box_neg_center).vertices, dtype=np.float32),
            tri_verts=np.array(trimesh.creation.box(extents=[huge, huge, huge]).faces, dtype=np.uint32)
        ))
        
        m_part_a = m_verse ^ m_box_pos
        m_part_b = m_verse ^ m_box_neg
        
        out_a = m_part_a.to_mesh()
        out_b = m_part_b.to_mesh()
        
        verse_a = trimesh.Trimesh(vertices=np.array(out_a.vert_properties, dtype=np.float64), faces=np.array(out_a.tri_verts, dtype=np.int32))
        verse_b = trimesh.Trimesh(vertices=np.array(out_b.vert_properties, dtype=np.float64), faces=np.array(out_b.tri_verts, dtype=np.int32))
        
        base, ext = os.path.splitext(output_path)
        path_a = f"{base}_partA{ext}"
        path_b = f"{base}_partB{ext}"
        verse_a.export(path_a)
        verse_b.export(path_b)
        print(f"Success! Saved split models to:\n  {path_a}\n  {path_b}")
    else:
        out_mesh_data = m_verse.to_mesh()
        verse = trimesh.Trimesh(vertices=np.array(out_mesh_data.vert_properties, dtype=np.float64), 
                                faces=np.array(out_mesh_data.tri_verts, dtype=np.int32))
        verse.export(output_path)
        print(f"Success! Saved zero-loss verse model to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zero-loss automated verse model generation using core extension (拔模面延伸).")
    parser.add_argument("-i", "--input", type=str, required=True, help="Path to input impression STL")
    parser.add_argument("-o", "--output", type=str, required=True, help="Path to output verse STL")
    parser.add_argument("-p", "--padding", type=float, default=5.0, help="Padding thickness around the impression (mm)")
    parser.add_argument("--axis", type=str, default=None, choices=['x+', 'x-', 'y+', 'y-', 'z+', 'z-'], 
                        help="The axis of the parting surface. If omitted, the script will auto-detect it.")
    parser.add_argument("--split", type=str, default=None, choices=['x', 'y', 'z'], 
                        help="Split the resulting mold in half along this axis (outputs two files).")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} does not exist.")
        exit(1)
        
    create_auto_verse_model(args.input, args.output, args.padding, args.axis, 20.0, args.split)
