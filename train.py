import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Load data
df = pd.read_csv("water_potability.csv")
df.fillna(df.median(numeric_only=True), inplace=True)

X = df.drop('Potability', axis=1)
y = df['Potability']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 3. Save model
joblib.dump(model, 'water_model.pkl')
print("Model Saved Successfully!")