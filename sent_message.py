

import requests
import json  

def sent_message(accessToken, responseMessage, roomId):
        HTTPHeaders = { 
                             "Authorization": f"Bearer {accessToken}",
                             "Content-Type": "application/json"
                           }
        # The Webex Teams POST JSON data
        # - "roomId" is is ID of the selected room
        # - "text": is the responseMessage assembled above
        PostData = {
                            "roomId": roomId,
                            "text": responseMessage
                        }
        # Post the call to the Webex Teams message API.
        r = requests.post( "https://webexapis.com/v1/messages", 
                              data = json.dumps(PostData), 
                              headers = HTTPHeaders
                         )
        if not r.status_code == 200:
            raise Exception("Incorrect reply from Webex Teams API. Status code: {}. Text: {}".format(r.status_code, r.text))