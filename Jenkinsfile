pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
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
                    } else {
                        bat 'docker build -t main-scores-image'
                        bat 'docker-compose up'
                    }
                }
            }
        }
    }
}
