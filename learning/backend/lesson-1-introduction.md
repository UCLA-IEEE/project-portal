# Lesson 1: Introduction to Python, Flask, and Backend Development

During our first session we went over a lot of topics: backend development in general, Python, and the framework Flask. I'll go over each topic one-by-one, giving a little summary and learning resources, and finally a short little assignment at the bottom that will allow you to get familiar with the technologies.

## Python

Python is quite simple and easy to use, especially compared to a language like C++. I could write a whole lot about Python but [the docs](https://docs.python.org/3/tutorial/index.html) do a better job than I ever can. The Python docs are fantastic and I recommend you guys read up on these. Specifically:
* Chapters 1, 2, 3
* Chapter 4.1-4.7.1
* Chapter 5.1-5.6
* Chapter 6 (don't worry if this doesn't make too much sense)
* Chapter 7.1
* Chapter 12

This is a lot of stuff to read, but you don't need to know it inside and out. Most of it should do fine with a skim (such as most of chapters 1, 2, and 3) and maybe a little more time spent on some more complicated sections. The main goal is to get familiar with everything: you can always reference the documentation later.

## Flask

Flask is a powerful and simple framework that allows us to easily create web applications. It works by defining functions that correspond to specific routes. Check out the [Flask documentation](http://flask.pocoo.org/docs/1.0/) and more specifically the [quickstart](http://flask.pocoo.org/docs/1.0/quickstart/) for more information. There's no assigned reading, but definitely take a look around.

## Backend Development

### MVC
Building a server for the backend isn't all too complicated. Mostly we design our servers with a _Model View Controller_ (MVC) design pattern.
* The _model_ is the part of the server that deals with the data, typically by interacting with some sort of database.
* The _view_ is the part of the server that gets exposed to the world. In a server's case, this is usually an API with a set of routes. For example, a `/users` endpoint (an endpoint is just an accessible URL that the server will respond on).
* The _controller_ is the middleman between the two, often doing at least a little bit of extra work, such as checking for duplicates in a database before creating a new entry.

We will construct our server in a way that makes it easy for us to follow the MVC design pattern.

### HTTP
The next big concept is _HTTP_, which stands for HyperText Transfer Protocol. Esssentially, it is the way applications communicate data to each other.

There are HTTP requests and responses. Every request has a few important fields, but the most important is the _method type_. This can be one of GET, POST, PUT, or DELETE (as well as others which are not too important). Each one carries a different meaning. For example, if I send a GET request then it means I just want to get an object back from the server. If I send a POST request it means I want to create a new object on the server. Most POST/PUT requests also contain data. For example, if I POST the `/users` endpoint to create a user, the POST request would contain the information of the user I want to create.

After someone sends a request to a server, the server responds with an HTTP response. The response contains a _status code_. Some common status codes:
* 200 (OK). Means that the request was able to be properly handled.
* 404 (Not found). Means the requested resource could not be found on the server.
* 403 (Forbidden). Means the client does not have access to that specific endpoint.

There are many more that you can look up, which you definitely should if you come across an error code you do not recognize.

The second part of the response is the data. As opposed to requests, where there is often no data attached, for a response there is almost always data (which makes sense: usually when you ask a server for something, you expect something back!). This is usually just a copy of the resource you asked to GET or create with POST. So, if you GET `/users/robert` the server would send back all the data it has about the user "robert".

### RESTful APIs

Similar to how we use MVC to design the structure of our server, we can use the REST API design pattern to design our endpoints (so for example, that `/users` endpoint and others). If you look online, you'll see a lot of information and debates about REST APIs, but at their core they're quite simple.

REST APIs are build around _resources_. One resource gets one endpoint; no exceptions. So, we can define a `user` resource, which would get the `/users` endpoint. A resource is defined by various fields. For example, a `user` could consist of a username, password, enrolled projects, and other fields. And then, on these resources we define _methods_, which correspond to the HTTP methods we discussed above:
* GET will return the resource as a collection of its fields.
* POST will create a resource. Usually the HTTP request will specify all the fields for you.
* PUT will update a resource. Again, the HTTP request usually contains a copy of the updated object.
* DELETE will delete a specified resource.

That's not the whole story, but is good enough for a high-level overview. If you want to read more [this website](https://restfulapi.net/) provides a nice little introduction.

## The Command Line

Finally I'll give a very brief introduction to the command line. On Mac this is just the normal terminal, and on Windows you'll have to open the bash subsystem. The command line looks scary but just offers a convenient way to do things on your computer. We will use it to create and run our Python programs, and later on for other things such as git. After you open the command line, get a feel for some of the common commands:
* `pwd`. Stands for "print working directory", just prints the directory you are currently in. Usually this starts you off in the `~` directory, known as the _root_ directory. Here is where your Desktop, Documents, and other common folders are stored.
* `ls`. Lists all the items in the current directory.
* `mkdir <name>`. Creates a directory with the specified name. Try creating a test directory now, such as `test-dir`.
* `cd <directory_name>`. "Change directory", change to the specified directory. Use `cd` to navigate into your newly created `test-dir`. Then, use `pwd` to confirm that you did indeed change directory.
* `touch <file>`. This will create a file of the specified name. Try creating a file now, such as `test.txt`. You can then use `ls` to confirm that the new file is indeed there.
* `rm <file>`. Removes the specified file. Does _not_ put the file in the trash bin, it is gone forever! However, we can use `rm` to remove the new file we just created.

And that's it for the basics!

## Assignment

* Read all of the above, and any required reading.
* Download Python 3 (not Python 2!), and figure out how to get it running on your computer (you should be able to type "python3" onto a command line and see the prompt).
* Figure out how to create and run a Python file. You'll probably need another text editor besides Visual Studio or Xcode.
* Once you are able to run a file, you can play around with things that you learned from the documentation (or alternatively use the python3 prompt to start an interactive session). Get used to writing things like `if` statements and functions.
* Finally, follow the [Flask quickstart](http://flask.pocoo.org/docs/1.0/quickstart/) and get your server up and running. Once it is running, you can use a web browser to get responses from your server.
* Play around with Flask a little bit. Read the rest of the quickstart, see if you can create some other endpoints and do some different functionality.

That's it for this week!