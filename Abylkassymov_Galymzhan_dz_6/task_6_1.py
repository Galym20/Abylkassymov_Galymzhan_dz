file_txt = open('nginx_logs.txt', encoding='utf-8')
with file_txt as f:
    text = []
    for i in f:
        split_text = i.split()
        text.append((split_text[0], split_text[5].replace('"', ''), split_text[6]))
print(text)

