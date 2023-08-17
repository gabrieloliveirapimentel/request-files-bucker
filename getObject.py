import boto3
from botocore.exceptions import NoCredentialsError

# Defina as informações do seu bucket S3
AWS_ACCESS_KEY = 'AWS_ACCESS_KEY'
AWS_SECRET_KEY = 'AWS_SECRET_KEY'
BUCKET_NAME = 'BUCKET_NAME'
BUCKET_REGION = 'BUCKET_REGION'
FILE_KEY = 'arquivo.txt'
DESTINATION_PATH = 'data/arquivo.txt'

# Inicializar o cliente do S3
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=BUCKET_REGION
)

# Download do arquivo do bucket S3
try:
    s3.download_file(BUCKET_NAME, FILE_KEY, DESTINATION_PATH)
    print("Arquivo baixado com sucesso!")
except NoCredentialsError:
    print("Credenciais não encontradas")
except Exception as e:
    print("Erro:", e)