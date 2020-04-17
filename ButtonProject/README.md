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
sudo ./configure --prefix=/usr --libdir=/usr/lib64
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
export LD_RUN_PATH=/usr/local/lib
sudo ./configure --enable-optimizations
sudo make altinstall
```

Now your Ubuntu is fully configured with SQLite and Python 3 for our purposes.

Create a folder for git on your home folder and pull the source of our repository:

```bash
cd ~
mkdir git
cd ./git
git clone https://github.com/mairasamary/SE-Course-django-deployment-example--Ubuntu.git
```

Now you should have a folder named **django-deployment-example** under your git folder. Let's investigate it:

```bash
cd ./django-deployment-example
ls -l

drwxr-xr-x 5 marquemo staff 4096 Apr 15 21:26 ButtonProject
```

There is only one project there for us: **ButtonProject**. Let's change to this folder and prepare it for running:

```bash
cd ./ButtonProject
pip3.8 install -r requirements.txt
python3.8 manage.py migrate
```
The file requirements.tx are the dependencies needed to run my example, if you want to generate a file for your project, on your computer run:
```bash
pip freeze > requirements.txt
```
This will generate a requirements with everything you need to run your project from Django.

You should see the following results:

```bash
System check identified some issues:
WARNINGS:
basic_app.SystemStatus.date_changed: (fields.W161) Fixed default value provided.
        HINT: It seems you set a fixed date / time / datetime value as default for this field. This may not be what you want. If you want to have the current date as default, use `django.utils.timezone.now`
Operations to perform:
  Apply all migrations: admin, auth, basic_app, contenttypes, sessions
Running migrations:
  No migrations to apply.
  Your models have changes that are not yet reflected in a migration, and so won't be applied.
  Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
```

That is good! It is asking you to run **manage.py makemigrations**. So let's do it:

```bash
python3.8 manage.py makemigrations
```

You should see the following result:

```bash
System check identified some issues:
WARNINGS:
basic_app.SystemStatus.date_changed: (fields.W161) Fixed default value provided.
        HINT: It seems you set a fixed date / time / datetime value as default for this field. This may not be what you want. If you want to have the current date as default, use `django.utils.timezone.now`
Migrations for 'basic_app':
  basic_app/migrations/0007_auto_20200416_0346.py
    - Delete model Book
    - Alter field date_changed on systemstatus
```

It seems there are additional migrations necessary. So, let's repeat the migrations command:

```bash
python3.8 manage.py migrate
```

You should see a nicer message now:

```bash
System check identified some issues:
WARNINGS:
basic_app.SystemStatus.date_changed: (fields.W161) Fixed default value provided.
        HINT: It seems you set a fixed date / time / datetime value as default for this field. This may not be what you want. If you want to have the current date as default, use `django.utils.timezone.now`
Operations to perform:
  Apply all migrations: admin, auth, basic_app, contenttypes, sessions
Running migrations:
  Applying basic_app.0007_auto_20200416_0346... OK
```

Setup for our database is done. We can run the application now:

```bash
python3.8 manage.py runserver
```

You should see the following:

```bash
Watching for file changes with StatReloader
Performing system checks...
System check identified some issues:
WARNINGS:
basic_app.SystemStatus.date_changed: (fields.W161) Fixed default value provided.
        HINT: It seems you set a fixed date / time / datetime value as default for this field. This may not be what you want. If you want to have the current date as default, use `django.utils.timezone.now`
System check identified 1 issue (0 silenced).
April 16, 2020 - 03:51:03
Django version 3.0.2, using settings 'ButtonProject.settings'
Starting development server at http://127.0.0.1:8000/
```

This is great! You can open the application now. Just be careful with two things:
- Your application is running **on the server**. If you try to open the URL above, it will be trying to open the application on your machine because 127.0.0.1 is the loopback IP address that is always your machine. So you need to replace 127.0.0.1 for the IP or the name of your server.
- Even if you fix the IP/name of the server, we need to open the right resource on our application such as http://<your_server_name>:8000/basic_app/index.
