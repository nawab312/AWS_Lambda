`check_ec2_public_ip.py`
This Lambda function checks all EC2 instances in an AWS account and identifies instances with public IP addresses, returning a compliance status indicating whether any instances are non-compliant by having public IPs.

`s3_upload.py`
This Lambda function processes an S3 file upload event, retrieves the uploaded file's content from the S3 bucket, logs the file's information, and returns a success message.
