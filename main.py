import boto3

# Replace these values with your actual AWS access key and secret access key
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'

# Create an S3 client with the provided credentials
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Specify the bucket name
bucket_name = 'your-bucket-name'

# List objects in the bucket
response = s3_client.list_objects(Bucket=bucket_name)

# Print the object keys
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print('No objects found in the bucket.')
