pipeline {
	
	agent any
	
	stages {
		
		stage('Hello') {
			steps {
				sh "echo 'Hello world!'"
			}
		}
		
		stage('Run in retry mode') {
			
			steps {
				retry(3) {
					sh "touch /root/this.txt"
				}
			}
		}
	}	

}
