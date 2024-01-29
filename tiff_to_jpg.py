from PIL import Image
import os
from tqdm import tqdm
import glob
import argparse

# Disable DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None


def slice_image(input_path, output_folder, slice_size):
    with Image.open(input_path) as img:
        # Convert the image to RGB if it's RGBA
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        img_width, img_height = img.size

        # Calculate the number of slices in each dimension
        x_slices = img_width // slice_size if img_width % slice_size == 0 else img_width // slice_size + 1
        y_slices = img_height // slice_size if img_height % slice_size == 0 else img_height // slice_size + 1

        # Create the output directory if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Generate slices
        for x in tqdm(range(x_slices), desc=f"Slicing {os.path.basename(input_path)}", leave=False):
            for y in range(y_slices):
                if x == x_slices - 1 and img_width % slice_size != 0:  # Last column slice
                    left = img_width - slice_size
                else:
                    left = x * slice_size

                if y == y_slices - 1 and img_height % slice_size != 0:  # Last row slice
                    upper = img_height - slice_size
                else:
                    upper = y * slice_size

                right = left + slice_size
                lower = upper + slice_size

                # Crop the image and save the slice
                slice = img.crop((left, upper, right, lower))

                slice_file_name = f"{output_folder}/slice_{os.path.basename(input_path).split('.')[0]}_{x}_{y}.jpg"
                slice.save(slice_file_name, "JPEG")


# Set up argument parsing
parser = argparse.ArgumentParser(description="Slice TIFF images in a folder into smaller JPEG images.")
parser.add_argument("input_folder", type=str, help="Path to the input folder containing TIFF files")
parser.add_argument("output_folder", type=str, help="Path to the output folder to save sliced images")
parser.add_argument("slice_size", type=int, help="Size of each slice (in pixels)")

# Parse the arguments
args = parser.parse_args()

# Process each TIFF file with an outer tqdm progress bar
tiff_files = glob.glob(f'{args.input_folder}/*.tif') + glob.glob(f'{args.input_folder}/*.tiff')

with tqdm(total=len(tiff_files), desc="Processing files") as pbar:
    for tiff_file in tiff_files:
        slice_image(tiff_file, args.output_folder, args.slice_size)
        pbar.update(1)

