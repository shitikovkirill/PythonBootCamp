Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.define "shitikovkirill"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.provider "virtualbox" do |vb|
        vb.name = "github shitikovkirill"
  end

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
        echo -e "\e[34mSet PROJECT"
        echo "export PROJECT_DIR=/home/vagrant/project" >> ~/.profile
        echo "export WIRTUALENV_NAME=PythonBootCamp" >> ~/.profile
  SHELL
  config.vm.provision "shell", path: "bootstrap/common.sh"
  config.vm.provision "shell", path: "bootstrap/java.sh"
  config.vm.provision "shell", path: "bootstrap/python.sh"
  config.vm.provision "shell", privileged: false, path: "bootstrap/virtualenvwrapper.sh"
  config.vm.provision "shell",
        privileged: false,
        path: "bootstrap/run.sh",
        run: "always"
end
