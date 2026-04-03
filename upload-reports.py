import requests
import os
import sys

file_name = sys.argv[1]
scan_type = ''

if file_name == 'gitleaks-report.json':
    scan_type = 'Gitleaks Scan'
elif file_name == 'semgrep-report.json':
    scan_type = 'Semgrep JSON Report'
elif 'dependency-check-report.json' in file_name:
    scan_type = 'Dependency Check Scan'


defectdojo_apitoken = os.environ.get('DEFECTDOJO_APITOKEN')
token = "Token {}".format(defectdojo_apitoken)
header = { 'Authorization': token}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
'active': True,
'verified': True,
'scan_type': scan_type,
'minimum_severity': 'Low',
'engagement': 17
}

files = {
'file': open(file_name, 'rb')
}

response = requests.post(url, headers = header, data=data, files=files)
print(response)

