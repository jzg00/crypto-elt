import requests, boto3, csv, datetime

# fetch prices from CoinGecko API
response = requests.get(
  "https://api.coingecko.com/api/v3/simple/price",
  params={"ids":"bitcoin,ethereum","vs_currencies":"usd"}
)

data = response.json()

# write data to CSV
now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
filename = f"prices_{now}.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["symbol","price","ts"])
    for coin, vals in data.items():
        writer.writerow([coin.upper(), vals["usd"], now])

# upload to S3
s3 = boto3.client("s3")
s3.upload_file(filename, "crypto-elt-2025", f"crypto/{filename}")
print(f"Uploaded {filename} to crypto/{filename}")



