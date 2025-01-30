def check_public_s3_buckets(buckets):
    public_buckets = []
    for bucket in buckets:
        if is_bucket_public(bucket):
            public_buckets.append(bucket)
    return public_buckets

def is_bucket_public(bucket_name):
    return False 

def check_unencrypted_gcp_buckets(buckets):
    unencrypted = []
    for bucket in buckets:
        if not is_bucket_encrypted(bucket):
            unencrypted.append(bucket)
    return unencrypted

def is_bucket_encrypted(bucket_name):
    return True 