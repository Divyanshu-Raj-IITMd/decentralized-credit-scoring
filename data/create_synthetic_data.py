import pandas as pd
import numpy as np
np.random.seed(42)

n = 1000
data = pd.DataFrame({
    "monthly_income": np.random.randint(10000, 100000, n),
    "phone_bill_paid_on_time": np.random.choice([0, 1], n),
    "electricity_usage": np.random.randint(100, 1000, n),
    "num_apps_installed": np.random.randint(10, 200, n),
    "social_media_hours": np.round(np.random.uniform(0, 10, n), 1),
    "upi_txn_count": np.random.randint(0, 50, n),
    "sms_notifs": np.random.randint(0, 20, n),
    "location_cluster": np.random.choice([0, 1, 2], n),
})

data["creditworthy"] = (
    (data["monthly_income"] > 30000) &
    (data["phone_bill_paid_on_time"] == 1) &
    (data["upi_txn_count"] > 5)
).astype(int)

data.to_csv("data/synthetic_credit_data.csv", index=False)
print("✅ Data generated!")