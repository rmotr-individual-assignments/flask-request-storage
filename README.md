# Flask Request logger

**You're going to build your first REST API!** Seriously, and you'll see how simple it is.

In this assignment you have to build a system that saves (logs) all the requests that it receives. It has two simple endpoints. One of them is `/home`. **ANY** valid request to `/home` should be stored in a database. And then we have `/dashboard` that basically creates a report of all the requests that `/home` has received. Suppose that we send the following requests:

* 1 GET request.
* 2 POST requests
* 0 PUT requests (we don't send any).
* 1 PATCH request
* 3 DELETE requests

We've, in total, sent 7 requests. Our dashboard should look something like:

![rmotr flask dashboard](https://cloud.githubusercontent.com/assets/872296/24013959/e0332298-0a61-11e7-8aff-648b77a6da0a.png)

**Go to app.py and get started, you'll see the barebones for you to write your code**

## Testing your app

Aside from running the test commands, you can of course just navigate to `http://localhost:8080/home` and submit a few GET requests. If you want to send other types of requests we've included a command `ping_api.py` that lets you submit any type of request to a given URL. Usage:

```bash
$ python ping_api.py POST  # Submit a POST request to http://localhost:8080/home
$ python ping_api.py PUT  # Submit a PUT request to http://localhost:8080/home
$ python ping_api.py DELETE  # Submit a DELETE request to http://localhost:8080/home
$ python ping_api.py GET -u http://google.com/home # Submit a GET request to http://google.com/home
```

As you can see, you just have to pass the method and **optionally** the URL. By default, it's `http://localhost:8080/home`.

## Database

The database for this project contains only one table (you can see the code in `requests-schema.sql`) that contains info about every request made (url and method). We'll use sqlite3 for this project. The database is already created in `requests.db` and committed to the git repo for your simplicity. But you can always regenerate it by executing the following command:

```bash
$ sqlite3 requests.db < requests-schema.sql
```
