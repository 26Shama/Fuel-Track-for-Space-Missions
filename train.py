import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load cleaned data
df = pd.read_csv("clean_data.csv")

# Features and target
X = df[['payload_kg', 'thrust_kN', 'isp', 'launch_angle_deg', 'orbit_type', 'engine_type']]
y = df['fuel_required_kg']

# Define categorical and numerical columns
categorical_cols = ['orbit_type', 'engine_type']
numerical_cols = ['payload_kg', 'thrust_kN', 'isp', 'launch_angle_deg']

# Preprocessing for categorical features + pass numerical as is
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ],
    remainder='passthrough'
)

# Create pipeline with preprocessing and model
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model pipeline
pipeline.fit(X_train, y_train)

# Save the pipeline to a file
joblib.dump(pipeline, 'spacecraft_fuel_model.pkl')

print("✅ Model trained and saved as 'spacecraft_fuel_model.pkl'")