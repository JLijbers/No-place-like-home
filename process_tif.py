from PIL import Image
import os

# Disable DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None


def slice_image(input_path, output_folder, slice_size):
    with Image.open(input_path) as img:
        img_width, img_height = img.size

        # Calculate the number of slices in each dimension
        x_slices = img_width // slice_size
        y_slices = img_height // slice_size

        # Create the output directory if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Generate slices
        for x in range(x_slices):
            for y in range(y_slices):
                left = x * slice_size
                upper = y * slice_size
                right = left + slice_size
                lower = upper + slice_size

                # Crop the image and save the slice
                slice = img.crop((left, upper, right, lower))
                slice_file_name = f"{output_folder}/slice_{x}_{y}.jpg"
                slice.save(slice_file_name, "JPEG")


# Usage
input_path = 'data/raw/20230823_105303_PNEO-04_1_1_30cm_RD_8bit_RGB_Stroe/20230823_105303_PNEO' \
             '-04_1_1_30cm_RD_8bit_RGB_Stroe.tif '
output_folder = 'data/jpg-tiles'
slice_size = 1024

slice_image(input_path, output_folder, slice_size)
