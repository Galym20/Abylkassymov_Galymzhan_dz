file_txt = open('nginx_logs.txt', encoding='utf-8')
with file_txt as f:
    text = []
    spam_users = {}
    for line in f:
        splitted = line.split()
        text.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        spam_users.setdefault(splitted[0], 0)
        spam_users[splitted[0]] += 1

spam_users = sorted(spam_users.items(), key=lambda x: x[1], reverse=True)
print(spam_users[:5])