pipeline {
    agent any
    stages{

        // stage('Stage 0: Test'){
        //     steps{
               
        //         sh "bash testing.sh"

        //     }
        // }

        stage('Stage 1: Build'){
            steps{

                sh "docker-compose build"
                sh "docker-compose up -d"

            }
        }

        stage('Stage 2: Push'){
            steps{
                sh "docker ps && docker images"         // Here we push to DockerHub or Nexus so in the Deployment phase we can pull from there
                sh "docker-compose push"                // as it is best practice
                                                        //         Then potentially delete images since container should be running
            }                                            
        }
        // stage('Stage 3: Config'){
        //     steps{

                

        //     }
        // }
        // stage('Stage 4: Deploy'){                        //     And here we pull from Dockerhub instead of using local images
        //     steps{

        //         sh "docker stack deploy --compose-file docker-compose.yaml Sentencer"
                
        //     }
        // }
    }
}