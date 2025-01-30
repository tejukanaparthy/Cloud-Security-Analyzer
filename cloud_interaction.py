import boto3
from google.cloud import storage

def get_aws_s3_buckets():
    client = boto3.client('s3')
    buckets = client.list_buckets()
    return [bucket['Name'] for bucket in buckets['Buckets']]

def get_gcp_storage_buckets():
    client = storage.Client()
    buckets = client.list_buckets()
    return [bucket.name for bucket in buckets]

