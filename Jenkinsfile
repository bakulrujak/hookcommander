pipeline {
	
	agent any
	stages {
		
		stage('set env') {
			steps {
				script {
					def (x, y, z) = "${env.JOB_NAME}.split('/')"
					// def BRANCH = j[2]
					echo "${z}"
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
				echo "${z}"
			}
		}
	}	

}
