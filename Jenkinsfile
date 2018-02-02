pipeline {
	
	agent any
	
	stages {
		
		stage('Hello') {
			steps {
				sh "echo 'Hello world!'"
			}
		}
		
		stage('Run in retry mode') {
			
			options {
				timeout(time: 1, unit: 'MINUTES')
			}
			
			steps {
				sh "touch /root/this.txt"
			}
		}
	}	

}
