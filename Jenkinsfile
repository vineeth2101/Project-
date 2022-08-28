node(label:'jenson-1') {
    
    stage('install') {
       sh "instalScripts.sh"
    }
    stage("Test") {
       sh "deploy.sh"
    }
}
