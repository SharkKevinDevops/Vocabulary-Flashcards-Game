pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Source') {
            steps {
                git url: 'https://github.com/SharkKevinDevops/Vocabulary-Flashcards-Game.git', branch: 'main'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv $VENV_DIR
                . $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install pygame
                '''
            }
        }

        stage('Build or Package') {
            steps {
                echo 'This is build package tage (test).'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy to server or container if needed'
              sh '''
              python3 main.py
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
