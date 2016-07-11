# Ansible install script for Steem

This is an Ansible playbook that sets up steemd on Ubuntu 14.04 for mining, witness or seeding. An automated playbook saves you a lot of time of manual package building and configuration process.

## Features

* Compatible with any server provider: Amazon, Linode, Digital Ocean, Azure

* Creates processor optimal steemd mining configuration and makes steemd to start on the server reboot

* Starts steemd under screen so you can connect to the session easily to diagnose possible problems

* Generates initial private key with brain key configuration file for mining

### Prerequisites

* Get a server with SSH access

* Make sure you have port 2001 open for incoming TCP/IP connections

* Have Python 2.7 and virtualenv command installed on a local computer in order to run Ansible. [Windows download link](https://www.python.org/download/releases/2.7/). For Linux use your distribution provided Python 2.7 package. For OSX you have Python 2.7 installed out of the box.

* You need to set up [SSH to allow passwordless connection to you server](https://opensourcehacker.com/2012/10/24/ssh-key-and-passwordless-login-basics-for-developers/).

Example for Amazon:

    ssh-add key-file-given-by-amazon.pem

## Installation

Clone yourself a local copy of this repository from Github:

    git clone git@github.com:miohtama/ansible-steem.git

.. or if you do not have Git use [direct download link](https://github.com/miohtama/ansible-steem/archive/master.zip).

## Usage

These instructions walk you through to set up *steemd* in mining mode. For witness or seed node see more instructions below.

Create and activate Python 2.7 venv:

    virtualenv -p python2.7 venv
    source venv/bin/activate

Install Ansible in this virtual environment:

    pip install ansible

Edit `playbook.yml` and add your steem account name:

    # My account name on steemit.com - CHANGE THIS
    steem_account: moo9000

Create a `hosts.ini` file that points to your server(s). In this example we use Amazon EC2 server with ubuntu user having sudo access. `hosts.ini`:

    [default]
    steem ansible_host=78.47.53.101 ansible_user=ubuntu

Here

* **ansible_host** is your server IP address

* **ansible_user** is a UNIX user with sudo access rights

Run Ansible:

    ansible-playbook -i hosts.ini

This will take 30-60 minutes depending on the server.

The miner should be up and running. To confirm this do:

    ssh YOUR SERVER IP ADDRESS
    screen -x

You should see steemd miner pushing out a lot of status text like:

    86718ms th_a       witness.cpp:425               on_applied_block     ] hash rate: 1 hps  target: 29 queue: 102 estimated time to produce: 8947848 minutes
    86719ms th_a       witness.cpp:425               on_applied_block     ] hash rate: 1 hps  target: 29 queue: 102 estimated time to produce: 8947848 minutes

Now detach from the screen using `CTRL + A` and then D`.

Before leaving the server get a backup copy of your private key:

    cat brainkey.json

Print this and store it in a safe location.

# Restart

The following will restart both screen and steemd:

    sudo /home/ubuntu/steem/programs/steemd/restart-miner.bash

# Testing playbook locally using Vagrant

Spin up a virtual machine using Vagrant and playbook locally:

    vagrant up

See its running:

    vagrant ssh
    screen -x

## Moving mined Steem around

TODO

## Further info

* https://steemit.com/steemhelp/@joseph/mining-steem-for-dummies

* https://steemit.com/steemhelp/@steemed/become-a-steem-witness-essentials
