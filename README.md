# No Place Like Home: AI-Driven Image Analysis with DINOv2 and FAISS

## Overview
This project, titled "No Place Like Home," leverages the power of AI to find places around the Netherlands that are similar to my childhood home. It demonstrates the powerful combination of DINOv2 and FAISS in image datasets.

## Project Structure
The project is structured into two main components:

1. **tiff_to_jpg.py**: A Python script that converts TIFF images into JPG format. This script takes input from a specified folder and outputs JPG tiles of a given size, suitable for further processing.

2. **similarity_search_dino_faiss.ipynb**: A Google Colab Notebook (because GPU) that processes the JPG tiles using DINOv2 for pattern finding and FAISS for conducting a similarity search among the images.

## How to Use

### For Your Own Project
You can easily adapt this project for your own data and research interests. Simply replace the satellite images with your own dataset and follow the provided steps to uncover patterns and similarities in your specific area of interest.

### Prerequisites
- Python 3.10 (but 3.9 will likely work as well)
- Google Colab
- Local Python libraries: Pillow & tqdm (see `requirements.txt` for exact versions I used)

### Step 1: Converting TIFF to JPG
1. Place your raw TIFF images in the `images/raw_tiffs` directory.
2. Run `tiff_to_jpg.py` script with appropriate arguments:
    ```bash
    python tiff_to_jpg.py --input_folder images/raw_tiffs --output_folder images/jpg_tiles --slice_size 1024
    ```

### Step 2: Running the Similarity Search
1. Open the `similarity_search_dino_faiss.ipynb` notebook in Google Colab.
2. Upload the generated JPG tiles to Colab or mount your Google Drive where the tiles are stored.
3. Follow the instructions in the notebook to perform the similarity search.

## Technologies Used
- **DINOv2**: For detecting intricate patterns in images.
- **FAISS**: For fast and efficient similarity search in large datasets.

## Results
The project successfully demonstrates the potential of AI in image analysis for practical applications like enhancing product recommendation systems.

---

*This project is a personal journey in AI and image analysis, showcasing the capabilities of DINOv2 and FAISS in a unique and innovative application.*