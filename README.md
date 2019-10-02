# Purpose

This is a simple demo of a Create Read Update Delete database.
Instructions written for Ubunutu 18.04 on windows 10 and AWS.
setup date : October 2019

## Installation

This uses Python 3, MySQL, Flask-SQLAlchemy, MySQL-Python, virtualenv.

https://virtualenv.pypa.io/en/stable/
the security upgrade is worth doing.
https://mariadb.com/kb/en/library/documentation/clients-utilities/mysql_secure_installation/
My default configuration uses Anaconda python 3.
https://flask-migrate.readthedocs.io/en/latest/
```
sudo apt-get update
sudo apt-get install mysql-server
pip install -U Flask-SQLAlchemy
pip freeze | grep Flask
pip install Flask-Migrate
```

resulted in these versions.
Flask==1.1.1
Flask-SQLAlchemy==2.4.1                                                 

installing mysql-python on windows-ubuntu was a little annoying.
```
sudo apt install default-libmysqlclient-dev
sudo -H pip install -U mysql-python
```
NB: pip freeze will not find mysql-python
```
sudo apt list --installed | grep  mysql
```
does not list mysql-python, weird.

setup mysql as a service (wont work on windows-ubuntu, use for aws & ubuntu system)
```
sudo systemctl start mysql
sudo systemctl enable mysql
sudo systemctl restart mysql
service mysql status
service mysqld status
```

```
sudo apt-get install mysql-server
sudo apt-get install mysql-client
sudo apt-get install mysql-common
sudo /etc/init.d/mysql status
sudo /etc/init.d/mysql start
sudo /etc/init.d/mysql stop
```

if you attempt
```
sudo mysql  
```
and encounter this error message
```
ERROR 1045 (28000): Access denied for user 'bmt'@'localhost' (using password: NO)
```
then login as root, add new user and assign password, login as new user.
```
sudo mysql
#GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'bmt'@'localhost' IDENTIFIED BY '123456';
CREATE DATABASE demo_db;
show databases;
GRANT ALL PRIVILEGES ON demo_db . * TO 'bmt'@'localhost';
exit
#now login to new database as newly created user
mysql -u bmt -p
use demo_db
show tables;
```
These might be useful for ubuntu users YMMV
https://support.rackspace.com/how-to/installing-mysql-server-on-ubuntu/
https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04


useful checks for port, mysql default port is 3306
nb: does not work with ubuntu app on windows.
for windows use nmap > https://nmap.org
```
sudo lsof -i -P -n | grep LISTEN
sudo netstat -tulpn | grep LISTEN
sudo lsof -i:3306 ## see a specific port such as 22 ##
sudo nmap -sTU -O IP-address-Here
```
https://dev.mysql.com/doc/mysql-security-excerpt/5.7/en/changing-mysql-user.html


Setup project directory structure and files
```
mkdir app
touch app/__init__.py
touch app/templates
touch app/models.py
touch app/views.py
touch app/config.py
touch app/requirements.txt
touch app/run.py
```

```
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
