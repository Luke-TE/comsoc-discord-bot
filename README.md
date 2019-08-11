# ComSoc Discord Bot
A satirical discord bot that conveys the themes of communism and the Soviet Union in an amusing manner.

This bot is used in a satirical Discord server based around communism and communist figures.

## PSA: This bot does not represent my or any of the developers' beliefs and is meant primarily as a humorous coding project.  

# Linux Installation instructions
Only Python 3.7 supports the latest asyncio operations.
```
# Install Python 3.7
sudo apt install python3.7

# Install PIP, Python's package manager
sudo apt install python-pip

# Install virtual environment 
python3.7 -m pip install virtualenv

# Create virtual environment for installing 
virtualenv bot-env

# Activate the virtual environment
source bot-env/bin/activate

# Install all the dependencies
python3.7 -m pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

```

### Adding a new feature:
Create a feature branch from the dev branch
Code the feature on the new branch  
Once the feature is done, push branch to origin so that Travis CI can build and test it
If the build passes, create pull request to merge feature to dev branch
If the pull request is approved, Travis CI builds and tests dev branch
If the build passes, hooray! A new feature has been implemented!

### Creating a release version:
Once enough new features are added to the dev branch and it has been approved by Travis CI
Create a pull request to merge it to the release branch
If the pull request is approved, Travis CI builds and tests release branch.
If the build passes, hooray! A new release version has been made! 
Travis CI deploys this to Heroku and a pull request to master can be made if so desired!

Possibly add test for new feature

Sentry intergration

Discord.py API docs
https://discordpy.readthedocs.io/en/latest/api.html#member

Pytest-asyncio API docs
https://github.com/pytest-dev/pytest-asyncio

Asynctest API docs
https://github.com/Martiusweb/asynctest


todo: Add git tags/version numbers
