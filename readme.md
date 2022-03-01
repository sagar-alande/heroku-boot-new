# Calculator Project Setup
[![Production Workflow](https://github.com/sagar-alande/heroku-boot-new/actions/workflows/prod.yml/badge.svg)](https://github.com/sagar-alande/heroku-boot-new/actions/workflows/prod.yml)
1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov
3. Add repository settings for action secrets for DOCKER_USERNAME, DOCKER_PASSWORD, HEROKU_API_KEY (put the appropriate
   values in)
4. Change line 45 to have your docker repo address
5. change lines 61 to have your heroku app name
6. change line 62 to have your heroku email
7. change line 19 of readme.md (this file) to have the link to your heroku app (click on the app and then there is a
   button to open the app in the upper right)  This will not work until it successfully deploys

### Heroku Notes: Get the heroku API key from account in: -> applications -> create authorization button
### GitHub Notes:  Set the action secrets repository in: -> settings -> actions -> secrets




.pylintrc is the config for pylint .coveragerc is the config for coverage setup.py is a config file for pytest

[My App](https://kwilliam-flask.herokuapp.com)
