# Project 12 (Julien Lamalle)

### This project was done in python <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="30" height="30"/> with django and django rest framework



To clone this folder, execute the following command:

```
git clone git@github.com:JulienLamalle/OC_DA_P12.git
```

From your terminal you can enter the project as follows:

```
cd OC_DA_PYTHON_P12
```

Now your have to create a virtual environment for this project using this command:

```
python -m venv env
```

Then you have to activate your environment:

```
source env/bin/activate
```

You now need to install all the libraries necessary for this project to work properly, for this you can run the following command:

```
pip install -r requirements.txt
```

Now you have to create a `.env` file at the root of this project with the following content:

```
SECRET_KEY='django-insecure-951l_c9b4mwqbv56pz)c)7z(71f3v6r-!(-o#w)qk_p7_aemxf'
DB_NAME='OC_DA_PYTHON_P12'
DB_USER='YOUR_PSQL_USERNAME'
DB_USER_PASSWORD='YOUR_PSQL_PASSWORD'
DB_HOST='localhost'
DB_PORT='5432'
```

Make sure that PostgreSQL is available on your system. You can find a detailed documentation of PostgreSQL by following this [link](https://www.postgresql.org/docs/)

In psql CLI you have to create a database with the name you have specified in the `.env` file. You can do this by running the following command:

```
CREATE DATABASE OC_DA_PYTHON_P12;
```


Then you have to create a user with the name you have specified in the `.env` file. You can do this by running the following command:

```
CREATE USER YOUR_PSQL_USERNAME WITH PASSWORD 'YOUR_PSQL_PASSWORD';
```

Then you have to grant the user the rights to create, read, update and delete on the database you have specified in the `.env` file. You can do this by running the following command:

```
GRANT ALL PRIVILEGES ON DATABASE OC_DA_PYTHON_P12 TO YOUR_PSQL_USERNAME;
```

You are now in the application folder with your environment launched and you database created, so you can access the django application using the following command:

```
cd src
```

To start the server locally, make sure you are in the src folder and run the following command:

```
python manage.py runserver
```

To create a superuser, run the following command:

```
python manage.py createsuperuser
```

You can access the management interface using this url: 

```
http://localhost:8000/management/
```

All the documentation for this project can be found in [here](https://documenter.getpostman.com/view/12983823/UVypzd4a)

### ENJOY 🎉 !
