import boto3
from botocore.exceptions import NoCredentialsError

# Defina as informações do seu bucket S3
AWS_ACCESS_KEY = 'AWS_ACCESS_KEY'
AWS_SECRET_KEY = 'AWS_SECRET_KEY'
BUCKET_NAME = 'BUCKET_NAME'
BUCKET_REGION = 'BUCKET_REGION'
FILE_PATH = 'arquivo.txt'
FILE_KEY = 'arquivo.txt'

# Inicializar o cliente do S3
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=BUCKET_REGION
)

try:
    s3.upload_file(FILE_PATH, BUCKET_NAME, FILE_KEY)
    print("Arquivo enviado com sucesso!")
except NoCredentialsError:
    print("Credenciais não encontradas")
except Exception as e:
    print("Erro:", e)