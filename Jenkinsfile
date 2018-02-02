pipeline {
	
	agent any
	
	stages {
		
		stage('Hello') {
			steps {
				sh "echo 'Hello world!'"
			}
		}
		
		stage('Run in retry mode') {
			
			opstions {
				retry(3)
			}
			
			steps {
				sh "touch /root/this.txt"
			}
		}
	}	

}
