#!/usr/bin/env bash

# https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1604

ssh-keygen

cat ~/.ssh/id_rsa.pub | ssh hari@192.168.0.127 "mkdir -p ~/.ssh && touch ~/.ssh/authorized_keys && chmod -R go= ~/.ssh && cat >> ~/.ssh/authorized_keys"

rsync -e ssh hari@192.168.0.127:/home/hari/Desktop/service_start/SourceDevBackupRemote/* /home/hari/Desktop/service_start/LocalDevBackup/


# Examples : https://www.fastwebhost.in/blog/13-rsync-command-examples-on-linux/
