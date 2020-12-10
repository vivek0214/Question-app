# Rest API services APP

## Tech/Framework used


- **Python** (v3.7)
- **MongoDB** (v4.0) 
    - ** mostly 3.6 and higher **


## Installation

### Mongodb Setup

Create Database

    use hps_goal_db

### Create db user
	db.createUser(
	    {
		    user: "rest_db",
		    pwd: "rest_pass123",
		    roles: [{ role: "dbOwner", db: "rest_db"}]
		}
    )
Create User collection

    db.creatCollection('goal')
    
### Virtual Env Setup

    virtualenv -p python3.7 <env_name>

### Activate Env

    . /path/to/env/bin/activate

### Run Server

    python server.py

### Install requirements

    pip install -r requirements.txt
## API Reference