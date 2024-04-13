node {
    checkout scm

    docker.withServer('tcp://10.22.208.108:4243') {
        docker.image('mysql:8-oracle').withRun('-p 3306:3306') {
            /* do things */
        }
    }
}
