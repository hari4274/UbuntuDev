# Redash Reporting tool local/server installation setps

#### Reference
- https://github.com/getredash/redash
- https://redash.io/help/open-source/dev-guide/setup
- https://redash.io/help/open-source/admin-guide/env-vars-settings
- [Configuration all - nice - gitgist](https://gist.github.com/mattes/f941cdc95639e482060a86b9f7ad983b)

#### git clone

`git clone https://github.com/getredash/redash.git`

`cd redash`

#### Create virtual env(Python 2.7 recommended)

#### Install postgres
- https://www.postgresql.org/download/linux/ubuntu/

`sudo apt-get install postgresql-11`

`sudo apt install redis-server`

#### Creating virual environment
`sudo apt-get install python-pip`

`sudo pip install virtualenv`

`virtualenv env`

`source env/bin/activate`

`pip install -r requirements.txt -r requirements_dev.txt`

#### for optional db dependencies(optional)
`pip install -r requirements_all_ds.txt`


#### env setup(Postgres Setup)
`touch .env`

- add line (postgresql://DB_USER:PASSWORD@HOST/)
  REDASH_DATABASE_URL=postgresql://postgres:postgres@localhost/

`echo "REDASH_DATABASE_URL=postgresql://postgres:postgres@localhost/" >> .env`

#### npm package install
`sudo apt install npm`

`npm install`

`npm run build`

#### Configuration check and verify
`bin/run ./manage.py check_settings`

#### Creating Database setup
- https://blog.theodo.com/2017/03/developping-a-flask-web-app-with-a-postresql-database-making-all-the-possible-errors/

`bin/run ./manage.py database create_tables`

#### Start seb server
`bin/run ./manage.py runserver --debugger --reload`

#### celery for log
`bin/run celery worker --app=redash.worker --beat -Qscheduled_queries,queries,celery -c2`

#### Starting Redash
`npm run start`

#### Install NGINX
`sudo apt-get install nginx`

#### Check running ports
`curl localhost:8080`

#### Add nginx configuration

`sudo nano /etc/nginx/sites-available/default`

- add the following lines

```
    server {
            listen 8092;
            listen [::]:8092;

            server_name _;


            #root /home/saasmate/workspace/jquery;
            #index index.html;

            location / {
                    add_header 'Access-Control-Allow-Origin' '*';
                    add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
                    add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range';
                    add_header 'Access-Control-Expose-Headers' 'Content-Length,Content-Range';
                    #try_files $uri $uri/ =404;
                    client_max_body_size 100M;
                    proxy_redirect off;
                    proxy_pass http://localhost:8080;
            }
    }

```



