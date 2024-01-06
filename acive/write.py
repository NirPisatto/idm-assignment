import csv

# Sample dictionary
data = {'Name': 'John', 'Age': 25, 'City': 'New York'}

# CSV file path
csv_file_path = 'example.csv'

# Check if the file exists, if not create it with header
file_exists = False
try:
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        if any(reader):
            file_exists = True
except FileNotFoundError:
    pass

# Append data to the CSV file
with open(csv_file_path, 'a', newline='') as file:
    fieldnames = data.keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # If the file is newly created, write header
    if not file_exists:
        writer.writeheader()

    # Write data to the file
    writer.writerow(data)
    raise Exception("Error")
    writer.writerow(data)


print(f"Data has been appended to {csv_file_path}.")
