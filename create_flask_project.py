from automation_project import auto_project
from automation_flask import flask_project
import os

name_project=input("Enter the name of the project: ")
#if folder not exists
if(auto_project.create_folder(name_project)!=False):
  #create flask folders
  auto_project.create_folder("src")
  flask_project.create_flask_files()
  flask_project.create_flask_folders()
  #create virtual environment and install dependencies
  flask_project.create_virtual_environment()
  flask_project.install_dependencies()
  #fill flask files
  flask_project.fill_Procfile()
  flask_project.fill_runtime()
  flask_project.fill_python_flask_base()

  #git flask project
  auto_project.create_git_repo()
  auto_project.create_github_repo()

  #opèn project
  auto_project.open_editor(auto_project.editor)

else:
     print("Folder already exist")