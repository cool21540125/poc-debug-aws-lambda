
def lambda_handler(event, context):
    print(f"event {event}")
    print(f"context: {context}")

    response = {
        'statusCode': 200,
        'body': 'hello from lambda'
    }