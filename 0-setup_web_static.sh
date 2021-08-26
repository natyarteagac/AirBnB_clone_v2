#!/usr/bin/env bash
# Script that sets the web serves for the deployment

# Installing Nginx if it not already installed
if ! dpkg -s nginx  > /dev/null
then
	apt-get -y update
	apt-get -y upgrade
	apt-get -y install nginx
fi
# Writing the string on the index.nginx-debian.html
echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html
# Redirecting
sudo sed -i '/server_name _;/ a \\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default
# Creating file custom_404.html with string
echo "Ceci n'est pas une page" | sudo tee /usr/share/nginx/html/custom_404.html
# Appending information in default file
sudo sed -i "20i \\\terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\t root /usr/share/nginx/html;\n\tinternal;\n\t}" /etc/nginx/sites-available/default
sed -i "/http {/ a \\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf

# Creating if doesn't exists
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# Creating the file index.html
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
# Creating symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Giving ownership of data to ubuntu and group
sudo chown -R ubuntu:ubuntu /data/
# Creating an alias
sudo sed -i '/:80 default_server;/ a \\\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}/' /etc/nginx/sites-available/default
# Restarting nginx
sudo service nginx restart
