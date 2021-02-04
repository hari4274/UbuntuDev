# UbuntuDev

### Ubuntu Realated Dev tips and tricks

1. [MySQL db remote connection establish with python example](mysql%20db%20remote%20connection%20establish%20with%20python%20example.txt)

2. [Postgres Upgrade 9.x to 10.x or latest](Postgres_upgrade_9.x%20to%2010.x.md)

3. [Postgresql Tutorial](https://www.systemcodegeeks.com/databases/postgresql/postgresql-database-tutorial/)

4. [Postgresql Replication Tutorial](https://www.systemcodegeeks.com/databases/postgresql/postgresql-hot-standby-database-replication/)
   - External Links:
     * https://severalnines.com/blog/top-pg-clustering-ha-solutions-postgresql
     * https://cloud.google.com/community/tutorials/setting-up-postgres-hot-standby
     * https://cloud.google.com/community/tutorials/setting-up-postgres

5. [How To Set Up SSH Keys on Ubuntu](rsync_ssh_copy_commands.sh)

6. To view cron logs in ubuntu:
> `grep CRON /var/log/syslog`

7. Kill all greb result in linux:
   - To kill all odoo services : `sudo ps -ax |grep odoo| awk '{print $1}'|xargs kill -9 $1`
   -  To Kill paricular Port : `sudo fuser -k 7073/tcp`

8. Dropbox upload script:
   * [Dropbox upload script Document](https://www.addictivetips.com/ubuntu-linux-tips/use-dropbox-from-the-linux-command-line/)
   > `wget https://raw.githubusercontent.com/andreafabrizi/Dropbox-Uploader/master/dropbox_uploader.sh && chmod +x dropbox_uploader.sh`
    
9. [External Application links not working(Blank chrome page opening)](https://askubuntu.com/questions/689449/external-links-are-opened-as-blank-tabs-in-new-browser-window-in-chrome)
    

10. [Install Redash reporting tool(Open source)](Redash/)

11. Pivot Views JS - Library
    * [Pivot JS - awesome - CSV or JSON](https://pivottable.js.org/examples/index.html)
    * [CSV File Map test](https://pivottable.js.org/examples/mps_csv.html)

12. Testing System performance Linux (Calculating 10000 Pi value)
    > `time echo "scale = 10000; 4 * a (1)" | bc -l`

13. [Set a Static IP on Ubuntu Server](https://www.howtoforge.com/linux-basics-set-a-static-ip-on-ubuntu)
14. [Delete all pyc files in current directory in terminal](https://blog.mozilla.org/webdev/2015/10/27/eradicating-those-nasty-pyc-files/)
   > `find . -name '*.pyc' -delete`
15. [Github or any VCS, for private repository pull and push every time asking username and password](github_credentials_setup.md)
16. [Postgresql Config File in  MAC OS](https://til.codes/postgresql-how-to-find-pg_hba-conf-file-using-mac-os-x/)
17. Restart postgreSQL in mac(without install brew):
  - `sudo su postgres && pg_ctl -D /Library/PostgreSQL/11/data/ status`
  - if Brew:
      * [Restarting postgresql in mac](https://tableplus.com/blog/2018/10/how-to-start-stop-restart-postgresql-server.html)
18. [Create Virtual environment in python](Create_virtual_environment.md)
19. [ProcessManager for individual scripts(node, py, sh or etc ...)](ProcessManager_for_microservices.md)
20. [GIT Cheatsheet pages](https://www.atlassian.com/dam/jcr:8132028b-024f-4b6b-953e-e68fcce0c5fa/atlassian-git-cheatsheet.pdf)
21. [GIT cherry pick commits](https://www.devroom.io/2010/06/10/cherry-picking-specific-commits-from-another-branch/)
22. [MacOS Shell change to bash](https://www.cyberciti.biz/faq/change-default-shell-to-bash-on-macos-catalina/) 
   - `cat /etc/shells`
   - `chsh -s /bin/bash`
23. [SQL based system query from facebook - Osquery](https://osquery.io)
24. [How to create a node-js module ?](https://www.digitalocean.com/community/tutorials/how-to-create-a-node-js-module)
25. [How to display data from the degitalocean api with django](https://www.digitalocean.com/community/tutorials/how-to-display-data-from-the-digitalocean-api-with-django)
26. [How to build a morden web application to manage with django and react on ubuntu -production deploy](https://www.digitalocean.com/community/tutorials/how-to-build-a-modern-web-application-to-manage-customer-information-with-django-and-react-on-ubuntu-18-04)
27. Github config commands:
   - Change Email : `git config --global user.email "email@ubuntu.com"`
   - Change Name : `git config user.name "Hariprasath"`
   - Dontconsider fiele permision changes : `git config core.fileMode false`
28. Http toolkit for testing requests : https://httptoolkit.tech/
29. Best JSON Formatter Online
   - http://jsonviewer.stack.hu/
   - http://chris.photobooks.com/json/default.htm
30. Online Photo editor : https://pixlr.com/x/
31. To get Analysis from explain with json in postgres:

`psql ejam_1910 -qAt -c "EXPLAIN (FORMAT JSON) select id from sale_order where fulfillment_order_id = '1213423423';" > /tmp/analyze.json`

use json to http://tatiyants.com/pev/#/plans/new

32. Grep command with before and after lines:(-A aftercount, -B beforecount)
   - `cat /var/log/app/server.log | grep -a -A 10 -B 30 "Expected singleton: object(44, 43)"`
