import pandas as pd
import glob
import os

def merge_csv_files(output_filename="2025_12_31.csv"):
    # 1. Identify all CSV files in the current directory
    # Use a pattern to avoid re-including the output file if it already exists
    extension = 'csv'
    all_filenames = [i for i in glob.glob(f'*.{extension}') if i != output_filename]
    
    if not all_filenames:
        print("No CSV files found to merge.")
        return

    print(f"Found {len(all_filenames)} files. Starting merge...")

    # 2. Read and combine files
    # We use a list comprehension for efficiency
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

    # 3. Export to a new CSV
    # index=False prevents pandas from adding an extra column for row numbers
    combined_csv.to_csv(output_filename, index=False)
    
    print(f"Success! Merged file saved as: {output_filename}")

if __name__ == "__main__":
    merge_csv_files()