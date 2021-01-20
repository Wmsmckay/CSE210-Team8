This repository contains assignments for our class. Each week will have a a different folder and the code will be stored in there to keep things organized. Because I don't know how comfortable everyone is with Git and GitHub, I have included some "cheat codes" for them both.


--- How to clone the repository ---
In the command line, navigate to the folder where you would like to put the repository. Then type:

git clone https://github.com/Wmsmckay/CSE210-Team8



--- How to create your own branch ---
Once you have the repo cloned, you need to create your own branch. In the command line type:

git checkout -b "your name"

Make sure you replace "your name" with your name.



--- How to commit your changes ---
When you have made your changes you need to commit them. To commit changes you need to save your changes in the repository. Then type the following command with a short message that describes your changes:

git commit -m "add message here"



--- How to push your code to GitHub ---
After making changes you need to push your code to GitHub. To push your code you need to stage the changes and then push them. To stage the changes type:

git stage "filename.py"

Then, after that, push the code to your remote branch with:

git push origin "your name"



--- How to pull down changes ---
Before you start working on a project, you will want to ensure that you have the updated version of the repository. To do that, you will need to pull it down from GitHub. In the command line, type:

git pull origin master



