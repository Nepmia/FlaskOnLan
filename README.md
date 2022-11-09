## REST API Django Basic Template
This repository is a template repository allowing the creation of a basic DRF powered django, it is initialized and is ready to be used to develop a REST API.

## Setup / Settings
This django setup works in a different way than the vanilla django settings, its settings are splitted bewteen prod env and dev env. Environ settings must be set inside the `.env` as `DJANGO_ENV` (like `App.settings.prod`), you wanna call the module settings from our app with either prod / dev. Be reminded that every settings inside `base.py` contains rules and settings shared by both prod and dev environment. To set specific settings, set them directly inside their corresponding py file.

  You can also generate new env type by creating a new file in settings, then import everything from `base.py` inside, then you just have to call this newly created env to use it.
  
  You are expected to generate a new django token inside `.env`.
  
  Default route for the API app is `api/`

## Environment
This django comes with `python-dotenv` allowing you to use and set environment variables easely, there is a file called `environ.py` inside the app helpers, there you can import any env variable you later need and just `from App.helpers.environ import THE_ENV_VAR` to use it. 

## Admin App and debug mode
Django admin app is enabled as it is usually required in developement, don't forget to remove / disable / hide it when you deploy to your prod, as well as the debug mode. 

## Database
This template is by default using a SQLlite db, database settings are splitted between prod and dev, meaning you can use different dabases depending on your env, e.g. PG on prod.

## Important note
This django template is delivered with `api` app created inside, you are expected to use this stock app for your REST API, however, as django is very modular you can totally create / import any other apps you need and just delete DRF + API app to make a fullstack django or whatever. I personally recommend staying on a REST API to use a JAMStack as it is for me the most efficient way to make webapps nowaday, but your code, your choice!

###### PS: If you're interested in doing JAMStacks but you're not sure which front framework you should use I totally recommend you to use Vue!
