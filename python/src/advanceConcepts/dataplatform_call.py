import requests
import json

apiUrl="http://mgmtservice.inteks-sf-dataplatform-mtt.svc.cluster.local:8080/dataplatform-mgmt/v1/mgmt/tenants"
headers = { 'Content-Type': 'application/json' }
data = {
    "data": {
        "type": "onboarding-sync",
        "attributes": {
            "tenants": [
                {
                    "tenantId": "THISEDR1-08FE-4DC2-AA7B-2023TESTTHIS",
                    "sourceType": [
                        "EDR"
                    ],
                    "dataRetentionDays": 30,
                    "entitledLicenseCount": 100,
                    "companyName": "abcd",
                    "partnerAccountNumber": "abcd1234",
                    "locale": "USA",
                    "countryCode": "US",
                    "region": "us-west",
                    "referenceNumber": "abcd1234"
                }
            ]
        }
    }
}

resp = requests.post(apiUrl, headers=headers, data=json.dumps(data))

print(resp.status_code)
print(resp.text)