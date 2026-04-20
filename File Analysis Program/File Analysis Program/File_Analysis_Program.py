import glob
import os

# Folder containing the .txt files
folder_path = "server_dump/*.txt"

# Get all .txt files in the directory
files = glob.glob(folder_path)

# Dictionaries to store counts and filenames
status_counts = {
    "OK": 0,
    "WARN": 0,
    "ERROR": 0
}

status_files = {
    "OK": [],
    "WARN": [],
    "ERROR": []
}

# Read each file and check status
for file in files:
    with open(file, "r") as f:
        content = f.read()
        
        if "OK" in content:
            status_counts["OK"] += 1
            status_files["OK"].append(os.path.basename(file))
        elif "WARN" in content:
            status_counts["WARN"] += 1
            status_files["WARN"].append(os.path.basename(file))
        elif "ERROR" in content:
            status_counts["ERROR"] += 1
            status_files["ERROR"].append(os.path.basename(file))

# Print counts
print("\nStatus Counts:")
for status, count in status_counts.items():
    print(f"{status}: {count}")

# Ask user if they want to print filenames
choice = input("\nWould you like to see the filenames for each status? (yes/no): ").lower()

if choice == "yes":
    for status, file_list in status_files.items():
        print(f"\n{status} Files:")
        if file_list:
            for name in file_list:
                print(name)
        else:
            print("None")