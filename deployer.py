import subprocess
import re
import time
import os

rebuild_list = []
error = 1


def handle_error():
    global error
    global rebuild_list
    while error:
        failed = os.popen('nova list | grep "ERROR"')
        error_list = failed.read()
        error_array = re.findall(" [a-zA-Z0-9]*.projectx", error_list)

        if error_array:
            for i in error_array:
                rebuild_list.append((i.replace(" ", "")).replace(".projectx", ""))
        else:
            error = 0
            rebuild_list = []

        for i in rebuild_list:
            subprocess.run('nova delete ' + i + '.projectx', shell=True)
            time.sleep(10)
            subprocess.run('mln start -p projectx -h ' + i, shell=True)
            time.sleep(20)
        rebuild_list = []
        


def deploy():
    folders = ['common', 'compiler', 'development', 'storage']

    # Config Foreman
    print('------------- Foreman setting up ------------')
    subprocess.run('foreman-installer --enable-foreman-plugin-discovery', shell=True)
    subprocess.run('apt-get install ruby-foreman-default-hostgroup', shell=True)
    subprocess.run('mkdir -p /etc/foreman/config/settings.plugins.d/', shell=True)
    subprocess.run('cp plugin-config/* /etc/foreman/config/settings.plugins.d/', shell=True)
    subprocess.run('cp plugin-config/* /etc/foreman/plugins/', shell=True)

    for folder in folders:
        subprocess.run('cp -r ' + folder + '/' + ' /etc/puppetlabs/code/environments/production/manifests/', shell=True)

    subprocess.run('service foreman restart', shell=True)

    print('------------- Please log out and log in from Foreman ------------')    
    print('------------- Please config classes in Foreman ------------')
    time.sleep(20)
    print('40 seconds left')
    time.sleep(20)
    print('20 seconds left')
    time.sleep(20)

    print('------------- Start Deployment ------------')
    # Build mln project
    subprocess.run('mln build -f projectx.mln -r', shell=True)
    time.sleep(30)

    # Start deployment infra with MLN
    subprocess.run('mln start -p projectx', shell=True)
    time.sleep(30)

    handle_error()
    print('------------- All errors resolved ------------')

    print('------------- Start Crontab Configuration ------------')
    subprocess.run('crontab -l > mycron', shell=True)
    subprocess.run('echo "*/2 * * * * /opt/puppetlabs/puppet/bin/puppet cert sign --all" >> mycron', shell=True)
    subprocess.run('crontab mycron', shell=True)
    subprocess.run('service cron restart', shell=True)
    print('------------- Deployment completed ------------')


deploy()
