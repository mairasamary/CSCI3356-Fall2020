Here I describe how to set up a Ubuntu 18 server to deploy a Django app using Django 3 and Python 3.8.

First we need to install git:

```bash
sudo apt update
sudo apt install git
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```

Now we can proceed and install our software.

SQLite3 first:


Python 3.8 requires SQLite 3.8.3 or later. The standard version of SQLite that Ubuntu 18 installs is 3.22. This is old and will not work. So we must instal SQLite and SQLite driver 3.8.3+ by compiling its source.

Visit [SQLite official page](https://www.sqlite.org/download.html) and find out which is the latest autoconf release version. At the time of this writing, the version was named like this:

```bash
sqlite-autoconf-3310100.tar.gz
```

Run the following commands on your server to download, unpack, configure and compile SQLite:

```bash
cd /opt
sudo wget https://www.sqlite.org/2020/sqlite-autoconf-3310100.tar.gz
sudo tar xvfz sqlite-autoconf-3310100.tar.gz
cd ./sqlite-autoconf-3310100
sudo ./configure --prefix=/usr --libdir=/usr/lib/x86_64-linux-gnu
sudo make
sudo make install
```

This will install SQLite in the place we need it.

Now, let's install Python 3.8 from source. Use the following command to install prerequisites for Python before installing it:

```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl
```

Now we can download the source, unpack, configure, compile and install python:
```bash
cd /opt
sudo wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
sudo tar xzf Python-3.8.2.tgz
cd Python-3.8.2
sudo ./configure --enable-optimizations
sudo make altinstall
```

Now your Ubuntu is fully configured with SQLite and Python 3 for our purposes.

Create a folder for git on your home folder and pull the source of our repository:

```bash
cd ~
mkdir git
cd ./git
git clone https://github.com/mairasamary/CSCI3356-Fall2020
```

Now you should have a folder named **django-deployment-example** under your git folder. Let's investigate it:

```bash
cd ./CSCI3356-Fall2020
ls -l

drwxr-xr-x 5 marquemo staff 4096 Apr 15 21:26 ButtonProject
```

There is only one project there for us: **ButtonProject**. Let's change to this folder and prepare it for running:

```bash
cd ./ButtonProject
pip3 install -r requirements.txt
python3 manage.py migrate
```
The file requirements.txt are the dependencies needed to run my example, if you want to generate a file for your project, on your computer run:
```bash
pip freeze > requirements.txt
```
This will generate a requirements with everything you need to run your project from Django.

You should see the following results:

```bash
Operations to perform:
  Apply all migrations: admin, auth, basic_app, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying basic_app.0001_initial... OK
  Applying basic_app.0002_systemstatus... OK
  Applying basic_app.0003_like_post... OK
  Applying basic_app.0004_auto_20200323_0353... OK
  Applying basic_app.0005_auto_20200323_0354... OK
  Applying basic_app.0006_auto_20200323_2301... OK
  Applying basic_app.0007_auto_20200416_1612... OK
  Applying basic_app.0008_auto_20200416_1612... OK
  Applying basic_app.0009_auto_20200416_1614... OK
  Applying sessions.0001_initial... OK
```

Setup for our database is done. We can run the application now:

```bash
python3 manage.py runserver 0.0.0.0:8000
```

You should see the following:

```bash
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
April 17, 2020 - 02:09:46
Django version 3.0.2, using settings 'ButtonProject.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

This is great! You can open the application now. Just be careful with two things:
- Your application is running **on the server**. To make django listen on port 8000 for connections coming from any interface, we started it with the 0.0.0.0:8000 parameter.
- If you try to open the URL above, your browser will not understand it. 
- We need to open the right resource on the right address of the server such as http://<your_server_name>:8000/basic_app/index. 
