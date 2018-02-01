import boto3
from utils.config import Config
from flask import jsonify

def get_ec2_all(tag_name):
	client = boto3.client(
		'ec2',
		region_name=Config.region,
		aws_secret_access_key=Config.aws_secret_access_key,
		aws_access_key_id=Config.aws_access_key_id
	)

	response = client.describe_instances(
		Filters=[
			{'Name': 'tag:kurio:service', 'Values': [tag_name]},
			{'Name': 'instance-state-name', 'Values': ['running']}
		]
	)

	ips = {}

	for reservations in response['Reservations']:
		for instance in reservations['Instances']:
			ips[instance['InstanceId']] = instance['PublicIpAddress']

	return jsonify(ips)
	