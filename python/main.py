from testrail import *
import pprint
 
client = APIClient('https://cloudbyte.testrail.com')
client.user = 'user'
client.password = 'password'

# ------------------------------------------------------------

result = client.send_post(
	'add_plan/1',
    {
	"name": "testsuite5-ck",
    }
)
print(result)
print("----------------(upto plan)------------------")

# ---------------------------------------------------------------

# result = json.dumps(result)
# pprint.pprint(result)

# ---------------------------------------------------------------

id = result['id']
arg = 'add_plan_entry/'+str(id)
result = client.send_post(
	arg,
    {
    "suite_id": "795"
    }
)
# result = json.dumps(result)
print(result)
print("--------------(upto add plan entry)--------------------")

# ---------------------------------------------------------------

store = result['runs']
run_id = store[0]['id']
id = result['suite_id']
arg2 = 'get_cases/1&suite_id='+str(id)
case = client.send_get(arg2)
print(case)
print("----------------(upto get cases)------------------")

# ----------------------------------------------------------------

id2 = case[0]['id']
arg2 = 'add_result_for_case/'+str(run_id)+'/'+str(id2)
result = client.send_post(
	arg2,
    { 'status_id': 1, 'comment': 'This is added by ck!' }
)
print(result)
print("----------------(upto add result for case)------------------")

# ----------------------------------------------------------------
