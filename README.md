# Deployment of IRIS Flask Web App using Putty and WinSCP on AWS EC2 Instance

1. Download [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) and [WinSCP](https://winscp.net/eng/download.php).
2. Create an Ubuntu EC2 instance on AWS.
3. Allow `All traffic` from `Anywhere`  in security groups of EC2 Instance. 
4. Create a Key pair in .pem or .ppk format and download it.
5. Now select the created instance and click on `connect`.
6. Navigate to SSH client and copy the `public DNS`.
7. Open WinSCP and paste the copied `public DNS` in `Host name` .
8. Now, Navigate to `EC2 Instance Connect` and copy the `username` and paste it in `username` in WinSCP.
9. For `Password` in WinSCP click on `Advanced` --> navigate to SSH --> Authentication, then in `private key file` input box browse for .pem or .ppk file that we earlier downloaded.
10.  If file is in .pem format than it will get automatically converted to .ppk and click `Yes` if it ask for permissions.
11. click on `Login` and click on `Yes` to do the authentication and for connecting to Host EC2 machine on AWS.

12. Drop the files from your local machine to Host EC2 ubuntu machine by drag and drop or by right click in file --> upload button.

13. A Putty terminal will get opened.

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