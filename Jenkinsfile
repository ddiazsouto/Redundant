pipeline {
    agent any
    stages{

        stage('Stage 1: Build/search'){
            steps{
                sh "apt-get install python3-pip"
            }
        }

        stage('Stage 2: Test/show'){
            steps{
                sh "ls -la"
            }
        }

        stage('Stage 3: Deploy/do'){
            steps{
                sh "echo 'Daniel' "
            }
        }
    }
}