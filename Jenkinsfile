node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        sh 'docker-compose build'
        echo "PATH=$PATH"
        sh 'cd app/features'
        echo "PATH=$PATH"
        echo "Workdir=$WORKDIR"
        sh 'behave'
    }

    stage('Start Containers') {
        sh 'docker-compose up -d'
    }

}