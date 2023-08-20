# S3-BOTO3-Bucket-Lister
This project is a simple Python script utilizing the Boto3 library to list objects within an AWS S3 bucket. It provides a basic demonstration of how to interact with AWS services programmatically using access key credentials, although best practices would recommend using more secure authentication methods.

-----------------------------------
Steps to Run - 
1. Create a Bucket in S3 with all permissions (Read / Write)
2. Create IAM User Policy and Generate 'aws_access_key_id' / 'aws_secret_access_key'
3. Replace in 'main.py' values such as 'aws_access_key_id' / 'aws_secret_access_key' Bucket Name.
4. Run this command in terminal
   
   ```
   pip install boto3
   ```
5. Run the main.py file, and a list will appear in your terminal.

-----------------------------------
NOTE -  

> Hardcoding your AWS credentials directly in the code is not a secure practice.
> 
> If your code gets shared or stored in a public repository, your credentials could be exposed.
> 
> Instead, consider using a more secure method like environment variables, AWS config files, or IAM roles.

This is how it looks - 

<img src="https://i.imgur.com/CgpjTGj.png"/>
