import os

def remove_content_before_word(folder_path, target_word):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding= 'utf-8' ) as file:
            lines = file.readlines()
        target_index = -1
        for i, line in enumerate(lines):
            if target_word in line:
                target_index = i
                break

        if target_index != -1:
            lines = lines[target_index:]
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            print(f"Removed content before '{target_word}'.")
        else:
            print(f"Target word '{target_word}' not found in the file.")

folder_path = r'F:\LLM-Isabelle\afp-2024-04-08\theory2 copy'  
target_word = 'theory' 
remove_content_before_word(folder_path, target_word)
