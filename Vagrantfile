# -*- mode: ruby -*-
Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"
  # config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.network :private_network, ip: "192.168.1.206"


  config.vm.synced_folder "geonode", "/var/www/geonode", owner: "www-data", group: "www-data"
  config.vm.synced_folder "my_geonode", "/var/www/my_geonode", owner: "www-data", group: "www-data"


  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1300"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yaml"
#    ansible.verbose = 'extra'
  end

end
