import json
import os
import requests


url = os.getenv("API_URL")

def handler(event, context):

    try:

        response = requests.get(url)

        return {
            'statusCode': response.status_code,
            'body': json.dumps(response.json())
        }
    
    except Exception as e:

        print("error: ", e)

        return {
            'statusCode': 500,
            'body': {
                'error': "There was an error",
                'message': "We couldn't process the request"
            }
        }
