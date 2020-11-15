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
                    //exit_code = bat(script: 'python e2e.py', returnStdout: true)
                    script { 
                        //try {
                        // do something that fails
                        //bat "exit 1"

                    def exit_code=bat ('python e2e.py')
                    //script {
                            //def exit_code = bat "python e2e.py"
                            bat "echo '${exit_code22}'"
}
                            //currentBuild.result = 'SUCCESS'
                         //} catch (Exception err) {
                            //currentBuild.result = 'FAILURE'
                         //}
                        // echo "RESULT: ${currentBuild.result}"
                    //}

                }
           }
      }
   }
}
