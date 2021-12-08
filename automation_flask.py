from automation_project import auto_project
import os

editor="code"

name_project=input("Enter the name of the project: ")
auto_project.create_folder(name_project)
auto_project.create_folder("src")
os.system("touch Procfile")
os.system("touch requirements.txt")
os.system("touch README.md")



auto_project.create_git_repo()
auto_project.open_editor(editor)