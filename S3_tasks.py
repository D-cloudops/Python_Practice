"""
This script is to take backup to S3
"""

import boto3
import datetime
import os
from os.path import isfile, join

s3=boto3.client('s3',region_name='eu-west-1')    

def create_bucket(s3, bucket_name):
    """
    Creates a new S3 bucket with the specified name.

    Args:
        s3: The boto3 S3 client object.
        bucket_name (str): The name of the bucket to create.

    Prints a success message upon creation.
    """
    response = s3.create_bucket(
        Bucket= bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-1',
        },
    )
    print("bucket created successfully")

def list_buckets(s3):
    """
    Lists all S3 buckets associated with the account.

    Args:
        s3: The boto3 S3 client object.

    Prints the names of all buckets.
    """
    response = s3.list_buckets()
    print("list of bucket: ")
    for bucket in response['Buckets']:
        print(bucket['Name'])

def list_objects(s3,bucket_name):
    """
    Lists all objects in the specified S3 bucket.

    Args:
        s3: The boto3 S3 client object.
        bucket_name (str): The name of the bucket to list objects from.

    Prints the keys of all objects in the bucket.
    """
    print("list of objects: ")
    list_objects=s3.list_objects(Bucket=bucket_name)
    for objects in list_objects.get('Contents', {}):
        print(objects['Key'])
    
def upload_object(s3,bucket_name,key_name,file_location):
    """
    Uploads all files from a local directory to the specified S3 bucket.

    Args:
        s3: The boto3 S3 client object.
        bucket_name (str): The name of the S3 bucket to upload to.
        key_name (str): The key name for the objects (though it seems to be used as prefix).
        file_location (str): The local directory path containing files to upload.

    Note: This function uploads each file with the same key_name, which might overwrite files.
    """
    list_files=[join(file_location,file) for file in os.listdir(file_location) if isfile(join(file_location,file))]
    print(list_files)
    for file in list_files:
        with open(file, 'rb') as content:
            updated_object=s3.put_object(
                Bucket=bucket_name,
                Key=key_name,
                Body=content
                )
    print("backup updated successfully")
    

def delete_object(s3,bucket_name,delete_key_name):
    """
    Deletes an object from the specified S3 bucket.

    Args:
        s3: The boto3 S3 client object.
        bucket_name (str): The name of the S3 bucket.
        delete_key_name (str): The key of the object to delete.

    Prints a success message with the deleted key.
    """
    delete_response=s3.delete_objects(
        Bucket=bucket_name,
        Delete={
            'Objects': [{
            'Key': delete_key_name
        },
        ]}
    )
    print(f"Bucket deleted successfully: {delete_response['Deleted'][0]['Key']}")
    
# Main script execution: Prompt user for operation and execute accordingly
operation=input("Enter the operation to perform:  \ncreate-bucket\nlist-bucket\nlist-objects\nupload-object\ndelete-object\n")

if operation=='create-bucket':
    create_bucket_name=input("Bucket name to be created: ")
    create_bucket(s3,create_bucket_name)
elif operation=='list-bucket':
    list_buckets(s3)
elif operation=='list-objects':
    bucket_name=input("Bucket name to list objects: ")
    list_objects(s3,bucket_name)
elif operation=='upload-object':
    bucket_name=input("Bucket name to upload object: ")
    key_name=input("Key name of object to be uploaded: ")
    file_location=input("Location of objects")
    upload_object(s3,bucket_name,key_name,file_location)
elif operation=='delete-object':
    bucket_name=input("Bucket name")
    delete_key_name=input("Key name of object to delete: ")
    delete_object(s3,bucket_name,delete_key_name)
else:
    print ("Provide one of the mention operation: \ncreate-bucket\nlist-bucket\nlist-objects\nupload-object\ndelete-object")




# Example usage (commented out):
#bucket_name='boto-first-bucket'
#today=datetime.date.today()
#key_name=f"local-backup-{today}"
#backup_location='/workspaces/Python_Practice/backup/'
#delete_key_name=f"local-backup-{today}"
#list_buckets(s3)
#upload_backup(s3,bucket_name,key_name,backup_location)
#delete_object(s3,bucket_name,delete_key_name)
#list_objects(s3,bucket_name)