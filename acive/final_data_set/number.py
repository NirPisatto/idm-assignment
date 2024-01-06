import csv

# Specify the path to your CSV file
csv_file_path = 'cleaned.csv'

# Read the CSV file and overwrite the values in the first column
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Read the data into a list
    data = list(csv_reader)

# Modify the values in the first column as needed
index = 1
for row in data:
    # Assuming you want to overwrite the first column with a new value, replace 'new_value' with your desired value
    row[0] = f'{index}'
    index += 1

# Write the modified data back to the CSV file
with open('cleaned.v1.csv', 'w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)
    
    # Write the modified data
    csv_writer.writerows(data)

print("CSV file updated successfully.")
