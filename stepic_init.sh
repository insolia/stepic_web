sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default   

sudo ln -sf  /home/box/etc/hello.py /etc/gunicorn.d/hello.py

sudo /etc/init.d/mysql start﻿

mysql -uroot -e "create database  IF NOT EXISTS ask_db"



gunicorn -b 0.0.0.0:8000 ask.wsgi
   
