import os

folders = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for base, direct in folders.items():
    if os.path.exists(base):
        print(base, 'Такая папка уже существует')
    else:
        for i in direct:
            con_dir = os.path.join(base, i)
            os.makedirs(con_dir)