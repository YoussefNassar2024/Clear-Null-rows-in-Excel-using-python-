
import pandas as pd

# Prompt user for file path
file_path = 'E:\\YourFile.xlsx'

# Load Excel file
df = pd.read_excel(file_path)

# Remove empty rows
df.dropna(how='all', inplace=True)

# Prompt user for output file path
output_path = "E:\\cleaned_file.xlsx" # do not forget to add the output file name in this case the output file name is cleaned_file.xlsx
# Save cleaned Excel file
df.to_excel(output_path, index=False)

print("File saved successfully!")
