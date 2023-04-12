
import pandas as pd

# Prompt user for file path
file_path = 'E:\\steps to add Quran Sound\\Hadith.xlsx'

# Load Excel file
df = pd.read_excel(file_path)

# Remove empty rows
df.dropna(how='all', inplace=True)

# Prompt user for output file path
output_path = "E:\\steps to add Quran Sound\\cleaned_file.xlsx"

# Save cleaned Excel file
df.to_excel(output_path, index=False)

print("File saved successfully!")
