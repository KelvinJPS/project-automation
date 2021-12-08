import os

os.chdir("/home/kelvin/projects")
editor =("code")

class auto_project:

 def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        os.chdir("{0}".format(folder_name))
   
    return False
        

 def create_git_repo():
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")

 def create_github_repo():
   os.system("gh repo create ")

 def open_editor(editor) :
    os.system("{0} .".format(editor))


name_project=input("Enter the name of the project: ")
#if folder exists
if(auto_project.create_folder(name_project)==True):
 auto_project.create_git_repo()
 auto_project.create_github_repo()
 auto_project.open_editor(editor)

else:
     print("Folder already exist")
