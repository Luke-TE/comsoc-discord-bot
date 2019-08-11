# ComSoc Discord Bot
A satirical discord bot that conveys the themes of communism and the Soviet Union in an amusing manner.
This bot is used in a satirical Discord server based around communism and communist figures.

The bot uses Travis CI, Heroku and Sentry. Travis CI builds and tests the core functionality of the bot. The bot is deployed on Heroku and Sentry is used for error tracking.

### PSA: This bot does not represent my or any of the developers' beliefs and is meant primarily as a humorous coding project.

## Linux Installation instructions
If you wish to run any of the code in the same environment as the Heroku server, you can use virtualenv.
Python 3.7 must be used as the asyncio operations used are only supported in Python versions from Python 3.7.
```
# Install Python 3.7
sudo apt install python3.7

# Install PIP, Python's package manager
sudo apt install python-pip

# Install virtual environment 
python3.7 -m pip install virtualenv

# Create virtual environment for installing the dependencies
virtualenv bot-env

# Activate the virtual environment
source bot-env/bin/activate

# Install all the dependencies
python3.7 -m pip install -r requirements.txt

# Deactivate the virtual environment when it is no longer needed
deactivate

```

# Running the program
```run.py``` can only be run on the Heroku server as it requires the bot token and the sentry connection data.
```
python3.7 src/run.py
```

### Adding a new feature:
- Create a feature branch from the dev branch
- Code the feature on the new branch  
- (Optional) Add a test for the new feature
- Once the feature is done, push the branch to origin and create a pull request to merge the feature to the dev branch
- Travis CI builds and tests the pull request
- If the build passes, hooray! A new feature has implemented!

### Deploying a new version to the server:
- Create a pull request to merge the dev branch to the deploy branch
- Travis CI builds and tests the pull request
- If the build passes and someone else has approved the pull request, hooray! A new release version has been made! This is automatically deployed to Heroku! If there are any errors with it, Sentry sends an email alert.


## TODO
- [ ] Add test for verifying that the bot can connect
- [ ] Add voice support
- [ ] Add git tags/version numbers


## Reference
Discord.py API docs
https://discordpy.readthedocs.io/en/latest/api.html#member

Pytest-asyncio API docs
https://github.com/pytest-dev/pytest-asyncio

Asynctest API docs
https://github.com/Martiusweb/asynctest
