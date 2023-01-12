import json


class Bucket:
    def __init__(self, bucket_data):
        self.deleted_at = bucket_data["DeletedAt"]
        self.updated_at = bucket_data["UpdatedAt"]
        self.created_at = bucket_data["CreatedAt"]
        self.file_number = bucket_data["FileNumber"]
        self.bucket_name = bucket_data["BucketName"]
        self.is_deleted = bucket_data["IsDeleted"]
        self.is_active = bucket_data["IsActive"]
        self.is_free = bucket_data["IsFree"]
        self.size = bucket_data["Size"]
        self.max_size = bucket_data["MaxSize"]
        self.address = bucket_data["Address"]
        self.bucket_uid = bucket_data["BucketUid"]

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
