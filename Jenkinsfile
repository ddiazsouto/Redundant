pipeline {
    agent any
    stages{

        stage('Stage 1: Build/search'){
            steps{
                sh "whoami && ls"
            }
        }

        stage('Stage 2: Test/show'){
            steps{
                sh "docker ps"
            }
        }

        stage('Stage 3: Deploy/do'){
            steps{
                sh "pwd && ls"
            }
        }
    }
}