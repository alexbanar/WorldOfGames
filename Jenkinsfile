pipeline {
    agent any       
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('H/30 * * * *')])])
                }
                git branch: 'main', url: "https://github.com/alexbanar/WorldOfGames.git"
            }
        }
        


       //stage('build') {
       //     steps {
          //              bat 'docker build -t main-scores-image .'
          //              bat 'docker-compose up'
          //              //bat 'docker-compose up --build'
          //              //bat 'docker kill main-scores-image'
            //}
      // }
           //stage('build') {
              //steps {
                   // bat 'docker build -t main-scores-image .'
      //            bat 'docker-compose up'
      //            //bat 'docker-compose up --build'
      //            //bat 'docker kill main-scores-image'

               //}
          //  }
            stage('test') {
                steps {
                    dir ('..\\..\\.\\tree\\main\\tests'){
                        bat 'pip install selenium'
                        bat 'python e2e.py'
                    }
                }
            }
        //}
            //stage('test') {
            //      bat 'pip install selenium'
            //      bat 'python .\\test\\e2e.py'
            //}
    }
}
