import requests

CF_API_KEY = "" # Your Global API KEY | https://dash.cloudflare.com/profile/api-tokens
CF_API_EMAIL = ""   # Your Email
CF_ID_ACCOUNT = ""  # Your ID Account | https://dash.cloudflare.com/ID_Account

# Save domain in domaincloudflare.txt
with open("domaincloudflare.txt", 'r') as f:
    for i in f.readlines():
        headers = {
            'X-Auth-Key': CF_API_KEY,
            'X-Auth-Email': CF_API_EMAIL,
            'Content-Type': 'application/json'
        }

        data = {
            'account': {'id': CF_ID_ACCOUNT},
            'name': i.strip('\n'),
            'jump_start': True
        }
        url = "https://api.cloudflare.com/client/v4/zones"

        r = requests.post(url, headers=headers, json=data)
        print(r.text)
