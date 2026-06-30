pipeline {

    agent any

    stages {

        stage('Verify Environment') {
            steps {
                sh 'pwd'
                sh 'docker --version'
                sh 'terraform --version'
                sh 'ansible --version'
                sh 'kubectl version --client'
            }
        }

        stage('Backend Dependencies') {
            steps {
                dir('backend') {
                    sh 'python3 -m pip install --break-system-packages -r requirements.txt'
                }
            }
        }

        stage('Backend Syntax Check') {
            steps {
                dir('backend') {
                    sh 'python3 -m compileall app'
                }
            }
        }

        stage('Frontend Dependencies') {
            steps {
                dir('frontend') {
                    sh 'npm ci'
                }
            }
        }

        stage('Frontend Lint') {
            steps {
                dir('frontend') {
                    sh 'npm run lint'
                }
            }
        }

        stage('Frontend Production Build') {
            steps {
                dir('frontend') {
                    sh 'npm run build'
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker compose build'
            }
        }

    }

    post {

        success {
            echo 'RetailIQ CI Pipeline Passed!'
        }

        failure {
            echo 'RetailIQ CI Pipeline Failed!'
        }

        always {
            echo 'Pipeline Finished'
        }
    }
}