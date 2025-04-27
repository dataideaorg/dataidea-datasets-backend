from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class DatasetStorage(S3Boto3Storage):
    """
    Custom storage for dataset files that places them in the datasets/ folder
    of the 'dataidea-base-bucket' bucket.
    """
    location = settings.AWS_LOCATION
    file_overwrite = False 