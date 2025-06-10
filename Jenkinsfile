pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Clone Source') {
            steps {
                git url: 'https://github.com/SharkKevinDevops/Vocabulary-Flashcards-Game.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    sudo apt-get update -y
                    sudo apt-get install -y xvfb
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Game with xvfb') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    xvfb-run -a python main.py
                '''
            }
        }
    }
}
