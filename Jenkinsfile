pipeline {
    agent any

    stages {
        stage ('Build of Image') {
            steps {
                script {
                    dockerapp = docker.build("register.debugsystem.com.br/debugsystem/app-votacao:v2", '-f ./Dockerfile ./')

                }
            }
        }

        stage ('Push of image') {
            steps {
                script {
                    docker.withRegistry('https://register.debugsystem.com.br/debugsystem', 'harbor') {
                        dockerapp.push('latest')
                        dockerapp.push('v2')
                    }
                }
            }
        }
    }
}