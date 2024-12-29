pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'  // Directory for the virtual environment
    }

    stages {
        stage('Set up Virtual Environment') {
            steps {
                echo 'Setting up virtual environment...'
                // Create virtual environment
                sh 'python3 -m venv ${VENV_DIR}'
                // Activate virtual environment and install dependencies using bash and .
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building the application...'
                // Build inside virtual environment
                sh '''
                    . ${VENV_DIR}/bin/activate
                    chmod +x build-script.sh
                    ./build-script.sh
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Set PYTHONPATH and run tests inside virtual environment
                sh '''
                    . ${VENV_DIR}/bin/activate
                    export PYTHONPATH=$PYTHONPATH:$(pwd)
                    pytest > test-results.txt
                '''
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
            // Clean up virtual environment
            sh 'rm -rf ${VENV_DIR}'
        }

        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
