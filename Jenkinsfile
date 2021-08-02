node {
  stage('Dockerise and Push'){
    checkout([$class: 'GitSCM',
         branches: [[name: "Dockerise"]],
              serRemoteConfigs: [[
                url: 'https://github.com/rtxverma123/multibranch-try.git']]
        ])
    docker.withRegistry('https://registry.hub.docker.com','Docker'){
      def myImage = docker.build("rtxverma123/multibranchflask")
      myImage.push()
    
    
  }
}
//   stage('Push Docker'){
//     checkout scm
//     docker.withRegistry('https://registry.hub.docker.com','Docker'){
      
