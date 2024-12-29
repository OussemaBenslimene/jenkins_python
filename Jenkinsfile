pipeline {
    agent any

    stages {
        stage('Build Application') {
            steps {
                echo 'Building the application...'
                // Build without Docker
                sh 'chmod +x build-script.sh && ./build-script.sh'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Set PYTHONPATH and run tests
                sh 'export PYTHONPATH=$PYTHONPATH:$(pwd) && pytest > test-results.txt'
            }
        }

        stage('Archive Results') {
            steps {
                echo 'Archiving test results...'
                archiveArtifacts artifacts: 'test-results.txt', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed. Cleaning up...'
        }

        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
