pipeline {
	
	agent any
	
	environment {
		def j = ${env.JOB_NAME}.split('/')
		BRANCH = j[2]
	}
	
	stages {
		
		stage('Hello') {
			steps {
				sh "echo 'Hello world!'"
			}
		}
		
		stage('String manipulation') {
			
			steps {
				echo "{env.BRANCH}"
				echo "${env.JOB_NAME}"
			}
		}
	}	

}
