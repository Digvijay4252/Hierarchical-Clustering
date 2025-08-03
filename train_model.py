import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import AgglomerativeClustering
import joblib

# Load data
data = pd.read_csv('mall_customers.csv')

# Drop CustomerID
data = data.drop(columns=['CustomerID'])

# Encode Gender
le_gender = LabelEncoder()
data['Gender'] = le_gender.fit_transform(data['Gender'])  # Male=1, Female=0

# Select features for clustering
X = data[['Gender', 'Age', 'Annual_Income', 'Spending_Score']]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Agglomerative Clustering model
model = AgglomerativeClustering(n_clusters=5, linkage='ward')
model.fit(X_scaled)

# Save encoder and scaler only (model doesn't support .predict or saving)
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(le_gender, 'gender_encoder.pkl')

# Save original data with cluster labels for visual exploration
data['Cluster'] = model.labels_
data.to_csv('clustered_customers.csv', index=False)

print("Hierarchical Clustering completed. Scaler and encoder saved.")
