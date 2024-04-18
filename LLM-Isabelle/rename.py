import os

def change_file_extension(folder_path, new_extension='.txt'):
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            name, ext = os.path.splitext(filename)
            new_filename = name + new_extension
            new_filepath = os.path.join(folder_path, new_filename)
            os.rename(filepath, new_filepath)
            print(f"Renamed '{filename}' to '{new_filename}'.")

folder_path = r'F:\LLM-Isabelle\afp-2024-04-08\theory2 copy' 
change_file_extension(folder_path)
