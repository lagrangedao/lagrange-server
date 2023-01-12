import os
from dotenv import load_dotenv
from mcs import BucketAPI, APIClient
from backend.obj_model.bucket import Bucket
from backend.obj_model.file import File

if __name__ == '__main__':
    load_dotenv("./../../.env")

    api_key = os.getenv('api_key')
    access_token = os.getenv('access_token')
    mcs_api = APIClient(api_key, access_token)
    bucket_client = BucketAPI(mcs_api)
    for b in bucket_client.get_buckets()['data']:
        bucket_info: Bucket = Bucket(b)
        bucket_client.upload_to_bucket(bucket_info.bucket_uid, "./../dataset/data/hello_world.zip")
        print(bucket_info.bucket_name)
        for f in bucket_client.get_full_file_list(bucket_info.bucket_uid):
            file_data: File = File(f)
            print(file_data.to_json())
