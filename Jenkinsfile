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
                sh 'docker --version'
                sh 'terraform --version'
                sh 'ansible --version'
                sh 'kubectl version --client'
            }
        }

    }

}