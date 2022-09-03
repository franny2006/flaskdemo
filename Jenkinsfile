node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        sh 'docker stop $(docker ps -q)'
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
        junit '**/testreports/*.xml'
   }

   stage('Import results to Xray') {
        step([$class: 'XrayImportBuilder', endpointName: '/junit', importFilePath: '**/testreports/*.xml', importToSameExecution: 'true', projectKey: 'DEP', serverInstance: '8cad2d10-c6a7-43ca-8dc5-9bdbd7ae8eec'])
   }

}