# Useful information

How to configure your Postgres environment

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

Same information for those one who does not like English (yet)

https://timeweb.com/ru/community/articles/kak-ustanovit-postgresql-na-ubuntu-18-04-1

Links for windows

https://www.w3resource.com/PostgreSQL/connect-to-postgresql-database.php

> - sudo -u postgres psql
> - postgres=# create database cursor_db;
> - postgres=# create user cursor with encrypted password 'very_secret_password';
> - postgres=# grant all privileges on database cursor_db to cursor;
> - postgres=# ALTER USER cursor WITH SUPERUSER;
> - postgres=# \q;


From linux shell
    psql -h localhost -U cursor -d cursor_db -p 5433 ( or 5432 based on your version of OS)


If you catch this error installing psycopg2 in your virtual env
```
    Error: b'You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for building a client-side application.\n'
```

Running next commands could fix your problem

```
sudo apt-get install postgresql
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
sudo apt-get install python3.7-dev

```

## psql
If you are logged in postgress shell you will seee
```
$ psql -h localhost -U cursor -d cursor_db -p 5432
Password for user cursor:
psql (12.1 (Ubuntu 12.1-1.pgdg18.04+1))
Type "help" for help.

cursor_db=#
```
To see all possible commands insert `\?`

About basic commands in psql you could read here
http://www.postgresqltutorial.com/psql-commands/

## Creating python environment
To create python environment go into `green_lantern/lantern/relational_database`

```
$ virtualenv env -p python3.7
$ source env/bin/activate
(env) $ pip install -r requirements.txt
(env) $
```

If you can connect to database with psql but still can't connect with
python code please edit next file
`/etc/postgresql/<YOUR POSTGRESS VERSION>/main/pg_hba.conf`
for version number check dir /etc/postgresql/
and change `local all all peer` to `local all all password`

Then you need to restart your postgres service

```
sudo service postgresql restart
```

If you still have problems with installing pyscopg2

try to do next

```
ls -la /usr/lib/postgresql/
# look on version of postgress

export PATH=/usr/lib/postgresql/your_version_here/bin/:$PATH

```


```.env
sudo apt install build-essential
```
