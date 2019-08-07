# Github or any VCS, for private repositary pull and push every time asking username and password

 ### Ref :
  - [Stock Over Flow](https://stackoverflow.com/questions/11403407/git-asks-for-username-every-time-i-push/27007500)
  - [Github Fourm Help](https://gist.github.com/ahoward/2885020)

## Steps:
 1) Go to inside the repositary
  - `cd RepoName`
 2) Edit git config
  - `nano .git/config`
 3) Add the follwing Lines,
  ```
    [credential "https://repoURL.git"]
       username = GITUSER_NAME
  ```
4) Save and Close, Then pull and push only ask you for a password.
