pipeline {
	
	agent any
	
	stages {
		
		stage('Hello') {
			steps {
				sh "echo 'Hello world!'"
			}
		}
		
		stage('String manipulation') {
			
			steps {
				echo "${env.JOB_NAME}"
			}
		}
	}	

}
