node {
    def app
    // Check Docker version
    stage('Check Docker') {
        script {
            sh 'docker -v'
        }
    }
    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        script {
            docker.withRegistry('tcp://10.22.208.108:4243', 'dockerengine') {
             app = docker.build("ashithss/packages")   
            }  
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
            docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                app.push("${env.BUILD_NUMBER}")
            }
        }
    }

    stage('Trigger ManifestUpdate') {
        echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
    }
}
