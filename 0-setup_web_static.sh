#!/usr/bin/env bash
# Script that sets the web serves for the deployment
# of web_static

# If nginx is not installed do it.
if [ ! -x /usr/sbin/nginx ]
then
    sudo apt-get -y install nginx
else
    :
fi
sudo service nginx start
# Creating if doesn't exists
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# Creating the file index.html
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
# Creating symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
# Creating an alias
sudo sed -i "/:80 default_server;/ a \\\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\tautoindex off;\n\t}/" /etc/nginx/sites-available/default
# Restarting nginx
sudo service nginx restart
