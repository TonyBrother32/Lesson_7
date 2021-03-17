import os

dir_path = os.path.join("my_project", "settings")
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
os.chdir("my_project")
for dir_in in ["mainapp", "adminapp", "authapp"]:
    if not os.path.exists(dir_in):
        os.mkdir(dir_in)

