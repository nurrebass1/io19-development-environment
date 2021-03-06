# A development environment by IO19
The project deploys development environments including two storage server, two developing servers and two compiler server.
The overview of the project is show below:

![Overview](https://github.com/nurrebass1/io19-development-environment/blob/master/Images/overview.PNG?raw=true)

## Prequisites
In order to deploy the development environments the below steps are required:

## Foreman Pre-Configuration

You need to config the Foreman once you setup the Foreman, if you have not configured it yet, please follow below steps:
### Create Host Groups:

1) Login to the Foreman  
2) Navigate to "Configure" &rarr; "Host groups"  
3) Create the host group below:

| Name                | Environment |
| ------------------- | ----------- |
| Compile Servers     | production  |
| Development Servers | production  |
| Storage Servers     | production  |

The result is:  

![host_group](https://github.com/nurrebass1/io19-development-environment/blob/master/Images/host_group.PNG?raw=true)

### Script runner
Navigate to root by running 

```
sudo su
cd
```
## Clone project
```
git clone https://github.com/nurrebass1/io19-development-environment.git 
```

## How to run
```
cd io19-development-environment
```
Copy your .openstack file to the directory.  

Open `projectx.mln` and modify the following:  
1) IP address of your master/Foreman server
2) The keypair name  

Now you can start the deployment using the command below:  

```
python3 deployer.py
```

When you see the ` Please config classes in Foreman ` then 
1) login to the Foreman 
2) Navigate to "Configure" &rarr; "classes"
3) Click on "Import environments ..." and update.
The result is :
![classes](https://github.com/nurrebass1/io19-development-environment/blob/master/Images/classes.PNG?raw=true)
You should assign each class to a host group. So click on each class and assign to host group/groups based on below table:  

| Class name          | Environment | Host groups                                           |
| ------------------- | ----------- | ------------------------------------------------------|
| compiler::install   | production  | Compile Servers                                       |
| devutils::install   | production  | Development Servers                                   |
| glusterfs::install  | production  | Storage Servers                                       |
| passhash::install   | production  | Compile Servers, Development Servers, Storage Servers |
| users::configure    | production  | Compile Servers, Development Servers, Storage Servers |

![classes-assign](https://github.com/nurrebass1/io19-development-environment/blob/master/Images/classes-assign.png?raw=true)

Now, please navigate to the "Administer" &rarr; "Settings", and check the `DefaultHostGroup` configuration:
![DefaultHOstGroup](https://github.com/nurrebass1/io19-development-environment/blob/master/Images/plugin_settings.PNG?raw=true)

The script is running in the background, so please wait until end of the script.

## Cleanup
To cleanup the environment run

```
python3 cleanup.py
```




