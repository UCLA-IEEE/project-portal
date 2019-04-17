# project-portal

### Server setup

- Clone this repository (git clone \[url\])
- Navigate into the newly created `project-portal` directory (probably just `cd project-portal`)
- Navigate into the "server" directory: `cd server`
- Create a virtual environment: `python3 -m venv venv`. If this command doesn't work you may need to update your Python3 installation or install a special package (for Debian or Ubuntu).
- Activate virtual environment: `. ./venv/bin/activate`
- Install required dependencies: `pip install -r requirements.txt`
- Start the Flask server: `flask run`

You will probably also need to create the DB at some point on your local machine (there should be some script or something... eventually).

Any other time you need to develop, all you need to do is `cd` into the `server` directory and activate your virtual environment again. 
