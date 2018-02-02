pipeline {
	
	agent any
	stages {
		
		stage('set env') {
			steps {
				script {
					def j = "${env.JOB_NAME}.split('/')"
				}

				environment {
					BRANCH = j[2]
				}
			}
		}
		
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
