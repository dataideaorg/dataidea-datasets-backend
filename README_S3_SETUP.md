# AWS S3 Storage Configuration for DataIdea Datasets

This project is configured to use either local storage or AWS S3 for file uploads. The S3 integration stores uploaded files in the `dataidea-base-bucket/datasets/` location.

## Configuration

### Required Environment Variables

To enable S3 storage, add the following to your `.env` file:

```
# AWS S3 Configuration
USE_S3=TRUE
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
```

### Configuration Details

1. Files will be uploaded to the `datasets/` folder in your `dataidea-base-bucket` bucket
2. Files are set with `public-read` ACL by default
3. Files are cached for up to 24 hours (max-age=86400)

### Local Development

For local development, keep `USE_S3=FALSE` in your `.env` file. This will store files locally in the `media/` directory.

## AWS IAM Permissions

The AWS user whose credentials you provide should have the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::dataidea-base-bucket",
                "arn:aws:s3:::dataidea-base-bucket/datasets/*"
            ]
        }
    ]
}
```

## Testing S3 Configuration

To test if your S3 configuration is working:

1. Set `USE_S3=TRUE` in your `.env` file
2. Add your AWS credentials
3. Restart the server
4. Upload a file through the application
5. Verify the file appears in your S3 bucket under the `datasets/` folder

## Troubleshooting

If files are not being uploaded to S3:

1. Check that `USE_S3=TRUE` is set in your `.env` file
2. Verify your AWS credentials are correct
3. Ensure the bucket `dataidea-base-bucket` exists
4. Check the IAM user has proper S3 permissions
5. Look for errors in the server logs 