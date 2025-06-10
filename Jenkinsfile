pipeline {
    agent any

    stages {
        stage('Clone Source') {
            steps {
                git url: 'https://github.com/SharkKevinDevops/Vocabulary-Flashcards-Game.git', branch: 'main'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                [ -f requirements.txt ] && pip install -r requirements.txt || echo "No requirements.txt"
                pip install pygame
                '''
            }
        }

        stage('Test Game Headless') {
            steps {
                sh '''
                . venv/bin/activate
                sudo apt update && sudo apt install -y xvfb
                xvfb-run -a python main.py
                '''
            }
        }
    }
}
