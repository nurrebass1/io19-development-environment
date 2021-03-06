import subprocess
import time

cert_list = ['comipler1', 'comipler2', 'development1', 'development2', 'storage1', 'storage2']
target_servers = ["storage-1.projectx", "storage-2.projectx", "development-1.projectx", "development-2.projectx",
                  "compiler-1.projectx", "compiler-2.projectx"]


def cleanup():
    print('------------- DELETING MANIFESTS ------------')
    subprocess.run('rm -rf /etc/puppetlabs/code/environments/production/manifests/', shell=True)
    print('------------- REMOVING CERTIFICATES ---------')

    for i in cert_list:
        subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean ' + i, shell=True)
        time.sleep(5)

    print('<---------- DELETING INSTANCES ------->')

    for server in target_servers:
        subprocess.run('nova delete' + server, shell=True)
        time.sleep(5)

    print('-------------- DONE ------------')


cleanup()
