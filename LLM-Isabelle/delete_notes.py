import os

def remove_content_between_words(folder_path, word1, word2):
    num = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            new_lines = []
            keep_lines = 0
            for line in lines:
                if word1 in line:
                    keep_lines += 1
                if not keep_lines:
                    new_lines.append(line)
                if word2 in line:
                    keep_lines -= 1
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(new_lines)
            num += 1
            print(f"No.{num}文件中特定两个单词之间的内容已删除。")
        except FileNotFoundError:
            print(f"文件 '{file_path}' 未找到。")

folder_path =  r'F:\LLM-Isabelle\afp-2024-04-08\theory2 copy'  
word1 = '(*'  
word2 = '*)'  
remove_content_between_words(folder_path, word1, word2)
