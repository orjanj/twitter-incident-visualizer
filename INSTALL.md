# Prerequisites

* Linux machine (preferably either Debian or Debian-based distribution)
* Minimum 2GB RAM
* Minimum 16GB HDD

Installation
---------------
### Ubuntu
1. Update repo and install of dependencies as elevated user ``root``.

``$ sudo apt-get update && sudo apt-get install apache2 git python3 postgresql postgresql-contrib -y``

2. Add a Linux user for use with this project. Let's call the user ``tiv`` and set a password.

``$ sudo useradd -m -d /home/tiv -s /bin/bash tiv && passwd tiv``

3. Delevate to the ``postgres`` user.

``$ sudo -i -u postgres``

4. Add a database user. Name the user the same as earlier added.

``$ createuser --interactive``

5. Create a database for the user

``$ createdb tiv``

6. Delevate to the ``tiv`` user.

``$ sudo -i -u tiv``

7. Test database connection with the ``tiv`` user

``$ psql``

``tiv=> \conninfo``

The result should be something like this:

``You are connected to database "tiv" as user "tiv" via socket in "/var/run/postgresql" at port "5432".``


8. Enable CGI in Apache (as ``root``)

``# a2enmod cgi``

9. Insert the following lines below ``CustomLog`` in ``/etc/apache2/sites-enabled/000-default.conf``:

```
        <Directory /var/www/>
            Options Indexes FollowSymLinks MultiViews ExecCGI
            AllowOverride None
            Order allow,deny
            allow from all
            AddHandler cgi-script .py
         </Directory>
```

10. Restart Apache (as ``root``)

``# systemctl restart apache2``


### Debian
1. Elevate to ``root``.

``$ su``

2. Update repo and install of dependencies.

``# apt-get update && apt-get install apache2 git python3 postgresql postgresql-contrib -y ``

3. Add a Linux user for use with this project. Let's call the user ``tiv`` and set a password.

``# useradd -m -d /home/tiv -s /bin/bash tiv && passwd tiv``

4. Delevate to the ``postgres`` user.

``# su - postgres``

5. Add a database user. Name the user the same as earlier added.

``$ createuser --interactive``

6. Create a database for the user

``$ createdb tiv``

7. Delevate to the ``tiv`` user.

``$ sudo -i -u tiv``

8. Test database connection with the ``tiv`` user

``$ psql``

``tiv=> \conninfo``

The result should be something like this:

``You are connected to database "tiv" as user "tiv" via socket in "/var/run/postgresql" at port "5432".``

9. Enable CGI in Apache (as ``root``)

``# a2enmod cgi``

10. Insert the following lines below ``CustomLog`` in ``/etc/apache2/sites-enabled/000-default.conf``:

```
        <Directory /var/www/>
            Options Indexes FollowSymLinks MultiViews ExecCGI
            AllowOverride None
            Order allow,deny
            allow from all
            AddHandler cgi-script .py
         </Directory>
```

11. Restart Apache (as ``root``)

``# systemctl restart apache2``
