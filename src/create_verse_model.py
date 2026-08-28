import argparse
import os
import trimesh
import numpy as np
from manifold3d import Mesh, Manifold

def create_verse_model(input_path, output_path, padding=5.0, open_face=None, split_axis=None, cut_depth=0.0):
    """
    Take an ear impression mesh (positive mold) and create a verse body model (negative mold).
    
    open_face: str, e.g., 'x+', 'y-'. Leaves this face open by not padding it.
    cut_depth: float. When open_face is used, cuts this many mm deeper into the mesh to guarantee opening.
    split_axis: str, e.g., 'x', 'y', 'z'. Splits the final mold in half along this axis at the centroid.
    """
    print(f"Loading impression model from: {input_path}")
    impression = trimesh.load(input_path)
    
    bounds = impression.bounds
    extents = impression.extents
    centroid = impression.centroid
    
    # Calculate bounding block
    block_extents = extents + (padding * 2)
    block_center = centroid.copy()
    
    if open_face:
        axis_char = open_face[0].lower()
        sign = 1 if open_face[1] == '+' else -1
        axis_idx = {'x': 0, 'y': 1, 'z': 2}[axis_char]
        
        # Shift the block so that it is flush with the impression on this face
        # If cut_depth is provided, we cut deeper into the impression
        cut = cut_depth if cut_depth else 0.0
        # Reduce the extent on this axis by 'padding' + 'cut'
        block_extents[axis_idx] -= (padding + cut)
        # Shift center towards the opposite direction by (padding + cut)/2
        block_center[axis_idx] -= sign * ((padding + cut) / 2.0)

        
    block = trimesh.creation.box(extents=block_extents)
    block.apply_translation(block_center)
    
    print("Converting meshes to Manifold objects for robust boolean subtraction...")
    m_imp = Manifold(Mesh(vert_properties=np.array(impression.vertices, dtype=np.float32), 
                          tri_verts=np.array(impression.faces, dtype=np.uint32)))
    m_blk = Manifold(Mesh(vert_properties=np.array(block.vertices, dtype=np.float32), 
                          tri_verts=np.array(block.faces, dtype=np.uint32)))
    
    print("Executing Boolean Difference (Block - Impression)...")
    m_verse = m_blk - m_imp
    
    if split_axis:
        print(f"Splitting mold along {split_axis}-axis...")
        axis_idx = {'x': 0, 'y': 1, 'z': 2}[split_axis.lower()]
        
        # Create two massive bounding boxes for splitting
        huge = 500.0
        
        # Box for positive half
        box_pos_extents = np.array([huge, huge, huge])
        box_pos_center = centroid.copy()
        box_pos_center[axis_idx] += huge / 2.0
        m_box_pos = Manifold(Mesh(
            vert_properties=np.array(trimesh.creation.box(extents=box_pos_extents).apply_translation(box_pos_center).vertices, dtype=np.float32),
            tri_verts=np.array(trimesh.creation.box(extents=box_pos_extents).faces, dtype=np.uint32)
        ))
        
        # Box for negative half
        box_neg_extents = np.array([huge, huge, huge])
        box_neg_center = centroid.copy()
        box_neg_center[axis_idx] -= huge / 2.0
        m_box_neg = Manifold(Mesh(
            vert_properties=np.array(trimesh.creation.box(extents=box_neg_extents).apply_translation(box_neg_center).vertices, dtype=np.float32),
            tri_verts=np.array(trimesh.creation.box(extents=box_neg_extents).faces, dtype=np.uint32)
        ))
        
        m_part_a = m_verse ^ m_box_pos  # Intersection
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
        print(f"Success! Saved verse model to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a negative (verse) ear model from a positive ear impression.")
    parser.add_argument("-i", "--input", type=str, required=True, help="Path to input impression STL")
    parser.add_argument("-o", "--output", type=str, required=True, help="Path to output verse STL")
    parser.add_argument("-p", "--padding", type=float, default=5.0, help="Padding thickness around the impression (mm)")
    parser.add_argument("--open-face", type=str, default=None, choices=['x+', 'x-', 'y+', 'y-', 'z+', 'z-'], 
                        help="Make the specified face flush with the impression (e.g., y-) to leave the ear cavity open to the outside.")
    parser.add_argument("--cut-depth", type=float, default=0.0, 
                        help="When using --open-face, cut this many mm deeper into the model to guarantee the opening is exposed.")
    parser.add_argument("--split", type=str, default=None, choices=['x', 'y', 'z'], 
                        help="Split the resulting mold in half along this axis (outputs two files).")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} does not exist.")
        exit(1)
        
    create_verse_model(args.input, args.output, args.padding, args.open_face, args.split, args.cut_depth)
