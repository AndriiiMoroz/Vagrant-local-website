Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.provision "shell", run: "always", path:"provision.sh"
  config.vm.network "forwarded_port", guest: 80, host: 8080
end