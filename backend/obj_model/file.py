import json
import os

from dotenv import load_dotenv


class File:
    def __init__(self, file_data):
        self.name = file_data["Name"]
        self.address = file_data["Address"]
        self.bucket_uid = file_data["BucketUid"]
        self.filehash = file_data["FileHash"]
        self.prefix = file_data["Prefix"]
        self.size = file_data["Size"]
        self.payloadCid = file_data["PayloadCid"]
        self.ipfs_url = file_data["IpfsUrl"]
        self.pin_status = file_data["PinStatus"]
        self.is_deleted = file_data["IsDeleted"]
        self.is_folder = file_data["IsFolder"]
        self.updated_at = file_data["UpdatedAt"]
        self.created_at = file_data["CreatedAt"]
        self.deleted_at = file_data["DeletedAt"]

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
