import sys
import requests
import json

def main(params):
    
    # Used to identify the specific task being called from Watson Assistant
    if params['type'] == "character_height":
        # URL used for API call
        url = "https://swapi.co/api/people/?search="+params['text']
        # Set headers
        headers = {'accept': 'application/json'}
        # Make API call
        r = requests.get(url,headers)
        # Process failed API call
        if r.status_code != 200:
            return {
                'statusCode': r.status_code,
                'headers': { 'Content-Type': 'application/json'},
                'body': {'message': 'Error processing your request'}
            }
        # Process successful API call 
        else:
            res = json.loads(r.content)
            height = res["results"][0]["height"]
            return {
                'statusCode': 200,
                'headers': { 'Content-Type': 'application/json'},
                'body': {"message":height}
            }
    else:
        pass

