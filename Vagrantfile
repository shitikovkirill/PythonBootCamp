Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.synced_folder ".", "/home/vagrant/project"

  config.vm.provision "shell", inline: <<-SHELL

     echo "Update system"
     apt-get -y -q update
     apt-get -y -q upgrade

     echo "Install pip"
     apt-get install -y python-pip python-dev build-essential
     pip install --upgrade pip
     pip install --upgrade virtualenv

     echo "Install Java"
     apt-get -y -q install software-properties-common htop
     add-apt-repository ppa:webupd8team/java
     apt-get -y -q update
     echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
     apt-get -y -q install oracle-java8-installer
     update-java-alternatives -s java-8-oracle
SHELL
end
