import json
import os

bucket = os.environ.get("S3_BUCKET")
print("Policy for bucket:", bucket)

with open('policy.json', 'r') as f:
    policy = json.load(f)

policy['Statement'][0]['Resource'] = [f'arn:aws:s3:::{bucket}/*']
print(policy)

with open('policy_updated.json', 'w') as f:
    json.dump(policy, f, indent=4)