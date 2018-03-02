# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "private_network", ip: "10.10.10.13"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  #config.vm.provision :shell, :path => "data/bootstrap.sh"
end