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
> `sudo ps -ax |grep odoo| awk '{print $1}'|xargs kill -9 $1`

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
