node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        try {
            sh 'docker-compose down -v'
            }
        catch (Exception e) {
            echo 'Container stoppen nicht möglich:  ' + e.toString()
            }
        sh 'docker-compose build'

        sh 'cd /var/lib/jenkins/workspace/Flaskdemo/app'
        dir('app'){
            echo "Workdir=$WORKSPACE"
            sh 'ls -l'
            dir ('testreports') {
                writeFile file:'dummy', text:''
            }
            sh 'ls -l'
            sh 'behave ./features/demo.feature --junit --junit-directory /var/lib/jenkins/workspace/Flaskdemo/app/testreports'
            // sh 'behave ./features/demo.feature --junit --junit-directory /var/lib/jenkins/workspace/Flaskdemo/app/testreports'
        }
    }

    stage('Start Containers') {
        sh 'docker-compose up -d --remove-orphans'
      //  sh 'docker exec -i flaskdemo_db_1 mysql -h db -uroot -p"root" < /var/lib/jenkins/workspace/Flaskdemo/db/init.sql'
    }

    stage('Create Network Connectivity') {
        sh 'docker network prune'
        sh 'docker network connect demoNetz da_gui'
        sh 'docker network connect demoNetz da_persistierung'
        sh 'docker network connect demoNetz da_mysql'
      //  sh 'docker exec -i flaskdemo_db_1 mysql -h db -uroot -p"root" < /var/lib/jenkins/workspace/Flaskdemo/db/init.sql'
    }

    stage('Integration Test') {
        sh 'cd /var/lib/jenkins/workspace/Flaskdemo/app'
        dir('app'){
            echo "Workdir=$WORKSPACE"
            sh 'ls -l'
            dir ('testreports') {
                writeFile file:'dummy', text:''
            }
            sh 'ls -l'
            sh 'behave --tags=integration --junit --junit-directory /var/lib/jenkins/workspace/Flaskdemo/app/testreports'
            // sh 'behave ./features/demo.feature --junit --junit-directory /var/lib/jenkins/workspace/Flaskdemo/app/testreports'
        }
    }


   stage('Import results to Xray') {
        junit '**/testreports/*.xml'
        step([$class: 'XrayImportBuilder', endpointName: '/junit', importFilePath: '**/testreports/*.xml', importToSameExecution: 'true', projectKey: 'DEP', serverInstance: '8cad2d10-c6a7-43ca-8dc5-9bdbd7ae8eec'])
   }

}