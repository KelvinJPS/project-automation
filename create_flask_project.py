from automation_project import auto_project
from automation_flask import flask_project
import os

name_project=input("Enter the name of the project: ")
#if folder exists
if(auto_project.create_folder(name_project)!=False):
  auto_project.create_folder("src")
  flask_project.create_files()
  flask_project.create_virtual_environment()
  flask_project.fill_runtime()

else:
     print("Folder already exist")