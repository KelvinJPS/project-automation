from automation_project import auto_project
import os

editor="code"

def create_files():
    os.system("touch Procfile")
    os.system("touch requirements.txt")
    os.system("touch README.md")

def create_virtaulenv():
    os.system("virtualenv venv")
    os.system("source venv/bin/activate")



name_project=input("Enter the name of the project: ")
#if folder exists

if(auto_project.create_folder(name_project)==True):
 auto_project.create_folder("src")
 create_files()
 auto_project.create_git_repo()
 auto_project.create_github_repo()
 auto_project.open_editor(editor)

else:
     print("Folder already exist")



auto_project.create_git_repo()
auto_project.open_editor(editor)