node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        sh 'docker-compose build'
        sh 'cd /var/lib/jenkins/workspace/Flaskdemo/app'
        dir('${env.WORKSPACE}/Flaskdemo/app'){
            echo "Workdir=$WORKSPACE"
            sh 'behave'
        }

    }

    stage('Start Containers') {
        sh 'docker-compose up -d'
    }

}