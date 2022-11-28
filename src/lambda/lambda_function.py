
def lambda_handler(event, context):
   
    version= '0.0.2'

    print("Hello world")
    return {  
        'statusCode': 200,
        'body': 'Lambda deployed using github  actions 1.6XX',
        'headers': {
            "Content-Type": "application/json"
        }    
    }       