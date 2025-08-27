import pandas as pd

# 1. Load raw data (example CSV)
data = pd.read_csv("raw_data.csv")

print("Original Data:")
print(data.head())

# 2. Clean data
# Remove duplicate rows
data = data.drop_duplicates()

# Fill missing numeric values with mean
data['Temperature'] = data['Temperature'].fillna(data['Temperature'].mean())

# Fill missing categorical values with mode
data['Condition'] = data['Condition'].fillna(data['Condition'].mode()[0])

# 3. Shape / Transform
# Rename columns for clarity
data = data.rename(columns={"Temp": "Temperature", "Hum": "Humidity"})

# Create a new feature
data['FeelsLike'] = data['Temperature'] - (100 - data['Humidity'])/10

# Encode categorical variables (Condition: Sunny/Rainy → 0/1)
data['Condition_encoded'] = data['Condition'].astype('category').cat.codes

# 4. Save cleaned + shaped data
data.to_csv("cleaned_data.csv", index=False)

print("\nPrepared & Shaped Data:")
print(data.head())
