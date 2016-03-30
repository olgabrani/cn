# Django_cn

*Django_cn* is a web application that allows the students of the [Computer Network Laboratory](https://www.cn.ntua.gr/) of the [National Technical University of Athens](http://www.ece.ntua.gr/) to submit their assignments online.


## Description

Students can login using their academic credentials.
Once logged in, they view a list of the courses they are registered in via moodle.
The can choose to view an assigment and/or submit it.

Examiners can view students submissions online or download them as a pdf  and grade them. They can also view suggested answers.

Teachers can upload assignment and suggested answers and view all students' grades and submissions.


## Installation 

### Prerequisites

For a fully functional application you need to have a working [moodle](https://moodle.org/?lang=el) installation and read-only permissions to its database.
You also need to have an [ldap server](http://www.openldap.org/) that will store the users' credentials.

###  Instructions

*The installation instructions are for unix-systems only*


```bash
# install python-pip package manager
$ sudo apt-get install python-pip

# instal virualenvwrapper
$ sudo pip install virtualenvwrapper

# create virtualenv
$ mkvirtualenv django_cn

# activate django_cn virtualenv
$ workon django_cn

# install necessary python packages
$ apt-get install python-dev libmysqlclient-dev libldap-dev libsasl2-dev

# go to django_cn folder
$ cd <path-to-app>/django_cn

# install requirements
$ pip install -r requirements.txt

# create database 
$ python manage.py syncdb

# migrate database
$ python manage.py migrate

```

You will be prompt to create a superuser.

## Screenshots

#### Student's homepage

![Students homepage](/screenshots/student_homepage.png "Students Homepage")

#### Student submission page

![Student submission page](/screenshots/student_submission.png "Student Submission")

#### Examiner's view: students list

![Examiner view](/screenshots/examiner_students.png "Examiner's view")

#### Examiner's view: students grades

![Examiner view](/screenshots/examiner_grades.png "Examiner's view")





## Full thesis

The full thesis can be found [here](http://dspace.lib.ntua.gr/handle/123456789/39251) (in greek).




