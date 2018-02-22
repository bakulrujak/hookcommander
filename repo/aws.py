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
	

def do_deploy(commit):
	client = boto3.client(
		'codedeploy',
		region_name=Config.region,
		aws_secret_access_key=Config.aws_secret_access_key,
		aws_access_key_id=Config.aws_access_key_id
	)

	response = client.create_deployment(
		applicationName='yojee-chat',
		deploymentGroupName='yojee-deployment',
		revision={
			'revisionType': 'S3',
			's3Location': {
				'bucket': 'andika-yojee',
				'key': 'yojee-pipeline/' + commit + '.zip',
				'bundleType': 'zip'
			}
		},
		deploymentConfigName='CodeDeployDefault.AllAtOnce',
		ignoreApplicationStopFailures=True,
		targetInstances={
			'tagFilters': [
				{
					'Key': 'envir',
					'Value': 'yojee-prod',
					'Type': 'KEY_AND_VALUE'
				}
			]
		},
		fileExistsBehavior='OVERWRITE'
	)

	return response