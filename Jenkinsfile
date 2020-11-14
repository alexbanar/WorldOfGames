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
             
          }    
     }    
}
