# coding=utf-8

# 참고링크 : https://aws.amazon.com/ko/sdk-for-python/
# pip를 이용해 bodo3 설치 필요
# .aws/credentials 파일에 계정 설정 필요

# 결과 : AWS SDK를 활용하여 S3 버킷에 업로드한다.

import boto3

# Create an S3 client

s3 = boto3.client('s3')

filename = 'json.txt'
bucket_name = 'elasticbeanstalk-ap-northeast-2-134745719369'

# 특정 s3 폴더에 위치시키기 위해 folder/{} 를 추가해준다.
s3.upload_file(filename, bucket_name, 'toto/{}'.format(filename))
s3.put_object_acl(ACL='public-read', Bucket=bucket_name, Key='toto/{}'.format(filename))
