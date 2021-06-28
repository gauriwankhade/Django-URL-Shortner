# Django-URL-Shortner

A simple web app built using Django that shorten URL given by user. 

* Fetures
  * Rest API for retriving data.
  * URL encoding based on [Base62](https://www.kerstner.at/2012/07/shortening-strings-using-base-62-encoding/).
  * Offline key Generation with seperate key storage.
  * Supports automatic key-generation based on given limit(Number of Keys to generate on one go)
  * Unittests
  * Swagger support to test API
  
  
* Set Up

  Download the zip or Clone this repository: ` git clone https://github.com/gauriwankhade/Django-URL-Shortner.git `

  Install the dependencies by simply executing: 
  
  ```
  pip3 install -r requirements.txt 
  ```

  Run this command to start the app: 
  
  ```
  python3 manage.py runserver
  ```

  Visit  ` 127.0.0.1:8000  `on your web browser.
  
  
  
* How to access API

  * to shorten url, send POST request to:  ` 127.0.0.1:8000/api/<url to be shortened>/ `
  
  * to retrieve url, send GET request to:  ` 127.0.0.1:8000/api/<short_urle>/ `
  
  Test Rest API on Swagger, user this endpoint
  
  ``` 
  http://127.0.0.1:8000/swagger/
  ```
  
* How to run unit tests

Use this command to run unit tests

``` 
 python3 manage.py test
```






  

  
  
