# Wine Cellar Sample Application (django-rest-framework + backbone + Twitter Bootstrap) #
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
