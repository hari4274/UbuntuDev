
Create Python Virtual Environment In Ubuntu
-------------------------------------------

        View Installed Packages in PIP:

            pip list

        Install Vitual Environment:

            sudo pip install virtualenv

        Create Folder:
            
            mkdir Environments

            cd Environments/

        Create Virtual Environment

            virtualenv project1_env

        Create Virtualenv with specific python3

            virtualenv -p /usr/bin/python3 py3_env

        Activate:
            
            source project1_env/bin/activate

        Deactivate:
            
            deactivate


        Create Requirements.txt in current env:

            pip freeze --local > requirements.txt

        Install Requirements.txt:

            pip install -r requirements.txt

        Remove Virtual environment:
            
            rm -rf py3_env

Note:
-----
    Don't put any project files inside virtual environment folder(py3_env).
    Because we use that for only differentiate python packages for every projects.
