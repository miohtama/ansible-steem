# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    # Needed in order to run screen
    # https://www.vagrantup.com/docs/vagrantfile/ssh_settings.html
    # http://stackoverflow.com/questions/27545745/start-screen-detached-in-a-vagrant-box-with-ssh-how
    config.ssh.pty = true

    config.vm.box = "trusty64"
    config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

    config.vm.network :public_network

    config.vm.provider "virtualbox" do |v|
      v.customize ["modifyvm", :id, "--memory", "2048"] # compiling native deps with GCC needs more memory
      v.customize ["modifyvm", :id, "--cpus", 2]
      # https://github.com/mitchellh/vagrant/issues/3860#issuecomment-167664778
      # v.customize ["modifyvm", :id, "--nictype1", "Am79C973"]
    end

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "playbook.yml"
        ansible.host_key_checking = false

        # ansible.verbose = "vvvv"
        ansible.extra_vars = { ansible_ssh_user: 'vagrant', ansible_connection: 'ssh', ansible_ssh_args: '-o ForwardAgent=yes'}
        ansible.raw_arguments = ENV['ANSIBLE_ARGS']

    end

end