import os

path = input("Path to the files: ")
output = input("Path to the output folder: ")

if not os.path.isdir(path):
    print("Path doesn't exist!")
    exit()

if not os.path.isdir(output):
    os.mkdir(output)

for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)
    base = os.path.splitext(file_name)[0]
    out_path = os.path.join(output, base)
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    os.rename(file_path, os.path.join(out_path, file_name))
    print(f"Moved {file_path} to {os.path.join(out_path, file_name)}")

print("Done")
