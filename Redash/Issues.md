# Common Issues

## Issue 1
>
	(env) saasmate@saasmate:~/.../redash_dev$ bin/run ./manage.py check_settings
	Traceback (most recent call last):
	  File "/home/saasmate/workspace/redash/redash_dev/manage.py", line 6, in <module>
	    from redash.cli import manager
	  File "/home/saasmate/workspace/redash/redash_dev/redash/__init__.py", line 5, in <module>
	    import redis
	ImportError: No module named redis

### Soln: Dont use sudo while install pip packages

## Issue 2
>
  `File "/home/saasmate/workspace/redash/redash_dev/env/local/lib/python2.7/site-packages/flask_oauthlib/utils.py", line 5, in <module>
    from oauthlib.common import to_unicode, bytes_type
ImportError: cannot import name bytes_type`

### soln: [Reference](https://github.com/getredash/redash/issues/3266)
>
	(env) saasmate@saasmate:~/.../redash_dev$ pip install Flask-OAuthLib==0.9.5



## Issue 3
>
  `File "/home/saasmate/workspace/redash/redash_dev/env/local/lib/python2.7/site-packages/kombu/transport/redis.py", line 957, in _get_client
    'You have {0.__version__}'.format(redis))
VersionMismatch: Redis transport requires redis-py versions 3.2.0 or later. You have 2.10.5`

### soln:
>
	(env) saasmate@saasmate:~/.../redash_dev$ pip install redis==3.2.0


## Issue 4
 - After Installtion, http://localhost:8092?next=/ or anything auto redirect error 

### soln:
 - Check the .env, add `REDASH_HOST=http://192.168.100.86:8092`
 - [Check the nginx server configuration](files/nginx_site_redash)