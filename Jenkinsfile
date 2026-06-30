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

        stage('Deploy RetailIQ') {
            steps {
                dir('ansible') {
                    sh 'ansible-playbook -i inventory.ini playbook.yml'
                }
            }
        }

    }

}