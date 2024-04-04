pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Step to clone the repository
                git 'https://github.com/sufian020801/practice.git'
                echo 'Hello, World'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Step to install dependencies using pip
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Step to execute test.py
                sh 'python test.py'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Step to deploy based on branch name
                    def branchName = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
                    if (branchName == 'main') {
                        echo 'Deploying to production'
                        // Add deployment commands for production
                    } else {
                        echo 'Deploying to UAT'
                        // Add deployment commands for UAT
                    }
                }
            }
        }
    }
}
