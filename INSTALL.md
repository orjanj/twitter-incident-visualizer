# Prerequisites

* Linux machine (preferably either Debian or Debian-based distribution)
* Minimum 2GB RAM
* Minimum 16GB HDD

Installation
---------------
### Ubuntu
1. Update repo and install of dependencies as elevated user ``root``.

``# sudo apt-get update && sudo apt-get install apache2 git python3 postgresql postgresql-contrib python3-dev libpq-dev python-pip curl ca-certificates -y``

2. Add a Linux user for use with this project. Let's call the user ``tiv`` and set a password. (as ``root``)

``# sudo useradd -m -d /home/tiv -s /bin/bash tiv && passwd tiv``

3. Get key for PostgreSQL and add it to the apt key sources keyring. (as ``root``)

``# curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -``

4. Append PostgreSQL repo to the apt sources list. (as ``root``)

``# echo deb http://apt.postgresql.org/pub/repos/apt bionic-pgdg main > /etc/apt/sources.list.d/pgdg.list``

5. Install pgAdmin and follow the instructions (this requires that you have a desktop installed, if not; install `lightdm` also) (as ``root``)

``# apt-get install pgadmin4 -y``

6. Edit the content in the pg_hba.conf file (as ``root``)
``# nano /etc/postgresql/10/main/pg_hba.conf``
There is a line in the file like, change this from:

```local		all		postgres		peer```

to this:

```local		all		postgres,tiv		md5```

7. Start pgAdmin and follow the instructions (if any). (as ``root``)

``# pgadmin4`` (an admin password must at least be set)

8. Create an user/role for the user `tiv` and an database `tiv`.

8.1 Fill in `tiv` in the general tab.

8.2 Fill in an password.

8.3 Privileges: Choose `Yes` on `Can login?` and `Create databases?`.


Alternatively you can insert this by using an script (before this, make sure that you have the `create_tiv_user.sql` script in the `postgres` home directory with the correct file permissions).

If you are not going to use the script, skip this step.

8.4 Switch to the `postgres` user and insert the script.

```
# su - postgres
$ psql < create_tiv_user.sql
```

You should be prompted with an password, then the role should have been created.

8.5 Right-click on databases and create an database for the `tiv` user.

Insert database name `tiv`, owner `tiv` and create.


Alternatively you can insert this by using an script (before this, make sure that you have the `create_tiv_db.sql` script in the `postgres` home directory with the correct file permissions).

If you are not going to use the script, skip this step.

8.6 Switch to the `postgres` user and insert the script.

```
# su - postgres
$ psql < create_tiv_db.sql
```

9. Switch to the `tiv` user and create an database for the user. Then insert the database structure from the file `create_table_structure.sql`. The file `create_table_structure.sql` must be placed in the `tiv` home directory with the correct file permissions and ownership.

```
# mv <path/to/file>/create_table_structure.sql /home/tiv
# chown tiv:tiv /home/tiv/create_table_structure.sql
# su - tiv
$ psql < create_table_structure.sql
```

10. Install Psycopg2 for Python (as ``root``)

``# pip install psycopg2``

11. Restart the PostgreSQL service (as ``root``)

``# systemctl restart postgresql``

12. Enable the CGI module in Apache (as ``root``)

``# a2enmod cgi``

13. Insert the following lines below ``CustomLog`` in ``/etc/apache2/sites-enabled/000-default.conf`` to allow Python files to be runned in Apache. (as ``root``)

```
        <Directory /var/www/>
            Options Indexes FollowSymLinks MultiViews ExecCGI
            AllowOverride None
            Order allow,deny
            allow from all
            AddHandler cgi-script .py
         </Directory>
```

14. Restart Apache (as ``root``)

``# systemctl restart apache2``

15. Navgate to the Apache Docroot

``# cd /var/www/html``

16. Clone the newest version of the twitter-incident-visualizer repo to the web server
``# git clone https://github.com/orjanj/twitter-incident-visualizer.git``
