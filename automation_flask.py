import os
from automation_project import auto_project

class flask_project():


 def create_files():
    os.system("touch Procfile")
    os.system("touch requirements.txt")
    os.system("touch README.md")
    os.system("touch app.py")
    os.system("touch runtime.txt")

 def create_virtual_environment():
    os.system("python3 -m venv venv")
     

 def install_dependencies():
    pip = "venv/bin/pip3"
    os.system("{0} install flask".format(pip))
    os.system("{0} install gunicorn".format(pip))
    os.system("{0} install freezer".format(pip))
    os.system("{0} freeze > requirements.txt".format(pip))
 
  
 def fill_runtime():
    python3 = "venv/bin/python3"
    os.system("{0} --version > runtime.txt".format(python3))
