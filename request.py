import requests
import json

url = "http://127.0.0.1:5000"
# sample data
data = {'NET CHARGE': 4
      , 'A': 0.0
      , 'C': 0.0
      , 'D': 0.0
      , 'E': 0.0
      , 'F': 0.0
      , 'G': 0.056
      , 'H': 0.056
      , 'I': 0.111
      , 'K': 0.0
      , 'L': 0.0
      , 'M': 0.0
      , 'N': 0.111
      , 'P': 0.333
      , 'Q': 0.056
      , 'R': 0.167
      , 'S': 0.0
      , 'T': 0.0
      , 'V': 0.056
      , 'W': 0.0
      , 'Y': 0.056
    }
data= json.dumps(data)
send_request= requests.post(url, data)
print(send_request.json())


