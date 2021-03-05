import subprocess


def cleanup():
    print('------------- DELETING MANIFESTS ------------')
    subprocess.run('rm -rf /etc/puppetlabs/code/environments/production/manifests/', shell=True)
    print('------------- REMOVING CERTIFICATES ---------')
    # TODO: fix cert name
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean XXXXX', shell=True)
    print('<---------- DELETING INSTANCES ------->')
    subprocess.run('nova delete storage1.projectx', shell=True)
    subprocess.run('nova delete storage2.projectx', shell=True)
    subprocess.run('nova delete compiler1.projectx', shell=True)
    subprocess.run('nova delete compiler2.projectx', shell=True)
    subprocess.run('nova delete development1.projectx', shell=True)
    subprocess.run('nova delete development2.projectx', shell=True)
    subprocess.run('nova delete host1.agent', shell=True)
    print('-------------- DONE ------------')


cleanup()

