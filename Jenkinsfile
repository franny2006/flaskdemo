node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        sh 'docker-compose build'
        sh 'cd /var/lib/jenkins/workspace/Flaskdemo/app'
        dir('app'){
            echo "Workdir=$WORKSPACE"
            sh 'ls -l'
            dir ('testreports') {
                writeFile file:'dummy', text:''
            }
            sh 'ls -l'
            sh 'behave  --junit --junit-directory /var/lib/jenkins/workspace/Flaskdemo/app/testreports'
        }

    }

    stage('Start Containers') {
        sh 'docker-compose up -d'
    }

    stage('Reporting') {
        junit '**/reports/junit/*.xml'
   }

}