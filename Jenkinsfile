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
    }
}