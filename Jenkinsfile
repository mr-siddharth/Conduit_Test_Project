pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'No Build Step Required'
      }
    }

    stage('Tests') {
      parallel {
        stage('SignIn Tests') {
          agent {
            node {
              label 'master'
            }

          }
          steps {
            bat 'pytest -vs testCases/test_signin.py'
          }
        }

        stage('Create New Article Tests') {
          agent {
            node {
              label 'windows_node'
            }

          }
          steps {
            bat 'pytest -vs testCases/test_create_new_article.py'
          }
        }

      }
    }

    stage('Deploy to Staging') {
      steps {
        echo 'Deploy to Staging'
      }
    }

    stage('Deploy to Production') {
      steps {
        input 'Deploy to Production?'
      }
    }

  }
  post {
    always {
      echo 'One way or another, I have finished'
    }

    success {
      echo 'I succeeded!'
    }

    unstable {
      echo 'I am unstable :/'
    }

    failure {
      echo 'I failed :('
      mail(to: 'siddharth2k007@gmail.com', subject: "Failed Pipeline ${currentBuild.fullDisplayName}", body: " For details about the failure, see ${env.BUILD_URL}")
    }

    changed {
      echo 'Things were different before...'
    }

  }
}