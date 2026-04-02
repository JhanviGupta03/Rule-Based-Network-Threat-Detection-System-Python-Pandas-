import pandas as pd

# Simulated network traffic data
data = {
    "packet_size": [200, 1500, 300, 2500, 100],
    "failed_logins": [0, 3, 0, 4, 1]
}

df = pd.DataFrame(data)

# Decision logic
def detect_threat(row):
    if row["packet_size"] > 1000 or row["failed_logins"] > 2:
        return "BLOCK"
    else:
        return "ALLOW"

df["Action"] = df.apply(detect_threat, axis=1)

print(df)
