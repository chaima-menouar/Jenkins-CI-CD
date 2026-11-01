pipeline {
    agent any
    options { skipDefaultCheckout(true) }
    environment {
        VENV_DIR = '.venv'
        HOST = '0.0.0.0'
        PORT = '5000'
        APP_MODULE = 'app:app'
    }
    triggers {
        cron('H/5 * * * *')
        githubPush()
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/chaima-menouar/Jenkins-CI-CD.git'
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv "$VENV_DIR"
                    "$VENV_DIR/bin/python" -m pip install -r requirements.txt
                    "$VENV_DIR/bin/python" -m pip install pytest-cov
                '''
            }
        }
        stage('Run Tests') {
            when {
                not { changeset pattern: 'README.md', comparator: 'EQUALS' }
            }
            parallel {
                stage('Test File 1') {
                    steps {
                        sh '"$VENV_DIR/bin/python" -m pytest test_app.py -v --junitxml=report-1.xml --cov=app --cov-report=xml:coverage-1.xml'
                    }
                    post { always { junit allowEmptyResults: true, testResults: 'report-1.xml' } }
                }
                stage('Test File 2') {
                    steps {
                        sh '"$VENV_DIR/bin/python" -m pytest test_app_2.py -v --junitxml=report-2.xml --cov=app --cov-report=xml:coverage-2.xml'
                    }
                    post { always { junit allowEmptyResults: true, testResults: 'report-2.xml' } }
                }
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    if [ -f gunicorn.pid ]; then
                        kill "$(cat gunicorn.pid)" 2>/dev/null || true
                        rm -f gunicorn.pid
                    fi
                    nohup "$VENV_DIR/bin/gunicorn" --bind "$HOST:$PORT" "$APP_MODULE" --pid gunicorn.pid > gunicorn.log 2>&1 < /dev/null &
                    sleep 2
                    curl --fail --silent http://127.0.0.1:"$PORT"/ > /dev/null
                '''
            }
        }
    }
}
