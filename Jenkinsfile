pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        CI = 'true'
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

        stage('Test Optional') {
            steps {
                echo 'This is test stage'
            }
        }    

        stage('Build or Package') {
            steps {
                echo 'If needed, you can package the game here.'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy to server or container if needed'
                sh '''
                . $VENV_DIR/bin/activate
                python main.py
                ^c
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
