# Project Portal

### Client setup
- Clone this repository (git clone \[url\])
- Navigate into the newly created `project-portal` directory
- Navigate into the "client" directory: `cd client`
- Install required dependencies: `npm install`
- Start the server: `npm run serve`

### Server setup

- Clone this repository (git clone \[url\])
- Navigate into the newly created `project-portal` directory (probably just `cd project-portal`)
- Navigate into the "server" directory: `cd server`
- Create a virtual environment: `python3 -m venv venv`. If this command doesn't work you may need to update your Python3 installation or install a special package (for Debian or Ubuntu).
- Activate virtual environment: `. ./venv/bin/activate`
- Install required dependencies: `pip install -r requirements.txt`
- Set up the database (see below)
- Start the Flask server: `make run`. Alternatively you can use the normal Flask command line tool: `flask run`.

You will also need to create the DB at some point on your local machine before you can use anything (see below).

Any other time you need to develop, all you need to do is `cd` into the `server` directory and activate your virtual environment again. 

#### DB Setup

- You'll need to create a `config.py` file in the `server/` folder with the variable `SQLITE_DB_URI` defined. You can use the following example

```
# config.py

SQLITE_DB_URI = 'sqlite:////tmp/test.db'
```

- You can run `python db-init.py` to create all database tables.
- You can also run `python db-restart.py` to delete and then recreate all tables. Be aware that running this will delete any data you have stored in your database.
