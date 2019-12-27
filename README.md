# Feature Request App

A "feature request" is a request for a new feature that will be added onto an existing piece of software. 

Assume that the user is an employee at IWS who would be entering this information after having some correspondence with
the client that is requesting the feature. 

The necessary elds are:

**Title:** A short, descriptive name of the feature request.

**Description:** A long description of the feature request.

**Client:** A selection list of clients (use "Client A", "Client B", "Client C")

**Client Priority:** A numbered priority according to the client (1...n).
<br>*Client Priority numbers **should not repeat** for the given client, so if a priority is set on a new feature as "1", then all other feature requests for that client should be reordered.

**Target Date:** The date that the client is hoping to have the feature.
Product Area: A selection list of product areas (use 'Policies', 'Billing',
'Claims', 'Reports')

# Stack
This application was made using Flask microframework with Python.

Front end technologies are Bootstrap (http://getbootstrap.com/), JQuery (http://jQuery.com/) and Jinja Template Engine (http://jinja.pocoo.org/).

All dependencies are listed in requirements.txt

# Running local
1) Create a virtualenv (https://virtualenv.pypa.io/en/latest/) 
2) Clone this repository to your local machine ` git clone https://github.com/ilitotor/featurerequestapp.git `
3) Enter in folder project called /featurerequesteapp 
4) Execute ` pip install -r requirements.txt `
5) Finally, execute:` python main.py `

# Testing
1) Run `python setup.py test`

# Deployment Version
https://featuretorquato.herokuapp.com/
