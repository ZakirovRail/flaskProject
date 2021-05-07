1. Create virtual environment
$ python3 -m venv /Users/zakirovrjicloud.com/Desktop/Flask/Flask/venv
   
clear
2. Activate created venv
$ source venv/bin/activate


3. Install Flask and other libraries
$ pip install flask 

4. Run project
$ python3 wsgi.py
   
5. export libraries to requirements.txt
https://pip.pypa.io/en/stable/user_guide/#requirements-files
https://www.jetbrains.com/help/pycharm/managing-dependencies.html#configure-requirements

$ pip freeze > requirements.txt


# import sys
# sys.path.append('../')
# sys.path.append('/')