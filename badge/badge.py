# https://img.shields.io/badge/E2E%20test-passed-brightgreen.svg
# https://img.shields.io/badge/E2E%20test-failed-red.svg

from testrail import *
import pprint
from github import *
 
token = "f2cb8cd18adfbf922f3c1f9c1589ca0e6d9f2635"
filename="README.md"
repo = "chandankumar4/ansible"
branch="master"

client = APIClient('https://cloudbyte.testrail.com')
client.user = 'user'
client.password = 'pass'
value = client.send_get('get_run/1763')
# pprint.pprint(value)
total_passed = value['passed_count']
total_failed = value['failed_count']
result = (total_passed/(total_failed + total_passed)) * 100
# print(result)
if result == 100 :
    print('Test passed')
    push_to_github(filename, repo, branch, token)
    # https://img.shields.io/badge/e2e%20status-passed-brightgreen.svg
else:
    print('Test failed')
    push_to_github(filename, repo, branch, token)
    # https://img.shields.io/badge/e2e%20status-failed-red.svg

