* **Author**: Jayesh Sidhwani

99movies is a small project to learn Flask and AngularJS

###Requirements

Requirements are listed in the requirements.txt

###Installation

* Checkout the Github repo
* Install virtualenv
* Install requirements
* Start API server: python api/manage.py
* Start APP server: python app/manage.py
* API runs at localhost:5000 and APP runs at localhost:80


####Functionalities

##### `Home Page`
```
URL:            'localhost/'
DESCRIPTION:    Lists all the movies. Depending on the authentication; you can edit or delete the movie.
```
---

##### `Login`
```
URL:            'localhost/login'
DESCRIPTION:    You can login using the login box given at the top of the page. The login enables authentication / authorisation.
                By default, you can only view all the movies. You need to be an 'admin' to edit and a 'super_admin' to delete a movie
                To simplify things, you can become one by using the respecting role as password.
                So for admin; username can be anything but password needs to be 'admin' likewise for 'super_admin'

                The authentication is enabled by using tokens to-fro from app to api. At the time of login, the API registers the new
                user and it's type and returns a token. For all subsequent communications with the API, the APP sends this token.
                If the token is validated by the API by checking in the MongoDB, the APP is allowed access for the particular
                resource otherwise error is thrown.
```
---

##### `Search`
```
DESCRIPTION:    The search box at the top could be used to search across Movie Name, Director / Actor Name. The logic begind
                search can be found in search method in api/utils/movies/
                This search can be fairly enhanced by using a token-based search engine like Solr / Elastic Search
```
---