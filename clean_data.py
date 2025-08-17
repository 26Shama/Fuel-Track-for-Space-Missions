import pandas as pd

# Load the dataset
df = pd.read_csv("spacecraft_fuel_prediction_dataset.csv")

# Step 1: Drop missing and duplicate rows
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Step 2: Remove outliers
df = df[(df['payload_kg'] >= 100) & (df['payload_kg'] <= 1000)]
df = df[(df['thrust_kN'] >= 5000) & (df['thrust_kN'] <= 10000)]
df = df[(df['isp'] >= 200) & (df['isp'] <= 400)]

# (Optional) Step 3: Reset index after dropping rows
df.reset_index(drop=True, inplace=True)

# Step 4: Save the cleaned data
df.to_csv("clean_data.csv", index=False)
print("✅ Cleaned data saved to clean_data.csv")

# Optional: Show info
print("\nCleaned Dataset Info:")
print(df.info())