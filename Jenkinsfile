pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/sufian020801/practice'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Execute Tests') {
            steps {
                sh 'python test.py'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def branchName = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
                    if (branchName == 'main') {
                        echo 'Deploying to production'
                        // Add your deployment steps for production
                    } else {
                        echo 'Deploying to UAT'
                        // Add your deployment steps for UAT
                    }
                }
            }
        }
    }
}
