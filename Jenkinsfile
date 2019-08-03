pipeline {
  environment {
  BRANCH='*/master'
  GIT_URL='https://github.com/kristaum/K8S-SecretsCI.git'
  AKS_RG=get_RG()
  AKS_CLUSTER=get_CLUSTER()
  K8S_YAML='secret-default.yaml'
  }
  agent any
  stages {
    stage('Checkout: Code') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: env.BRANCH]], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'github_conn', url: env.GIT_URL]]])
      }
    }
    stage('Create yaml for each config') {
      steps {
          sh "/usr/bin/python create_yaml.py $AMBIENTE"
      }
    }
    stage('Deploy Secrets-config AKS') {
      steps {
        withCredentials([azureServicePrincipal('azure_sp_devops')]) {
          sh "az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET -t $AZURE_TENANT_ID"
        }
        sh "az aks get-credentials --resource-group $AKS_RG --name $AKS_CLUSTER"
        sh '''
          for file in `ls $WORKSPACE | grep yml`
          do
            /usr/local/bin/kubectl apply -f `echo $WORKSPACE/$file`
          done
        '''
      }
    }
  }
  post {
    always {
      cleanWs()
    }
  }
}

def get_RG() {
    if (env.AMBIENTE == "QA"){
      return "KUBERNETES_QA"
    } else if (env.AMBIENTE == "Prod"){
      return "KUBERNETES_PROD"
    }
}

def get_CLUSTER() {
    if (env.AMBIENTE == "QA"){
      return "AKS-QA"
    } else if (env.AMBIENTE == "Prod"){
      return "AKS-PROD"
    }
}
