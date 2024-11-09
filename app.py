import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
wcss=[]

data=pd.read_csv("data/preprocessed/age_diabetess1.csv")
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()