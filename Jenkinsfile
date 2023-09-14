node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        try {
            sh 'docker-compose down -v'
            // sh 'docker rm $(docker ps -a -q)'
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
            sh 'behave ./features/demo.feature --tags komponentenintegrationstest --junit --junit-directory /var/lib/jenkins/workspace/Flaskdemo/app/testreports'
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
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
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
    }


   stage('Transfer Testresults to Zephyr') {
        junit '**/testreports/*.xml'
        sh 'zip -D /var/lib/jenkins/workspace/Flaskdemo/app/testreports/junit_tests.zip /var/lib/jenkins/workspace/Flaskdemo/app/testreports/TEST*.xml'
        sh 'curl -o -X POST -F "file=@/var/lib/jenkins/workspace/Flaskdemo/app/testreports/junit_tests.zip" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb250ZXh0Ijp7ImJhc2VVcmwiOiJodHRwczovL3Rlc3RtYW51ZmFrdHVyLmF0bGFzc2lhbi5uZXQiLCJ1c2VyIjp7ImFjY291bnRJZCI6IjVhZGIwNTAxZWVlODdmMmUzMTUxMTU3MSJ9fSwiaXNzIjoiY29tLmthbm9haC50ZXN0LW1hbmFnZXIiLCJzdWIiOiIwZTU0ZTg0ZS0yOTRlLTM2NDItYmMzMC0wY2JkN2Y1ZmJjYzEiLCJleHAiOjE3MjYyMjE1MTUsImlhdCI6MTY5NDY4NTUxNX0.i-Pv3fXtrnE1nFy_kARZu8OgccCPLyF8SbtzqQHUvVM" "https://api.zephyrscale.smartbear.com/v2/automations/executions/junit?projectKey=DA&autoCreateTestCases=true"'
    }

}