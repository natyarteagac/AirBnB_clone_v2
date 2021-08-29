#!/usr/bin/env bash
# Script that sets the web serves for the deployment

# Installing Nginx if it not already installed
if ! dpkg -s nginx  > /dev/null
then
	apt-get -y update
	apt-get -y upgrade
	apt-get -y install nginx
fi
# Creating if doesn't exists
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# Creating the file index.html
touch /data/web_static/releases/test/index.html
echo "Created succesfully" > /data/web_static/releases/test/index.html
# Creating symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Giving ownership of data to ubuntu and group
sudo chown -R ubuntu:ubuntu /data/
sudo chmod -R 755 /data/
# Creating an alias
sudo sed -i "/:80 default_server;/ a \\\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}/" /etc/nginx/sites-available/default
# Restarting nginx
sudo service nginx restart
