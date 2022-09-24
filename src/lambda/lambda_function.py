
def lambda_handler(event, context):
   
    version= '0.0.1'

    print("Hello world")
    return {
        'statusCode': 200,
        'body': 'Lambda deployed using github actions',
        'headers': {
            "Content-Type": "application/json"
        }
    }