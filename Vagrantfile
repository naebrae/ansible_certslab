# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.define :crtsrv01 do |crtsrv01_config|
    crtsrv01_config.vm.box = "almalinux/8"
    crtsrv01_config.vm.network "private_network", ip: "172.16.1.201"

    crtsrv01_config.vm.provider "virtualbox" do |crtsrv01_vb|
      crtsrv01_vb.name = "crtsrv01"
    end
  end

  config.vm.define :crtcli01 do |crtcli01_config|
    crtcli01_config.vm.box = "almalinux/8"
    crtcli01_config.vm.network "private_network", ip: "172.16.1.101"

    crtcli01_config.vm.provider "virtualbox" do |crtcli01_vb|
      crtcli01_vb.name = "crtcli01"
    end
  end

  config.vm.provision "shell", inline: <<-SHELL
    ln -f -s /usr/share/zoneinfo/Australia/Perth /etc/localtime
    echo "172.16.1.201	crtsrv.lab.home crtsrv crt1.lab.home crt2.lab.home www.lab.home tomcat.lab.home ftp.lab.home ldap.lab.home smtp.lab.home imap.lab.home pop.lab.home postgresql.lab.home" >> /etc/hosts
    echo "172.16.1.101	crtcli.lab.home crtcli" >> /etc/hosts
  SHELL
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.groups = {
       "crtsrv" => ["crtsrv01"],
       "crtcli" => ["crtcli01"]
    }
  end
  config.vm.synced_folder ".", "/home/vagrant/sync", type: "rsync", disabled: true
  config.vm.synced_folder ".", "/vagrant", disabled: true
end
