# Prerequisites

* Linux machine (preferably either Debian or Debian-based distribution)
* Minimum 2GB RAM
* Minimum 16GB HDD

Installation
---------------
### Ubuntu

1. Elevate first to ``root``.
```
user@host:~$ sudo -i
```
2. Update repo and install of dependencies.
```
root@host:~# apt-get update && apt-get install apache2 git python3 postgresql postgresql-contrib python3-dev libpq-dev python-pip curl ca-certificates python3-pip -y
```

3. Add a Linux user for use with this project. Let's call the user ``tiv`` and set a password.
```
root@host:~# useradd -m -d /home/tiv -s /bin/bash tiv && passwd tiv``
```

4. Get key for PostgreSQL and add it to the apt key sources keyring.
```
root@host:~# curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
```

5. Append PostgreSQL repo to the apt sources list.
```
root@host:~# echo deb http://apt.postgresql.org/pub/repos/apt bionic-pgdg main > /etc/apt/sources.list.d/pgdg.list
```

6. Install pgAdmin and follow the instructions (this requires that you have a desktop environment installed, if not; install `lightdm` or `gdm` also, or something else if you prefer)
```
root@host:~# apt-get update && apt-get install pgadmin4 -y
```

7. Edit the content in the pg_hba.conf file.
```
root@host:~# nano /etc/postgresql/10/main/pg_hba.conf
```

There is a line in the file like, change this from:

```local		all		postgres		peer```

to this:

```local		all		postgres,tiv		md5```

8. Start pgAdmin and follow the instructions (if any). Can not be run as root
```
user@host:~$ pgadmin4 (an admin password must at least be set)
```

9. Click on Create Server
```
General tab

Name: Name of database

Connection tab

Hostname/adresse: 127.0.0.1
Port: 5432
Maintenance database: postgres
Username: postgres
Password: The password you have created
Save password?: Yes 
```

10. Create an user/role for the user `tiv` and an database `tiv`. If you prefer to do this by the premade scripts, see point 10.4

10.1 Fill in `tiv` in the general tab.

10.2 Fill in an password.

10.3 Privileges: Choose `Yes` on `Can login?` and `Create databases?`.


Alternatively you can insert this by using an script (before this, make sure that you have the `create_tiv_user.sql` script in the `postgres` home directory with the correct file permissions).

If you are not going to use the script, skip this step.

10.4 Switch to the `postgres` user and insert the script.

```
root@host:~# su - postgres
postgres@host:~$ git clone https://github.com/orjanj/twitter-incident-visualizer.git
postgres@host:~$ cd twitter-incident-visualizer/sql/
postgres@host:̃~/twitter-incident-visualizer/sql$ psql < create_tiv_user.sql
```

You should be prompted with an password, then the role should have been created.

10.5 Right-click on databases and create an database for the `tiv` user.

Insert database name `tiv`, owner `tiv` and create.


Alternatively you can insert this by using an script (before this, make sure that you have the `create_tiv_db.sql` script in the `postgres` home directory with the correct file permissions).

If you are not going to use the script, skip this step.

10.6 Switch to the `postgres` user and insert the script.

```
postgres@host:~/twitter-incident-visualizer/sql$ psql < create_tiv_db.sql
```

11. Switch to the `tiv` user and create an database for the user. Then insert the database structure from the file `create_table_structure.sql`. The file `create_table_structure.sql` must be placed in the `tiv` home directory with the correct file permissions and ownership.

```
tiv@host:~$ git clone https://github.com/orjanj/twitter-incident-visualizer.git
tiv@host:~$ cd twitter-incident-visualizer/sql/
tiv@host:̃~/twitter-incident-visualizer/sql$ psql < create_table_structure.sql
```

12. Install Psycopg2, googlemaps and Twitter for Python.

```
root@host:~# pip3 install psycopg2 python-twitter googlemaps
```

Follow also the installation steps here: https://github.com/bear/python-twitter#getting-the-code

13. Restart the PostgreSQL service.
```
root@host:~# systemctl restart postgresql
```

14. Enable the CGI module in Apache.
```
root@host:~# a2enmod cgi
```

15. Insert the following lines below ``CustomLog`` in ``/etc/apache2/sites-enabled/000-default.conf`` to allow Python files to be runned in Apache. (as ``root``)

```
        <Directory /var/www/>
            Options Indexes FollowSymLinks MultiViews ExecCGI
            AllowOverride None
            Order allow,deny
            allow from all
            AddHandler cgi-script .py
         </Directory>
```

16. Restart Apache.

```
root@host:~# systemctl restart apache2
```

17. Change owner for the Apache Docroot to your user.
```
root@host:/var/www# chown -hR <your user>:<your group, same as username as usual> /var/www/html
```

18. Clone the newest version of the twitter-incident-visualizer repo to the web server
```
root@host:/var/www/html# git clone https://github.com/orjanj/twitter-incident-visualizer.git
```
19. Run interface.py to generate JSON structure 
```
generate web_application.json (for use on web app) run python3 interface.py
```
20. In config.JAML you can change the settings 
```
Change settings if needed
```
21. To access the demo site, open demo.html in your browser
```
Localhost or IP of your server/PC /twitter-incident-visualizer/examples/demo.html
```
