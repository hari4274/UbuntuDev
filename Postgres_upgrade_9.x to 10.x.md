Ref: https://stackoverflow.com/questions/46687645/upgrade-postgresql-from-9-6-to-10-0-on-ubuntu-16-10

Updating postgres 9.5 to 10.1 with database
-------------------------------------------

A Step-by-Step Guide
--------------------------
1) Make a backup. Make sure that your database is not being updated.

	pg_dumpall > outputfile

2) Install Postgres 10. Follow instructions on this page: 
	https://www.postgresql.org/download/linux/ubuntu/

Then run "sudo apt-get install postgresql-10", A newer version will be installed side-by-side with the earlier version.

3) Run "pg_lsclusters":

	Ver Cluster Port Status Owner    Data directory               Log file
	9.6 main    5432 online postgres /var/lib/postgresql/9.6/main /var/log/postgresql/postgresql-9.6-main.log
	10  main    5433 online postgres /var/lib/postgresql/10/main  /var/log/postgresql/postgresql-10-main.log

There already is a cluster main for 10 (since this is created by default on package installation). This is done so that a fresh installation works out of the box without the need to create a cluster first, but of course it clashes when you try to upgrade 9.6/main when 10/main also exists. The recommended procedure is to remove the 10 cluster with pg_dropcluster and then upgrade with pg_upgradecluster.

4) Stop the 10 cluster and drop it:

	sudo pg_dropcluster 10 main --stop

5) Stop all processes and services writing to the database. Stop the database:

	sudo systemctl stop postgresql 

6) Upgrade the 9.6 cluster:

	sudo pg_upgradecluster -m upgrade 9.6 main

7) Start PostgreSQL again

	sudo systemctl start postgresql

8) Run "pg_lsclusters". Your 9.6 cluster should now be "down", and the 10 cluster should be online at 5432:

	Ver Cluster Port Status Owner    Data directory               Log file
	9.6 main    5433 down   postgres /var/lib/postgresql/9.6/main /var/log/postgresql/postgresql-9.6-main.log
	10  main    5432 online postgres /var/lib/postgresql/10/main  /var/log/postgresql/postgresql-10-main.log

9) First, check that everything works fine. After that, remove the 9.6 cluster:

	sudo pg_dropcluster 9.6 main --stop


Some notes on pg_upgradecluster

This guide works fine for upgrading from 9.5 to 10.1. When upgrading from an older version, 
consider omitting -m upgrade on the step #6:

	sudo pg_upgradecluster 9.6 main

	sudo pg_ctlcluster 10 main start

If you have a really big cluster, you may use pg_upgradecluster with a --link option,
so that the upgrade will be in-place. However, this is dangerous — you can lose the cluster in an event of failure.
Just don't use this option if not necessary, as -m upgrade is already fast enough.
