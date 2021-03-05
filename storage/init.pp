class glusterfs::install {
    exec { "install_dep" :
    path => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    command => "sudo apt -y install software-properties-common && sudo add-apt-repository ppa:gluster/glusterfs-7 -y",
    unless => "grep glusterfs /etc/apt/sources.list.d/gluster-ubuntu-glusterfs-7-xenial.list"
    }

    exec { "install_glusterfs" :
    path => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    command => "sudo apt update && sudo apt -y install glusterfs-server",
    require => Exec["install_dep"]
    }

}
