import os

class auto_project:
 os.chdir("/home/kelvin/projects")
 editor =("code")

 def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        os.chdir("{0}".format(folder_name))

    else: return False
   
 def create_git_repo():
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")

 def create_github_repo():
   os.system("gh repo create ")

 def open_editor(editor) :
    os.system("{0} .".format(editor))



