# Wine Cellar Sample Application (django-rest-framework + backbone + Twitter Bootstrap templating) #
"Backbone Cellar" is a sample application built with [Backbone.js](http://documentcloud.github.com/backbone/).

This project aims to go through the steps to tie this js lib to the django-rest-framework to see what the steps are to make this work.

Will also tie this to a bootstrap template

## Set up VirtualEnv
- $ mkvirtualenv djangoCellarTut
- $ workon djangoCellarTut
- $ pip install markdown
- $ pip install -r ./virtualenv_rf_requirements.txt 
- $ pip install -r ./virtualenv_rf_optionals.txt 
- $ pip install -r ./virtualenv_tut_requirements.txt

- $ django-admin.py startproject wine_cellar
- $ cd wine_cellar; python ./manage.py startapp cellar

-- interesting the startapp command in django 1.4 is now putting the app at the same level as the project root, follow up on this and figure out why this is --

### Install Initial Data fixture ###
chicken n egg problem. The Wine-Cellar tut from backbone was kind enough to provide a sql file with the initial set of data. Which I included here for completeness.. Note: the steps I am about to describe are going to become OBE as soon as I create a inital_data.json file. But I document them here for completeness.

- $ mysql cellar -uroot < cellar.sql
- $ python ./manage.py dumpdata --indent=3 cellar > cellar/fixtures/initial_data.json

### More Notes ###
## A sample Query
- [snippets][snip1]
- [snippets/1/][snip2]
- [snippets/1/?format=json][snip3]
- $ curl -X GET http://localhost:8000/snippets/1/ -H "Accept: application/json; indent=4"

[snip1]: http://localhost:8000/snippets/
[snip2]: http://localhost:8000/snippets/1/
[snip3]: http://localhost:8000/snippets/1/?format=json
[tut]: http://django-rest-framework.org/tutorial/1-serialization.html



1. [Backbone.js + Twitter Bootstrap](https://github.com/ccoenraets/backbone-cellar/tree/master/bootstrap) implementation
2. [Backbone.js Tutorial](https://github.com/ccoenraets/backbone-cellar/tree/master/tutorial): A four-part Backbone.js tutorial
