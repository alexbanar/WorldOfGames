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
                     sh "pip install selenium"
                     sh 'python e2e.py'  
                     //sh 'docker build -t test-scores-service-image' 
                     //sh 'docker-compose up'
                 
             } else {
                 dir('.\\test\\') {
                        
                    //bat 'docker build -t test-scores-service-image'
                    //bat 'docker-compose up'
                    but "pip install selenium"
                    def OS_exit_code = bat 'python e2e.py' 
                    println("disk_size = ${disk_size}")
                     
                     
                     
                    currentBuild.result = 'FAILURE'
                    //script {
                        error 'Test error'
                   //}
               try {
                    // do something that fails
                    //bat "exit 1"
                   script { 
                    bat "exit 0"
                   }
                    currentBuild.result = 'SUCCESS'
                     } catch (Exception err) {
                    currentBuild.result = 'FAILURE'
                     }
                     echo "RESULT: ${currentBuild.result}"
                     }    
                     script {
                       error("Build failed because of this and that..")
                     }
                      docker-compose run/exec //do return exit codes of the container being run
 /*                     Options:
    --exit-code-from SERVICE   Return the exit code of the selected service container.
                               Implies --abort-on-container-exit.

    --abort-on-container-exit  Stops all containers if any container was stopped.
                               Incompatible with -d.

    -d                         Detached mode: Run containers in the background,
                               print new container names.
                               Incompatible with --abort-on-container-exit.
                               "--exit-code-from SERVICE" isn't too clear so i tested it really quick. it will return the actual exit code if you have the service that failed directly but if not, it returns a SIGTERM (128) – dtc Jun 3 at 0:51*/
             }
         }
         echo "RESULT: ${currentBuild.result}"
     }    
}
