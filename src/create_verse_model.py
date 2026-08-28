import argparse
import os
import trimesh
import numpy as np
from manifold3d import Mesh, Manifold

def create_verse_model(input_path, output_path, padding=5.0):
    """
    Take an ear impression mesh (positive mold) and create a verse body model (negative mold)
    by subtracting it from a bounding block using robust boolean operations via manifold3d.
    """
    print(f"Loading impression model from: {input_path}")
    impression = trimesh.load(input_path)
    
    if not impression.is_watertight:
        print("Warning: Input mesh is not watertight! Boolean operations might yield unexpected results.")
    
    # Calculate bounding box of the impression
    bounds = impression.bounds
    extents = impression.extents
    
    print(f"Impression bounds: {bounds}")
    print(f"Impression extents: {extents}")
    print(f"Impression volume: {impression.volume if impression.is_watertight else 'N/A'}")
    
    # Create a bounding block (flesh) that is larger than the impression
    # We add padding to all sides.
    # However, for the "outer" side (usually where the impression was cut, e.g., the base),
    # we might want it flush. We'll add padding everywhere for a complete mold.
    block_extents = extents + (padding * 2)
    block_center = impression.centroid
    
    # Create the block in trimesh
    block = trimesh.creation.box(extents=block_extents)
    block.apply_translation(block_center)
    
    print("Converting meshes to Manifold objects for robust boolean subtraction...")
    # Convert impression to Manifold
    # Note: Manifold expects float32 for vertices and uint32 for faces
    verts_imp = np.array(impression.vertices, dtype=np.float32)
    faces_imp = np.array(impression.faces, dtype=np.uint32)
    m_imp = Manifold(Mesh(vert_properties=verts_imp, tri_verts=faces_imp))
    
    # Convert block to Manifold
    verts_blk = np.array(block.vertices, dtype=np.float32)
    faces_blk = np.array(block.faces, dtype=np.uint32)
    m_blk = Manifold(Mesh(vert_properties=verts_blk, tri_verts=faces_blk))
    
    print("Executing Boolean Difference (Block - Impression)...")
    m_verse = m_blk - m_imp
    
    print("Extracting resulting mesh...")
    out_mesh_data = m_verse.to_mesh()
    
    # Reconstruct trimesh object
    verse_verts = np.array(out_mesh_data.vert_properties, dtype=np.float64)
    verse_faces = np.array(out_mesh_data.tri_verts, dtype=np.int32)
    
    verse = trimesh.Trimesh(vertices=verse_verts, faces=verse_faces)
    
    print(f"Resulting verse model volume: {verse.volume if verse.is_watertight else 'N/A'}")
    
    # Export to output path
    verse.export(output_path)
    print(f"Success! Saved verse model to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a negative (verse) ear model from a positive ear impression.")
    parser.add_argument("-i", "--input", type=str, required=True, help="Path to input impression STL")
    parser.add_argument("-o", "--output", type=str, required=True, help="Path to output verse STL")
    parser.add_argument("-p", "--padding", type=float, default=5.0, help="Padding thickness around the impression (mm)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} does not exist.")
        exit(1)
        
    create_verse_model(args.input, args.output, args.padding)
