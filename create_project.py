from automation_project import auto_project


name_project=input("Enter the name of the project: ")
#if folder exists
if(auto_project.create_folder(name_project)!=False):
 auto_project.create_git_repo()
 auto_project.create_github_repo()
 auto_project.open_editor(auto_project.editor)

else:
     print("Folder already exist")