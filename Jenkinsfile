pipeline {
    agent any
        //options {
            //parallelsAlwaysFailFast()  // https://stackoverflow.com/q/54698697/4480139
       //}
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('H/30 * * * *')])])
                }
                git branch: 'main', url: "https://github.com/alexbanar/WorldOfGames.git"
            }
        }
        


        //stage('Parallel') {
          //parallel {
              stage('build') {
                  steps {
                    script {
                       if (Boolean.valueOf(env.UNIX)) {
                            sh 'docker build -t main-scores-image'
                            sh 'docker-compose up -d'
                            //sh 'docker-compose up --build'
                            //sh 'docker kill main-scores-image'

                       } else {
                            bat 'docker build -t main-scores-image'
                            bat 'docker-compose up -d'
                            //bat 'docker-compose up --build'
                            //bat 'docker kill main-scores-image'
                       }
                    }
                 }
           }
           stage('test') {
              steps {
                script {
                  bat 'pip install selenium'
                  bat '.\\test\\e2e.py'
               }    
           }  
        //}
     //}
 }

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
}
