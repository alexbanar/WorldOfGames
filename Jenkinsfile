pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    //properties([pipelineTriggers([pollSCM('H/30 * * * *')])])
                }
                git branch: 'main', url: "https://github.com/alexbanar/WorldOfGames.git"
            }
        }
        stage('build') {
            steps {
                script {
                   if (Boolean.valueOf(env.UNIX)) {
                        sh 'docker build -t main-scores-image'
                        sh 'docker-compose up'
                        //sh 'docker-compose up --build'
                        //sh 'docker kill main-scores-image'
                       
                    } else {
                        bat 'docker build -t main-scores-image'
                        bat 'docker-compose up'
                        //bat 'docker-compose up --build'
                        //bat 'docker kill main-scores-image'
                   }
              }
          }
     }
     stage('test') {
       steps {
          script {
             if (Boolean.valueOf(env.UNIX)) {
                  dir('./test/') {
                    //sh 'python e2e.py'  
                     sh 'docker build -t test-scores-service-image' 
                     sh 'docker-compose up'
                 
             } else {
                 dir('.\\test\\') {
                        //bat 'python e2e.py'
                    bat 'docker build -t test-scores-service-image'
                    bat 'docker-compose up'
                    currentBuild.result = 'FAILURE'
                    //script {
                        error 'Test error'
                   //}
               try {
                    // do something that fails
                    //bat "exit 1"
                    bat "exit 0"
                    currentBuild.result = 'SUCCESS'
                     } catch (Exception err) {
                    currentBuild.result = 'FAILURE'
                     }
                     echo "RESULT: ${currentBuild.result}"
                     }      
             }
         }
         echo "RESULT: ${currentBuild.result}"
     }    
}
