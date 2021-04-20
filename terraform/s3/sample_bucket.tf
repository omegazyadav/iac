# S3 Bucket(Sample)
resource "aws_s3_bucket" "sample_s3_bucket" {
  bucket = "sample-s3-${terraform.workspace}"
  acl    = "private"

  # Enable the bucket versioning
  versioning {
    enabled = true
  }

  tags = {
    Name        = "Sample S3 Bucket"
    Environment = terraform.workspace
  }
}

