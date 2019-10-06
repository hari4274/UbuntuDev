# Process Manager for individual scripts(node,py,sh or etc...)

### Links
 - [PM2](http://pm2.keymetrics.io/docs/usage/quick-start/)
 - [PM2 example - Medium](https://medium.com/@gokhang1327/deploying-flask-app-with-pm2-on-ubuntu-server-18-04-992dfd808079)
 
#### Sample example try to run python script with environment using pm2
```
 npm install pm2@latest -g
 sudo npm install pm2@latest -g
 sudo npm install -g npm
 pm2 plus
 pm2 list
 cd workspace/python/opencv-face-detector/
 pm2 start app.py --interpreter .env/bin/python
 pm2 log
 pm2 ls
 pm2 monit
 pm2 stop app
 pm2 delete app
 pm2 start app.py --interpreter .env/bin/python --name PyFace
 pm2 log
 pm2 stop PyFace
 pm2 delete PyFace
 pm2 start app.py --interpreter .env/bin/python --name PyFace --time
 pm2 log
 pm2 stop PyFace
 pm2 start app.py --interpreter .env/bin/python --name PyFace --time --log /Users/hariprasath/.pm2/logs/PyFace-error.log
 pm2 monit
 pm2 stop PyFace
 pm2 start app.py --interpreter .env/bin/python --name PyFace --time --log /Users/hariprasath/.pm2/logs/PyFace-error.log -- --host=0.0.0.0
 pm2 monit
 pm2 restart PyFace
 pm2 logs
 pm2 stop PyFace
```

### Odoo run via PM2
```
cd /opt/odoo/odoo12
pm2 start ./odoo-bin --interpreter .env/bin/python --name odoo12Demo -- --config=odoo12_conf.conf
pm2 ls
tail -f /var/log/odoo/odoo12/odoo12Demo-server.log
pm2 restart odoo12Demo
pm2 monit
pm2 delete odoo12Demo

```

