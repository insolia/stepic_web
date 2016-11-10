sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default   

sudo ln -sf  /home/box/etc/hello.py /etc/gunicorn.d/hello.py

gunicorn -b 0.0.0.0:8000 ask.wsgi
   
