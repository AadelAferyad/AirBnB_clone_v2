#!/usr/bin/env bash
# setup your web servers for the deployment of web_static

sudo apt update
sudo apt install -y nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
ls -L /data/web_static/current > /dev/null 2>&1 && rm -f /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
replacment="server_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "s@server_name _;@$replacment@" /etc/nginx/sites-enabled/default
sudo service nginx restart
