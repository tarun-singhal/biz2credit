# biz2credit

## To setup the Flask Framework
### Prerequisite of the project:


**Step 1:** Need to install the python3 

**Step 2:** GO to the project path directory i.e biz2credit_api directory

**Step 3:** Run the below command to activiate the flask env

$ source bin/activate

now you should see (flask) on the left of the command line. Let's install flask

**Step 4:** Install flask to run the REST API

**Step 5:** Need to install the python packages dependencies 

**Step 6** : Install python3 dependencies via pip3
$ pip3 install <package-name>

**Step 7:** Run the project via below command
$ python3 run-app.py



Run the REST API endpoint
1. http:localhost:5000/story : To post and get all story
2. http:localhost:5000/story/id : To delete/get/update specific story
3. http:localhost:5000/user : To get all user and create user
4. http:localhost:5000/user/id : to delete/get/update specific user

HTTPBASIC Auth: API authenitication require for all end points

**user : admin**

**password: SuperSecretPwd**

## To setup the Django project
**Step 1:** Go to project biz2credit directory

**Step 2**: install the virtualenv setup

$ virtualenv env

**Step 3:** Now, activate the virtual environment with the following command:

$ . env/bin/activate

**Step 4:** install django
$ pip install django

**Step 5** : Install python3 dependencies via pip3

**Step 6**: Run the APP
$ python3 manage.py runserver
Wil run on port no 8000

see the below url for the frontend:
1. http://127.0.0.1:8000/blog-list/ : To get the list of story
2. http://127.0.0.1:8000/blog    :: To create the story 

