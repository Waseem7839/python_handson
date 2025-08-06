#1
import os
# Folder name
input_folder = 'data_input'

# Check if folder exists
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print(f"'{input_folder}' folder created.")

    # Create two sample .txt files inside it
    sample_files = {
        "notes.txt": "This is a sample note.\n# This is a comment.\nThis temp line will be replaced.\n",
        "report.txt": "Report line 1.\nReport temp line 2.\n# Report comment line.\n"
    }

    for file_name, content in sample_files.items():
        file_path = os.path.join(input_folder, file_name)
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Created sample file: {file_name}")

    print("Sample .txt files added.")
else:
    print(f"'{input_folder}' folder already exists. Please check for existing .txt files.")

#2
# Reads all .txt files from the data_input folder.
import os

# Folder name
input_folder = 'data_input'

# Check if folder exists
if not os.path.exists(input_folder):
    print(f"'{input_folder}' folder does not exist. Please create it and add .txt files.")
    exit()

# Get list of all .txt files
txt_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

# Check if any .txt files are found
if not txt_files:
    print("No .txt files found in 'data_input'. Please add some and try again.")
    exit()

# Print the list of found files
print("Found the following .txt files in 'data_input':")
for file in txt_files:
    print(f"- {file}")

#3
import os

input_folder = 'data_input'
output_folder = 'data_output'

# Ensure input folder exists
if not os.path.exists(input_folder):
    print(f"'{input_folder}' does not exist. Please create it and add .txt files.")
    exit()

# Get list of .txt files
txt_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

if not txt_files:
    print("No .txt files found in 'data_input'.")
    exit()

# ✅ Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each file
for file_name in txt_files:
    input_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, file_name)

    line_count = 0
    word_count = 0
    modified_lines = []

    with open(input_path, 'r') as infile:
        for line in infile:
            if line.strip().startswith('#'):
                continue  # Ignore comment lines

            line_count += 1
            word_count += len(line.split())

            # Replace 'temp' with 'permanent'
            modified_line = line.replace('temp', 'permanent')
            modified_lines.append(modified_line)

    # Save modified content to output folder
    with open(output_path, 'w') as outfile:
        outfile.writelines(modified_lines)

    # Print status
    print(f"Processed {file_name} → Lines: {line_count}, Words: {word_count}")
    print(f"Modified version saved in 'data_output/{file_name}'")

#4
summary_data = []  # Initialize list to store summary info

for filename in txt_files:
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    with open(input_path, 'r') as file:
        lines = file.readlines()

    processed_lines = []
    line_count = 0
    word_count = 0

    for line in lines:
        if line.strip().startswith('#'):
            continue
        line_count += 1
        words = line.strip().replace("temp", "permanent").split()
        word_count += len(words)
        processed_lines.append(" ".join(words))

    with open(output_path, 'w') as file:
        file.write("\n".join(processed_lines))

    print(f"Processed {filename} → Lines: {line_count}, Words: {word_count}")
    print(f"Modified version saved in 'data_output/{filename}'")

    # Store summary
    summary_data.append((filename, line_count, word_count))


