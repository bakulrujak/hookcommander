from utils.config import Config, main
from repo import aws, jaguar
from urllib import parse
from flask import Flask, request

app = Flask('__name__')

@app.route('/')
@app.route('/index')
def index():
	return "Hello home!"

@app.route('/get-instances/<string:tag_name>', methods=['GET'])
def getIntances(tag_name):
	return aws.get_ec2_all(parse.unquote(tag_name))

@app.route('/hook/testbvg', methods=['POST'])
def jaguar_fb():
	c = request.form
	if c['text'] == 'jaguar':
		r = jaguar.send_cmd()
		return r
	else:
		return 'Try again!'

@app.route('/ping', methods=['GET', 'POST'])
def ping_default():
	return "pong"

if __name__ == '__main__':
	app.run(
		host=main.host,
		port=main.port,
		debug=main.debug
	)
