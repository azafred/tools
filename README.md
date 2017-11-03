# tools
A couple of tools I have written and decided to share


## gitrepos.py
This script will clone or pull every repo you have on your github account
which is either yours (public and private) or forked.
If the repo is a fork, it will store it in a 'forks' subdirectory

I recommend creating a Repos dir, cd'ing into it and running the script.
Edit the first lines in the script to replace your username / company /token.
```bash
mkdir Repos
cd Repos
gitrepos.py
```
