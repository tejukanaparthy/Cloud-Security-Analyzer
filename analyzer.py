from cloud_interaction import get_aws_s3_buckets, get_gcp_storage_buckets
from security_checks import check_public_s3_buckets, check_unencrypted_gcp_buckets

def analyzer():
    aws_buckets = get_aws_s3_buckets()
    public_s3_buckets = check_public_s3_buckets(aws_buckets)
    print(f"Public AWS S3 Buckets: {public_s3_buckets}")

    gcp_buckets = get_gcp_storage_buckets()
    unencrypted_gcp_buckets = check_unencrypted_gcp_buckets(gcp_buckets)
    print(f"Unencrypted GCP Storage Buckets: {unencrypted_gcp_buckets}")

if __name__ == "__main__":
    analyzer()
