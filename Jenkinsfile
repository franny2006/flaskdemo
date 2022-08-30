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
        junit '**/testreports/*.xml'
   }

   stage('Import results to Xray') {
        step([$class: 'XrayImportBuilder', endpointName: '/junit', fixVersion: 'v3.0', importFilePath: '**/testreports/*.xml', importToSameExecution: 'true', projectKey: 'DEP', serverInstance: '552d0cb6-6f8d-48ba-bbad-50e94f39b722'])
   }

}