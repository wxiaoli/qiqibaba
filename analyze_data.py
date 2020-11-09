# coding=utf-8

''' 聚类'''
from sklearn.cluster import KMeans
def clusting(arr, n_clusters):
    kmeans = KMeans(n_clusters)
    kmeans.fit(arr)
    cluster_centers = kmeans.cluster_centers_ 
    sample_labels = kmeans.labels_
    squared_distance_sum = kmeans.inertia_
    return cluster_centers, sample_labels, squared_distance_sum


''' t-SNE 降维
    t-distributed Stochastic Neighbor Embedding
    https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
'''
from sklearn.manifold import TSNE
def dim_reduction(arr, new_dim):
    reduced_arr = TSNE(n_components=new_dim).fit_transform(arr)
    return reduced_arr
