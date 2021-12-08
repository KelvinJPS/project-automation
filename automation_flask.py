import os
from automation_project import auto_project
editor="code"

class flask_project():

 def create_files():
    os.system("touch Procfile")
    os.system("touch requirements.txt")
    os.system("touch README.md")

 def create_virtaulenv():
    os.system("virtualenv venv")
    os.system("source venv/bin/activate")


 def install_dependencies():
    os.system("pip3 install flask")
    os.system("pip3 install gunicorn")
    os.system("pip3 install freezer")





