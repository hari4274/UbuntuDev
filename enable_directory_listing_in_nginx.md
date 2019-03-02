
ref : https://nginxlibrary.com/enable-directory-listing/

Enabling directory listing in a folder in nginx is simple enough with just an <b>autoindex on;</b> directive inside the location directive. You can also enable sitewide directory listing by putting it in the server block or even enable directory access for all sites by putting it in the http block.

An example config file:

          server {
                  listen   80;
                  server_name  domain.com www.domain.com;
                  access_log  /var/...........................;
                  root   /path/to/root;
                  location / {
                          index  index.php index.html index.htm;
                  }
                  location /somedir {
                         autoindex on;
                  }
          }
