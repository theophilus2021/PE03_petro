pipeline {
      environment{
            imagename = "toroking/theophilus2021"
            registryCredential ="jenkins_docker2023"
            dockerimage = ''
      }
      agent any
      stages{
            stage('Cloning Git'){
                  steps{
                        git([url: 'https://github.com/theophilus2021/PE03_petro', branch:'main',credentialsId: 'devops'])
                  }
            }
            stage('Building image'){
                  steps{
                        script {
                              dockerImage = docker.build imagename
                        }
                  }
            }
            stage('Deploy Image'){
                  steps{
                        script{
                              docker.withRegistry('', registryCredential){
                                    dockerImage.push("$BUILD_NUMBER")
                                    dockerImage.push('latest')
                              }
                        }
                  }
            }
            stage('Remove Unused docker image'){
                  steps{
                       sh "docker rmi $imagename:$BUILD_NUMBER"
                       sh "docker rmi $imagename:latest"
                  }
            }
      }
}