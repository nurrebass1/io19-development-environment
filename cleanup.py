import subprocess


def cleanup():
    print('------------- DELETING MANIFESTS ------------')
    
    subprocess.run('rm -rf /etc/puppetlabs/code/environments/production/manifests/', shell=True)
    print('------------- REMOVING CERTIFICATES ---------')
    
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean agent1.projectx', shell=True)   
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean development1.projectx', shell=True)
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean development21.projectx', shell=True)
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean storage1.projectx', shell=True)
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean storage2.projectx', shell=True)
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean compiler1.projectx', shell=True)
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean compiler2.projectx', shell=True)
    print('<---------- DELETING INSTANCES ------->')
    
    subprocess.run('nova delete storage1.projectx', shell=True)
    subprocess.run('nova delete storage2.projectx', shell=True)
    subprocess.run('nova delete compiler1.projectx', shell=True)
    subprocess.run('nova delete compiler2.projectx', shell=True)
    subprocess.run('nova delete development1.projectx', shell=True)
    subprocess.run('nova delete development2.projectx', shell=True)
    subprocess.run('nova delete host1.agent', shell=True)
    
    #TODO: remove from Foreman
    print('-------------- DONE ------------')


cleanup()

