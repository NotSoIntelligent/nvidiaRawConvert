import sys
import os
import numpy as np

def read_raw_data(filename, num_pixels, bit_shift):
    # Read the raw data as 16-bit unsigned integers
    with open(filename, 'rb') as file:
        raw_data = np.fromfile(file, dtype=np.uint16, count=num_pixels)
    
    # Check that the file size is correct
    if raw_data.size != num_pixels:
        raise ValueError(f"File size does not match expected size. Expected {num_pixels} pixels, got {raw_data.size} pixels.")
    
    # Process the raw data in a vectorized manner
    processed_data = raw_data >> bit_shift

    return processed_data

def save_raw_data(data, output_filename):
    # Write the data to a file as 16-bit unsigned integers
    with open(output_filename, 'wb') as file:
        data.tofile(file)

def process_folder(input_folder, width, height, bit_shift):
    # Iterate over files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.raw'):
            # Get the full path of the file
            input_filepath = os.path.join(input_folder, filename)

            # Calculate the number of pixels
            num_pixels = width * height

            # Read and process the raw data
            processed_data = read_raw_data(input_filepath, num_pixels, bit_shift)

            # Generate the output filename
            output_filename = os.path.join(input_folder, f"out_{filename}")

            # Save the processed data
            save_raw_data(processed_data, output_filename)
            print(f"Processed data saved as {output_filename}")

def main():
    # Check if command line arguments are provided
    if len(sys.argv) < 5:
        print("Usage: python your_program_name.py width height bit_shift input_folder")
        sys.exit(1)

    # Parse command line arguments
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    bit_shift = int(sys.argv[3])
    input_folder = sys.argv[4]

    # Process the input folder
    process_folder(input_folder, width, height, bit_shift)

if __name__ == "__main__":
    main()
