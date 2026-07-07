pipeline {

    agent any

    stages {

        stage('Verify Environment') {
            steps {
                sh 'pwd'
                sh 'python3 --version'
                sh 'node --version'
                sh 'npm --version'
                sh 'ansible --version'
                sh 'kubectl version --client'
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
                    withEnv(["NEXT_PUBLIC_API_URL=/api"]) {
                        sh 'npm run build'
                    }
                }
            }
        }

        stage('Deploy RetailIQ') {
            steps {
                dir('ansible') {
                    sh '''
                    echo "Starting deployment..."

                    ansible-playbook \
                        -i inventory.ini \
                        playbook.yml \
                        --tags build,deploy

                    echo "Deployment completed."
                    '''
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