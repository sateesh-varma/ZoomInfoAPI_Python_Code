from zi_api_auth_client import AuthClient
from company_search import companySearch
from company_enrich import companyEnrich
from company_contacts import company_contacts
import math

def user_name_pwd_authentication(user_name, password):
    auth_client = AuthClient(user_name)
    return auth_client.user_name_pwd_authentication(password)


def pki_authentication(user_name, client_id, private_key):
    auth_client = AuthClient(user_name)
    return auth_client.pki_authentication(client_id, private_key)

username="cmgvendorapi@deloitte.com"
client_id="fd3e4ad4-224b-409b-9b03-9c8825c8a384"
private_key= '''
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCg/6U/rim5E1xl
EjiElLNd++GP9/1jczYibYvrSWIptk2XFG5gOuvBEte46tRf2R5YiY54zUx08u2D
vxWPVQonllfNwKzPjDuYpho4bAtz9PFsbGY4k1hgrH0wokmWuyIkCil/3aDlGxIb
fe2nsHABMVV1kK0srsE+JEp5FI0Vx+LZiKEXUwmbYZsI1mIdC6rSKnDH92oRvkyR
dBYqaFLhcJmpTnVUNSO+PeC+Rcl6s8B4kdtU3ZSuI1Y1CzDbMTkVwhsm8dZ03bhp
X6ZqzP80Uc+oxUcrim+VW/DubkEGfz232JcCmktZ5Hzx5RXHBKDOi0rk/HKEsReD
u2Ibmf2tAgMBAAECggEAdfGykos5f58iYdzOULpLCL/8x6aKF7AQaXpNNYomAp7O
Cq7qCU9A5Mm0BYDrImiBpaToHbFwoIBS5eA3oDBRZxzpqA7NyqJWCocs0Ea+wS0h
LCfhXvL6nJ/gep95P5ZJ9ZMIQecP9qc1RbSkROOpugX1MFJTu1cutCKL+FXI4bnI
PIW2rEkQ1H/Viv5LD3vXxtwLBh14NwIbQFDdJWSEzVGtNXldNj9tQGJkAgSfuTdT
6jDZMzjmDjmfqd49H7udZ7NZtz3QZDjMHpGOxHg5ldW7wGs4eQ9qfY/rIFz0xEoL
HAGU/1PpcwtlBYSVqGhd7HR4xd1JDeylkkCok8XTYQKBgQDo99XBtssqNhs35dX3
c3eWCqYQiQ8xbqO4avIkgxPFXCPN3Ehp3zeMLiOpyplltHSOiy6dFAwtLsIORNPj
jcvsE/18qOFqUwq6HFh4yNCYzXjMcvW0zwZyomKHJf3Rppub9oFWVPFEi0Zy7PR1
HaGXMqIGP5a4JE0HffH8dgFViQKBgQCw6lejnARl7VYS+CdV36r7L9MnN8v5rEoS
CLNSemNAndSaJxymNSVUYRoMGc+E4eCpTMJSw/SVhhF0XkK6jVb7vQ9MZsPsrw4I
tQxwcwVPRqwLMQnqkE04EloAMI22hmNW0UZa7GoTrdYbHq4ehVd3D+41tYQbAl8Q
Ul2CDdZCBQKBgFknPu46/dTRj+j8U722unT47kQ1r1LDfHP+uVuvrclBUZJeUnfx
rFhA7/TyS3HYdSJ3sQb7vQ0tb6X2QQA8K2XU4JTsLBd8YAaJAnJ2px1SxH+5Hr5q
25TS/9GogFHS6Inu8+AN8abBhdxFQefvxv8NqWOqwgsGGVRcplZu8mPBAoGAfmyo
fily1yfYd6vP6ETy2ZeejAsKf3wIXoTLKKh/HuDq2dITXg7igz70rysOqcYEltdc
kmqn8OYiuQbXJpr0Suca9J0Ha67ZF43RutXnOHSnY0QC8xV1qRksKbCIxKOaf6MD
ZNxHHZL/StgM05C0JUhEESuKoQZ7yp0hZ1vd/cUCgYEA1aDwk2QOdOaZGBc8kprx
SkSKBTLvF89CcNuiJ3zAnO/j90SxEA0vUAQOjpbVJROzSZDQI7QnwOyFszw6kfPP
eFoajzAxE320gCb6rM6d4Ldx3Zl3qS+rxsNhyL6PdW9zhkwjxrq9ihvLWaBjXxfa
qRBm9x4Zo0TEzuhC0R56TtM=
-----END PRIVATE KEY-----'''

result_token = pki_authentication(username,client_id,private_key)
#print(result)

company_search_client = companySearch(result_token)
print(company_search_client.perfom_search('deloitte'))

print('------------------ENRICH API STARTS HERE-----------------------------')

company_enrich_client = companyEnrich(result_token)
result= company_enrich_client.company_enrich_details('34361792')
print(result[0]['data'][0])
print('-------------- DOMINAS---------------')

for d in result[0]['data'][0]['domainList']:
    print(d)
print('------------------------------ENRICH API ENDS HERE---------------------------')
'''
print('------Company contacts----------')

company_contacts_client = company_contacts(result_token)
#print(company_contacts_client.ge_company_contacts('141295847'))
company_contacts = company_contacts_client.ge_company_contacts('141295847')
for con in company_contacts:
    print(con.first_name)
print(len(company_contacts))



#print(converted_enrich_data.data['result'])#.data.result[0].data[0].number_of_contacts_in_zoom_info)


'''