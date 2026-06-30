pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Environment') {
            steps {
                sh 'pwd'
                sh 'python3 --version'
                sh 'node --version'
                sh 'npm --version'
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

        stage('Terraform Format') {
            steps {
                dir('terraform') {
                    sh 'terraform fmt -check'
                }
            }
        }

        stage('Terraform Init') {
            steps {
                dir('terraform') {
                    sh 'terraform init'
                }
            }
        }

        stage('Terraform Validate') {
            steps {
                dir('terraform') {
                    sh 'terraform validate'
                }
            }
        }

        stage('Terraform Plan') {
            steps {
                dir('terraform') {
                    sh 'terraform plan -out=tfplan'
                }
            }
        }

        stage('Ansible Deployment Validation') {
            steps {
                dir('ansible') {
                    sh 'ansible-playbook -i inventory.ini deploy.yml'
                }
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