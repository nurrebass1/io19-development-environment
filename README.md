# A development environment by IO19
The project deploys development environments including two storage server, two developing servers and two compiler server.
The overview of the project is:

![Overview](https://github.com/nurrebass1/io19-development-environment/blob/master/Images/overview.PNG?raw=true)

## Prequisites
In order to deploy the development environments the below steps are required:

## Foreman Pre-Configuration
### Create Host Groups:

Login to the Foreman
Navigate to "Configure" --> "Host groups"
Create below host group:

| Name                | Environment |
| ------------------- | ----------- |
| Compile Servers     | production  |
| Development Servers | production  |
| Storage Servers     | production  |


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

Open `projectx.mln` and modify IP address of your master/Foreman server and keypair name.

Now you can start deployment using below command:

```
python3 deployer.py
```

When you see the ` Please config classes in Foreman ` then login to the Foreman, and navigate to "Configure" --> "classes", click on "Import environments ..." and update.

The script is running in the background, so please wait until end of the script.

## Cleanup
To cleanup the environment run

```
python3 cleanup.py
```




