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
```bash
sudo apt-get update
sudo apt-get install mysql-server
pip install -U Flask-SQLAlchemy
pip freeze | grep Flask
```
resulted in these versions.
Flask==1.1.1
Flask-SQLAlchemy==2.4.1                                                 

installing mysql-python on windows-ubuntu was a little annoying.
```
sudo apt install default-libmysqlclient-dev
sudo -H pip install -U mysql-python
```




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
