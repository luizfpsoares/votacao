pipeline {
    agent any

    stages {
        stage ('Build of Image') {
            steps {
                script {
                    dockerapp = docker.build("register.debugsystem.com.br/debugsystem/app-votacao:v1", '-f ./Dockerfile ./')

                }
            }
        }

        stage ('Push of image') {
            steps {
                script {
                    docker.withRegistry('https://gegister.debugsystem.com.br/debugsystem', 'harbor')
                        dockerapp.push('latest')
                        dockerapp.push('v1')
                }
            }
        }
    }
}