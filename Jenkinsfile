node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("ashithss/packages")
    }

    stage('Test image') {
        app.inside {
            sh 'python3 -m unittest'
        }
    }

    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'dockerHubCredentials') {
            app.push("${env.BUILD_NUMBER}")
        }
    }

    stage('Trigger ManifestUpdate') {
        build job: 'ManifestUpdate', wait: false
    }
}