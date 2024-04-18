import json

def txt_to_json(folder_path, json_file, title_markers={"function", "definition", "lemma", "prove"}):
    data = []
    with open(txt_file, 'r', encoding='utf-8') as file:
        title = None
        content = ""
        for line in file:
            line = line.strip()
            if line:  
                if not title: 
                    for marker in title_markers:
                        if line.startswith(f"{{{marker}}}"):
                            title = line[len(marker) + 2:-1].strip() 
                            break
                else:
                    content += line + "\n"
            else:  
                if title:
                    data.append({"title": title, "content": content.strip()})
                    title = None
                    content = ""
    if title:
        data.append({"title": title, "content": content.strip()})

    with open(json_file, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

folder_path = r'F:\LLM-Isabelle\LLM-Isabelle\theory2 copy'

txt_to_json(txt_file, json_file, title_markers={"function", "definition", "lemma", "prove"})
