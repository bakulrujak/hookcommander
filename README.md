# hookcommander
Simple python script to send command using HTTP or commandline to AWS. Powered by Flask and boto3

## Requirements
- boto3
- Flask
- paramiko

## Install
- Config file is located at `utils/config.py`, contains AWS credentials, HTTP port (for Flask), and other parameters.
- Install all requirements `pip3 install -r requirements.txt`

## Run flask
- Run command `python3 main.py`
- No usage guideline for Flask (RESTful API) for now. Please stay tune.

## Usage in CLI yojee-chat deployment
- Run command `./pydeployr.py [commit ID]`
