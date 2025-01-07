import json
import boto3
from botocore.exceptions import ClientError

#Get Secrets
region_name = 'us-east-1'
db_secrets_key = 'mysqldb'
openapikey_secret_key = 'openaikey2'

session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)

try:
    db_secrets_value_response = client.get_secret_value(
        SecretId=db_secrets_key
    )

    openapikey_secret_value_response = client.get_secret_value(
        SecretId=openapikey_secret_key
    )


except ClientError as e:
    print("Error is-")
    # For a list of exceptions thrown, see
    # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    raise e


db_secrets = db_secrets_value_response["SecretString"]
openapikey_secret = openapikey_secret_value_response["SecretString"]

db_secrets = json.loads(db_secrets)
openapikey_secret = json.loads(openapikey_secret)


OPENAI_API_KEY = openapikey_secret["openaikey2"]
LLM_MODEL_NAME = "gpt-4-0125-preview"
USER = db_secrets["username"]
PASSWORD = db_secrets["password"]
HOST = db_secrets["host"]
DATABASE = "ecommerce"
PORT = db_secrets["port"]