# RAW Data Processor

This Python script processes RAW data files, where each pixel value is stored as a 16-bit unsigned integer. It performs a right shift operation on each pixel value to extract the lower bits, effectively reducing the bit depth. The processed data is saved in the same folder with a filename prefix "out_".

## Usage

1. **Run the Script**

    ```bash
    python raw_data_processor.py width height bit_shift input_folder
    ```

    - `width`: Width of the image in pixels.
    - `height`: Height of the image in pixels.
    - `bit_shift`: Number of bits to right-shift each pixel value.
    - `input_folder`: Path to the folder containing RAW data files.

2. **Output**

    Processed data files will be saved in the same folder with a filename prefix "out_".

## Dependencies

- NumPy: The script uses NumPy for efficient array operations. Install it using pip:

    ```bash
    pip install numpy
    ```
