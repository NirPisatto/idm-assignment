import csv
from collections import defaultdict

# Specify the path to your CSV file
csv_file_path = 'cleaned.v1.csv'

# Specify the column index for which you want to get unique values (indexing starts from 0)
column_index = 3  # Change this to the desired column index


# Create a defaultdict to store counts for each unique value
value_counts = defaultdict(int)

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip header row if it exists
    header = next(csv_reader, None)
    
    for row in csv_reader:
        # Check if the row has the specified column index
        if column_index < len(row):
            value = row[column_index]
            value_counts[value] += 1

# Print unique values and their counts
print(f"Unique values in column {column_index + 1} and their counts:")
for value, count in value_counts.items():
    print(f"{count} times - {value}")
