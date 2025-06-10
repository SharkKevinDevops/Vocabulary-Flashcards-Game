pipeline {
    agent any

    stages {
        stage('Clone Source') {
            steps {
                git 'https://github.com/SharkKevinDevops/Vocabulary-Flashcards-Game.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt || pip install pygame
                '''
            }
        }

        stage('Build or Package') {
            steps {
                echo 'This is build package stage (test).'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy to server or container if needed'
                sh '''
                . venv/bin/activate
                python main.py
                '''
            }
        }
    }

    post {
        always {
            echo 'CI/CD job completed'
        }
    }
}
