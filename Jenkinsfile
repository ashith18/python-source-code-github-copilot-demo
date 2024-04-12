node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        script {
            app = docker.build("my-app:${env.BUILD_NUMBER}")
        }
    }

    stage('Test image') {
        script {
            app.inside {
                sh 'echo "Tests passed"'
            }
        }
    }

    stage('Push image') {
        script {
            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                app.push("${env.BUILD_NUMBER}")
                app.push("latest")
            }
        }
    }

    stage('Trigger ManifestUpdate') {
        script {
            build job: 'ManifestUpdate', parameters: [string(name: 'IMAGE_TAG', value: "${env.BUILD_NUMBER}")]
        }
    }
}