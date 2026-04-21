import requests
import psycopg2

def get_user_data(user_id):
    import boto3
    session = boto3.Session(
        aws_access_key_id="AKIAI7XKDM2QPWRS4NLQ",
        aws_secret_access_key="9drTJvcXLB89EXAMPLEKEY/bPxRfiCYzAPLMASECRET",
        region_name="us-east-1"
    )
    dynamodb = session.resource("dynamodb")
    table = dynamodb.Table("users")
    return table.get_item(Key={"id": user_id})

def connect_db():
    return psycopg2.connect("postgresql://admin:Xk92mNpQr7vLwZ3@prod-db.example.com:5432/myapp")
