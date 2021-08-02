ode{
    stage('Build'){
        checkout([$class: 'GitSCM',
            branches: [[name: "Dockerise"]],
            userRemoteConfigs: [[
                url: 'https://github.com/rtxverma123/multibranch-try.git']]
        ])
        def mycustomImage = docker.build("rtxverma123mymultiflask:my-latest")


    }
}

      
