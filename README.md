# Deployment of IRIS Flask Web App using Putty and WinSCP on AWS EC2 Instance

1. Download [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) and [WinSCP](https://winscp.net/eng/download.php).
2. Create an Ubuntu EC2 instance using [AWS console](https://aws.amazon.com/console/).
3. Allow `All traffic` from `Anywhere`  in security groups of EC2 Instance. 
4. Create a Key pair in .pem or .ppk format and download it.
5. Now select the created instance and click on `connect`.
6. Navigate to SSH client and copy the `public DNS`.
7. Open WinSCP and paste the copied `public DNS` in `Host name` .
8. Now, Navigate to `EC2 Instance Connect` and copy the `username` and paste it in `username` in WinSCP.
9. For `Password` in WinSCP click on `Advanced` --> navigate to SSH --> Authentication, then in `private key file` input box browse for .pem or .ppk file that we earlier downloaded.
10.  If file is in .pem format than it will get automatically converted to .ppk and click `Yes` if it ask for permissions.
11. click on Login` and click on `Yes` to do the authentication and for connecting to Host EC2 machine on AWS.
`![WinSCP authentication](https://github.com/Gourav052003/Iris-WebApp-Deployement-on-AWS/assets/81559597/c1b161e7-bfc4-431b-8313-f006fe9bc303)
12. Drop the files from your local machine to Host EC2 ubuntu machine by drag and drop or by right click in file --> upload button.
![Opening Putty seesion in WinSCP](https://github.com/Gourav052003/Iris-WebApp-Deployement-on-AWS/assets/81559597/953ca08e-032c-42b4-a809-dc9804a1a987)
13. A Putty terminal will get opened.
![Putty terminal](https://github.com/Gourav052003/Iris-WebApp-Deployement-on-AWS/assets/81559597/4f0e33cd-ac65-4b5e-8658-f78b43940bff)
14. Install Python EC2 using Putty
```
sudo apt install python3
```

15. Update all packages and install pip python package manager.
```
sudo apt-get update && sudo apt-get install python3-pip 
```

16. Install all requirements for the Flask app to run using:
```
pip3 install -r requirements.txt
```

17. Run python app using:
```
python app.py
```

18. Paste the `public DNS` that we have copied into browser with port:8080 and see your app runing on EC2.

19. Use below command to run your app even after closing Putty terminal.
```
screen -R deploy python3 app.py
```
20. To close the running app repeate above step again and ctrl+c to close session which created using above command.


# Deploy Flask App using GitHub Actions, CI/CD piplelines, ECR, Dcoker and EC2 on AWS

1. Login to [AWS console](https://aws.amazon.com/console/)

### Create IAM user with policies
2. Create IAM user for deployment --> attach following policies
```
AmazonEC2ContainerRegistryFullAccess
AmazonEC2FullAccess
```
3. Navigate to `Security Credentials` for this IAM user --> `Access keys` --> `Create Access Keys`
4. Create Access Keys using `CLI` option --> Download your access keys in .csv file.

### Create a ECR repository to store Docker Image
5. Create ECR repository in AWS by searching for ECR --> `Get started`
6. Keep the ECR repository private.
7. Provide a name to ECR repository.
8. Copy the ECR repository URI.

```
URI : 566373416292.dkr.ecr.us-east-1.amazonaws.com/myapp
```

### Create a EC2 instance on AWS
9. Create a ubuntu EC2 virtual machine on AWS.
10. Do configuration as per your requirements.
11. Create a Key-pair for your EC2 instance and download it.
12. In `Network Settings` check the following:

```
Allow SSH traffic from the 0.0.0.0/0 (Anywhere)
Allow HTTPS traffic from the Internet
Allow HTTP traffic from the Internet
```

13. Click on `Launch Instance` to create a new instance of EC2.
14. Click on `Instance ID` for this EC2 instance --> `Connect`
15. Navigate to `EC2 Instance connect` --> `Connect` then a terminal of EC2 ubuntu machine will get opened in browser.

### Running Commands on EC2 ubuntu instance terminal
16. Update and upgrade the packages using commands on terminal
```
sudo apt-get update -y
sudo apt-get upgrade
```

17. Download docker using:
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

18. Add the user "ubuntu" to the "docker" group 
```
sudo usermod -aG docker ubuntu
```

19. switching your primary group to the "docker" group
```
newgrp docker
```

### Configure EC2 as self-hosted Runners
20. Go to your [GitHub Project](https://github.com/Gourav052003/Iris-WebApp-Deployement-on-AWS/tree/main) --> `Settings` --> `Actions` --> `Runners` --> `New self-hosted runner`
21. select the `Linux` and run the following commands on Ubuntu EC2 instance terminal for downloading GitHub Actions Runner.
```
# Create a folder
$ mkdir actions-runner && cd actions-runner

# Download the latest runner package
$ curl -o actions-runner-linux-x64-2.314.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.314.1/actions-runner-linux-x64-2.314.1.tar.gz

# Optional: Validate the hash
$ echo "6c726a118bbe02cd32e222f890e1e476567bf299353a96886ba75b423c1137b5  actions-runner-linux-x64-2.314.1.tar.gz" | shasum -a 256 -c

# Extract the installer
$ tar xzf ./actions-runner-linux-x64-2.314.1.tar.gz
```

22. Configure the GitHub Actions Runner using Commands:
```
# Create the runner and start the configuration experience
$ ./config.sh --url https://github.com/Gourav052003/Iris-WebApp-Deployement-on-AWS --token ATOIALLTYUWFB54KS62L5NTGAKAKI

# user name of runner group as --> self-hosted

# Last step, run it!
$ ./run.sh
```

### Setup Secrets in GitHub repository
23. Navigate to `Settings` --> `Secrets and variables` --> `Actions`
24. Add following secrets by clicking on `New repositiry secret`
```
AWS_ACCESS_KEY_ID= in .csv file we downloaded

AWS_SECRET_ACCESS_KEY= in .csv file we downloaded

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = 566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = myapp
```

### configuring security of EC2 instance
25. open EC2 instance --> `Security` --> click on `security groups` 
26. Edit `Inbound Rules` --> `Add Rule` --> save rules
```
Custom TCP, Anywhere traffic , port 5000 
```

27. open Public IP with port :5000 in EC2 instance to see your app running on EC2 











1. `docker init` to create the necessary Docker assets to containerize your application

```
docker init
```

2. `docker init` provides some default configuration, but you'll need to answer a few questions about your application. For example, this application uses Flask to run. Refer to the following example to answer the prompts from docker init and use the same answers for your prompts.

3. Following files will be added:
 * [Dockerfile](https://docs.docker.com/reference/dockerfile/)
 * [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)
 * [compose.yaml](https://docs.docker.com/compose/compose-file/)

4. Run the application using following command in a terminal.
```
docker compose up --build

# detached mode
docker compose up --build -d
```

5. Open a browser and view the application at http://localhost:5000

6. In the terminal, run the following command to stop the application.
```
docker compose down
```

