import json
import datetime
import os
import time




os.system("chmod +x start")
os.system("chmod +x change")
os.system("chmod +x test1")
os.system("chmod +x time")

os.system("./start")

def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}



