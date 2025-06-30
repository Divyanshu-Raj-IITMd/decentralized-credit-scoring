# ipfs_integration/upload_to_ipfs.py

import requests

def upload_to_ipfs(file_path):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {
        "pinata_api_key": "YOUR_API_KEY",
        "pinata_secret_api_key": "YOUR_SECRET_KEY"
    }

    with open(file_path, "rb") as file:
        response = requests.post(url, files={"file": file}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Adjust based on actual response keys
        cid = data.get("IpfsHash") or data.get("Hash") or data.get("cid")
        if not cid:
            raise ValueError(f"IPFS upload succeeded but response missing CID: {data}")
        return f"https://gateway.pinata.cloud/ipfs/{cid}"
    else:
        raise Exception(f"IPFS upload failed: {response.status_code} - {response.text}")
