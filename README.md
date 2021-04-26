# git
all git commands

Install Git on Ubuntu
_______________________

$sudo apt update 

$sudo apt install git -y

verify version
---------------------------
$git --version

You may view additional help on each command following the syntax git help <command>. For this you must first install git man pages using the command sudo apt-get install git-man


Once done use the help of the init command with the command git help init and identify the option used to create a bare repository.

Initialize a local Git Repository
$git init

Verify
$ls -a
. .. .git

Save a file to local git repository
$touch lion-and-mouse.txt
$sarah $ echo "A Lion lay asleep in the forest" >> lion-and-mouse.txt 
$git status

GIT CONFIG

git config user.email sarah@example.com

git config user.name sarah

Ignore a File
Add a file to .gitignore
echo notes.txt >> .gitignore

All files to be ignored by Git
cat .gitignore 
