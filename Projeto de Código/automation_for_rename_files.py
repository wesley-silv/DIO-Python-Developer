import os

def rename_files(directory, prefix):
    files = os.listdir(directory)  # list all files of directory

    for i, name in enumerate(files, start=1):
        extensao = os.path.splitext(name)[1]  # separate extension (.jpg, .txt, etc.)
        new_name = f"{prefix}-{i}{extensao}"
        old_path = os.path.join(directory, name)
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)
        print(f"✅ Renomeado: {name} → {new_name}")

# Example of use
directory = r"C:\Users\wesle\OneDrive\Imagens\Saved Pictures\Renamed"
rename_files(directory, "IMG")