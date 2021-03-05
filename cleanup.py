import subprocess
import time
cert_list=["comipler1","comipler2","development1","development2","storage1","storage2"]

def cleanup():
    print('------------- DELETING MANIFESTS ------------')
    subprocess.run('rm -rf /etc/puppetlabs/code/environments/production/manifests/', shell=True)
    print('------------- REMOVING CERTIFICATES ---------')

    for i in cert_list:
        subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean '+ i, shell=True)
        time.sleep(5)

    print('<---------- DELETING INSTANCES ------->')
    subprocess.run('nova delete storage1.projectx', shell=True)
    time.sleep(5)
    subprocess.run('nova delete storage2.projectx', shell=True)
    time.sleep(5)
    subprocess.run('nova delete compiler1.projectx', shell=True)
    time.sleep(5)
    subprocess.run('nova delete compiler2.projectx', shell=True)
    time.sleep(5)
    subprocess.run('nova delete development1.projectx', shell=True)
    time.sleep(5)
    subprocess.run('nova delete development2.projectx', shell=True)
    
    print('-------------- DONE ------------')


cleanup()

