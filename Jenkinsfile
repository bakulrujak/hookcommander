pipeline {
	
	agent any
	stages {
		
		stage('set env') {
			steps {
				script {
					def j = "${env.JOB_NAME}.split('/')"
					def BRANCH = ${j[2]}
					echo "${BRANCH}"
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
				// echo "$BRANCH"
				echo "${env.JOB_NAME}"
				echo "${BRANCH}"
			}
		}
	}	

}
