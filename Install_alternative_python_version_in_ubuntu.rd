Ref : https://towardsdatascience.com/building-python-from-source-on-ubuntu-20-04-2ed29eec152b

sudo apt-get update
sudo apt-get install -y build-essential checkinstall

sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

cd /usr/src
sudo wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz

sudo tar xzf Python-3.6.9.tgz

cd Python-3.6.9
sudo ./configure --enable-optimizations

sudo make altinstall

python3.6 --version
