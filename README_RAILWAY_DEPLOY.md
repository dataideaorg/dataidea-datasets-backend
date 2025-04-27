# Railway Deployment Guide for DataIdea Dataset Backend

This guide explains how to deploy this Django application to Railway.app, including setting up an automatic superuser.

## Prerequisites

- A Railway.app account
- Git repository connected to Railway

## Environment Variables

Set the following environment variables in your Railway project:

### Required

```
SECRET_KEY=your_django_secret_key
DEBUG=False
ALLOWED_HOSTS=your-railway-app-name.up.railway.app,your-custom-domain.com
```

### Database (if using PostgreSQL)

Railway will automatically set these if you provision a PostgreSQL database:

```
PGDATABASE=
PGUSER=
PGPASSWORD=
PGHOST=
PGPORT=
```

### AWS S3 Configuration (if using S3 storage)

```
USE_S3=TRUE
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
```

### Automatic Superuser Creation

Set these to automatically create a Django superuser during deployment:

```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=your_secure_password
```

## Deployment

1. Connect your GitHub repository to Railway
2. Add the environment variables
3. Railway will automatically deploy using the provided Procfile
4. During deployment, our custom script will:
   - Apply database migrations
   - Create a superuser using the provided credentials
   - Collect static files
   - Start the Django application

## Updating Your Deployment

Simply push changes to your connected Git repository, and Railway will automatically redeploy.

## Local Testing

To test the superuser creation locally:

```bash
cd backend
./test_superuser.sh
``` 