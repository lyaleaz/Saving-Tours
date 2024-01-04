pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.10.4'
                }
            }
            steps {
		            withEnv(["HOME=${env.WORKSPACE}"]) {
		               sh 'pip install -r requirements.txt'
                       sh 'python manage.py makemigrations'
                       sh 'python manage.py migrate'

					}
			}
        }
        stage(' Unit Tests') {
            agent {
                docker {
                    image 'python:3.10.4'
                }
            }
            steps {
		            withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'python manage.py test'
		      }
			}
        }
        stage(' integration_test') {
            agent {
                docker {
                    image 'python:3.10.4'
                }
            }
            steps {
		            withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'python manage.py test --tag=integration_test'
		      }
			}
        }
        stage('coverage') {
            agent {
                docker {
                    image 'python:3.10.4'
                }
            }
            steps {
		        withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "python -m coverage run --include='project/*' manage.py test"
                    sh "python -m coverage report"		     
                }
			}
        }
        stage('pylint') {
            agent {
                docker {
                    image 'python:3.10.4'
                }
            }
            steps {
		        withEnv(["HOME=${env.WORKSPACE}"]) {
                    dir("SavingTours1"){
                        sh "python -m pylint settings.py"
                        sh "python -m pylint urls.py"
		    		}
		    		dir("project"){
                        sh "python -m pylint admin.py"
                        sh "python -m pylint urls.py"
                        sh "python -m pylint __init__.py"
		    		}		      
                }
			}
        }
	}
}