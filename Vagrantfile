# -*- mode: ruby -*-
Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 80, host: 8080

  config.vm.synced_folder "geonode", "/var/www/geonode"
  config.vm.synced_folder "my_geonode", "/var/www/my_geonode"


  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1300"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yaml"
    ansible.verbose = 'extra'
  end

end
