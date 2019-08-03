Vagrant.configure("2") do |config|
  config.vm.define "master" do |subconfig|
    subconfig.vm.box = "centos/7"
    subconfig.vm.hostname = "master"
    subconfig.vm.network "private_network", ip: "192.168.33.10"
  end

  config.vm.define "slave1" do |subconfig|
    subconfig.vm.box = "centos/7"
    subconfig.vm.hostname = "slave1"
    subconfig.vm.network "private_network", ip: "192.168.33.11"
  end

  config.vm.define "slave2" do |subconfig|
    subconfig.vm.box = "centos/7"
    subconfig.vm.hostname = "slave2"
    subconfig.vm.network "private_network", ip: "192.168.33.12"
  end

  config.vm.provision "file", source: "./preconfig_keys/hadoop_rsa.pub", destination: "~/.ssh/id_rsa.pub"
  config.vm.provision "file", source: "./preconfig_keys/config", destination: "~/.ssh/config"
  config.vm.provision "file", source: "./preconfig_keys/hadoop_rsa", destination: "~/.ssh/id_rsa"
  config.vm.provision "shell", inline: "cat ~vagrant/.ssh/id_rsa.pub >> ~vagrant/.ssh/authorized_keys"
end
