import requests
import os

defectdojo_apitoken = os.environ.get('DEFECTDOJO_APITOKEN')
token = "Token {}".format(defectdojo_apitoken)
header = { 'Authorization': token}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
'active': True,
'verified': True,
'scan_type': 'Gitleaks Scan',
'minimum_severity': 'Low',
'engagement': 18
}

files = {
'file': open('gitleaks-report.json', 'rb')
}

response = requests.post(url, headers = header, data=data, files=files)
print(response)

