import subprocess
import time

cert_list = ['compiler1', 'compiler2', 'development1', 'development2', 'storage1', 'storage2']


def cleanup():
    print('<---------- REMOVE CRONTAB RULE ------->')
    subprocess.run('echo "" >> mycron', shell=True)
    subprocess.run('crontab mycron', shell=True)
    
    print('------------- REMOVING CERTIFICATES ---------')

    for i in cert_list:
        subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean ' + i, shell=True)
        time.sleep(5)

    print('<---------- DELETING INSTANCES ------->')

    for server in cert_list:
        subprocess.run('nova delete ' + server + '.projectx', shell=True)
        time.sleep(5)
    

    print('-------------- DONE ------------')


cleanup()
