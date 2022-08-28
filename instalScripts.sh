#script for installing NODE,NOM,ANGULAR,DOCKER


sudo apt-get update
sudo apt-get upgrade

echo "=================================================   INSTALLING CURL ====================================================="
	whereis curl | grep ' ' -ic
	if [ $? == 0 ]; then
        	echo "already curl Installed "
        else
                echo "curl not installed,installing agian"
		sudo apt-get install curl
        fi
echo "================================================    INSTALLING NODE ====================================================="
	whereis node | grep ' ' -ic
	if [ $? == 0 ]; then
                echo "Node Installed"
        else
                echo "Node not installed"
		curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
		sudo apt-get install -y nodejs
        fi

echo "================================================ INSTALLING ANGULAR ====================================================="
	whereis ng | grep ' ' -ic
	if [ $? == 0 ]; then
                echo "ALRAEDY ANGULAR Installed"
        else
                echo "ANGULAR not installed"
                sudo npm install -g @angular/cli
		npm uninstall @angular-devkit/build-angular
		npm install --save-dev @angular-devkit/build-angular
	fi
echo "===================================================== node,npm ,angular version ========================================="
	node --version
	npm --version
	ng v

echo "=====================================================INSTALLING DOCKER ====================================================="
	whereis ng | grep ' ' -ic
	if [ $? == 0 ]; then
                echo "ALRAEDY DOCKER Installed"
        else
                echo "DOcker not installed"
		sudo apt update
		sudo apt install apt-transport-https ca-certificates curl software-properties-common
		curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
		sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
		apt-cache policy docker-ce
		sudo apt install docker-ce
		sudo systemctl status docker
	fi
