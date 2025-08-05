<!-- # Hierarchical-Clustering

<img width="1621" height="914" alt="image" src="https://github.com/user-attachments/assets/67ea4d9a-af49-46ee-aeb9-1f82e180f595" /> -->


## Hierarchical Clustering – Customer Segment Predictor

This project demonstrates Hierarchical Clustering to segment customers based on features such as age, income, and spending habits. A Flask-based web app allows users to input data and predict the cluster/segment their profile belongs to.

---

## What is Hierarchical Clustering?

Hierarchical Clustering is an unsupervised machine learning algorithm that builds a hierarchy of clusters. Unlike K-Means, it does not require predefining the number of clusters and visualizes results with a dendrogram.

---

##  Project Structure
```
Hierarchical-Clustering/
├── app.py               # Flask web app for prediction
├── train_model.py       # Script to train Agglomerative Clustering model
├── model.pkl            # Saved trained model
├── encoders.pkl         # Encoded mappings (if any)
├── data.csv             # Dataset used for training
│
├── templates/
│   └── index.html       # Web UI

```
---

##  Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/Hierarchical-Clustering.git
cd Hierarchical-Clustering
```
Install dependencies
```
pip install -r requirements.txt
```
Run the application
```
python app.py
```
Open in browser

Visit: http://localhost:10000

# Sample Input
```
Gender: Male

Age: 28
Annual Income: $55,000
Spending Score: 78
Time on App: 35 mins
Membership Years: 2
```
## Screenshots
<img width="1621" height="914" alt="image" src="https://github.com/user-attachments/assets/67ea4d9a-af49-46ee-aeb9-1f82e180f595" />

## Future Improvements
Auto-detect optimal clusters via dendrogram cutoff

Visualization dashboard

Database integration for customer records

Export cluster reports as PDF