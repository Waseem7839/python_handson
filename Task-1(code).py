import os

# Q1: Print current working directory
print("Current Working Directory:", os.getcwd())

# Q2: Check if a path is a file or directory
path = "practice.py"  

if os.path.isfile(path):
    print(f"{path} is a file")
elif os.path.isdir(path):
    print(f"{path} is a directory")
else:
    print(f"{path} does not exist")

# Q3: Create a directory if not exists
folder_name = "test_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created:", folder_name)
else:
    print("Folder already exists:", folder_name)

# Q4: List only .txt files
print("Listing .txt files in current directory:")
current_dir = os.getcwd()
for file in os.listdir(current_dir):
    if file.endswith(".txt"):
        print(file)

#Q5
# import os
import shutil

reports_dir = "reports"

if not os.path.exists(reports_dir):
    os.mkdir(reports_dir)
    print(f"Created directory: {reports_dir}")
else:
    print(f"Directory already exists: {reports_dir}")

txt_files = [f for f in os.listdir() if f.endswith('.txt') and os.path.isfile(f)]

for file in txt_files:
    print(f"Found .txt file: {file}")

    source_path = os.path.join(os.getcwd(), file)
    destination_path = os.path.join(os.getcwd(), reports_dir, file)
    
    shutil.move(source_path, destination_path)
    print(f"Moved '{file}' to '{reports_dir}/'")


