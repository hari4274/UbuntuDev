# Redash Reporting tool local/server installation setps

#### Reference
- https://github.com/getredash/redash
- https://redash.io/help/open-source/dev-guide/setup
- https://redash.io/help/open-source/admin-guide/env-vars-settings

#### git clone

`git clone https://github.com/getredash/redash.git`

`cd redash`

#### Create virtual env(Python 2.7 recommended)

#### Install postgres
- https://www.postgresql.org/download/linux/ubuntu/

`sudo apt-get install postgresql-11`

`sudo apt install redis-server`

#### Creating virual environment
`virtualenv env`

`pip install -r requirements.txt -r requirements_dev.txt`

#### for optional db dependencies(optional)
`pip install -r requirements_all_ds.txt`


#### env setup(Postgres Setup)
`touch .env`

- add line (postgresql://DB_USER:PASSWORD@HOST/)
  REDASH_DATABASE_URL=postgresql://postgres:postgres@localhost/

  
#### npm package install
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
