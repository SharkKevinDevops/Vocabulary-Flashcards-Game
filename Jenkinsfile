pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Source') {
            steps {
                git url: 'https://github.com/ten-ban/my-python-game.git', branch: 'main'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv $VENV_DIR
                . $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt || pip install pygame
                '''
            }
        }

        stage('Test Optional') {
            steps {
                echo 'This is test tage'
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
                . venv/bin/activate
                python main.py
                '''
            }
    }

    post {
        always {
            echo 'CI/CD job completed'
        }
    }
}
