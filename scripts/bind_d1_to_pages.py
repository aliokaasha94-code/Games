import requests
import json

account_id = "91d00526ee0af8e04ce79a1897ebf523"
token = os.getenv("CLOUDFLARE_API_TOKEN", "")
project_name = "emad-afandi-games-hub"
d1_id = "046a76ed-8537-4309-be8e-dfa039b4fe73"

url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project_name}"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# First GET the current project configuration
r = requests.get(url, headers=headers)
print("GET status:", r.status_code)
if r.status_code == 200:
    proj = r.json().get('result', {})
    print("Project name:", proj.get('name'))
    configs = proj.get('deployment_configs', {})
    print("Current deployment configs:", json.dumps(configs, indent=2))
    
    # Update with D1 binding
    patch_body = {
        "deployment_configs": {
            "production": {
                "d1_databases": {
                    "DB": {
                        "id": d1_id
                    }
                }
            },
            "preview": {
                "d1_databases": {
                    "DB": {
                        "id": d1_id
                    }
                }
            }
        }
    }
    pr = requests.patch(url, headers=headers, json=patch_body)
    print("PATCH status:", pr.status_code)
    if pr.status_code == 200:
        print("Successfully bound D1 database DB to Cloudflare Pages project!")
    else:
        print("PATCH error:", pr.text)
else:
    print("GET error:", r.text)
