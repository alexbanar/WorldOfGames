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
        
       stage('build') {
            steps {
                bat 'docker build -t main-scores-image-new .'
                bat 'docker-compose up -d'
                //bat 'docker-compose up --build'
                //bat 'docker kill main-scores-image'
           }
       }
          
       stage('test') {
            steps {
                dir ('.\\tests'){
                    bat 'pip install selenium'
                    def OS_exit_code=bat 'python e2e.py'
                    bat 'echo OS_exit_code'
                }
           }
      }
   }
}
