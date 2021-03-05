import subprocess
import re
import time
import os

rebuild_list=[]
error=1

# List of target servers to deploy
#target_servers=["storage-1.projectx","storage-2.projectx","development-1.projectx","development-2.projectx","compiler-1.projectx","compiler-2.projectx"]


# Config Foreman
print('------------- Foreman setting up ------------')
subprocess.run('apt-get install ruby-foreman-default-hostgroup', shell=True)
subprocess.run('mkdir /etc/foreman/config/settings.plugins.d/', shell=True)
subprocess.run('cp default_hostgroup.yaml /etc/foreman/config/settings.plugins.d/', shell=True)
subprocess.run('cp default_hostgroup.yaml /etc/foreman/plugins/', shell=True)
subprocess.run('cp -r common /etc/puppetlabs/code/environments/production/manifests/', shell=True)
subprocess.run('cp -r compiler /etc/puppetlabs/code/environments/production/manifests/', shell=True)
subprocess.run('cp -r development /etc/puppetlabs/code/environments/production/manifests/', shell=True)
subprocess.run('cp -r storage /etc/puppetlabs/code/environments/production/manifests/', shell=True)
subprocess.run('service foreman restart', shell=True)

print('------------- Please config classes in Foreman ------------')
time.sleep(120)

print('------------- Start Deployment ------------')
# Build mln project
subprocess.run('mln build -f projectx.mln -r', shell=True)
time.sleep(5)

# Start deployment infra with MLN
subprocess.run('mln start -p projectx', shell=True)
time.sleep(30)

# Check the error in deployment ----> need to be a function
while error:
    failed=os.popen('nova list | grep "ERROR"')
    error_list=failed.read()
    error_array=re.findall(" [a-zA-Z0-9]*.projectx",error_list)

    if error_array:
        for i in error_array:
            rebuild_list.append((i.replace(" ","")).replace(".projectx",""))
    else:
        error=0
        rebuild_list=[]

    for i in rebuild_list:
        subprocess.run('nova delete ' + i+ '.projectx', shell=True)
        time.sleep(10)
        subprocess.run('mln start -p projectx -h ' + i, shell=True)
        time.sleep(40)
    rebuild_list=[]

print('------------- Start Crontab Configuration ------------')
#set crontab
subprocess.run('crontab -l > mycron', shell=True)
subprocess.run('echo "*/2 * * * * /opt/puppetlabs/puppet/bin/puppet cert sign --all" >> mycron', shell=True)
subprocess.run('crontab mycron', shell=True)
subprocess.run('service cron restart', shell=True)

