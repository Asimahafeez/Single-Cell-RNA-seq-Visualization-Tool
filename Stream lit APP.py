import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

st.set_page_config(page_title="Single-Cell RNA-seq Visualization Tool", layout="wide")

st.title("🧬 Single-Cell RNA-seq Visualization Tool")
st.write("Upload a single-cell RNA-seq expression matrix to explore PCA, t-SNE, and clustering.")

# File uploader
uploaded_file = st.file_uploader("Upload expression matrix (CSV)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, index_col=0)
    st.success(f"File loaded! Shape: {data.shape}")
    
    st.write("### Preview of data")
    st.dataframe(data.head())

    # Standardize (optional)
    st.write("### PCA Visualization")
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(data.values)
    pca_df = pd.DataFrame(pca_result, columns=["PC1", "PC2"], index=data.index)

    fig, ax = plt.subplots()
    sns.scatterplot(x="PC1", y="PC2", data=pca_df, s=40, color="blue", ax=ax)
    st.pyplot(fig)

    st.write("### t-SNE Visualization")
    tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=500)
    tsne_result = tsne.fit_transform(data.values)
    tsne_df = pd.DataFrame(tsne_result, columns=["Dim1", "Dim2"], index=data.index)

    fig, ax = plt.subplots()
    sns.scatterplot(x="Dim1", y="Dim2", data=tsne_df, s=40, color="green", ax=ax)
    st.pyplot(fig)

    # Clustering
    st.write("### K-means Clustering on PCA")
    k = st.slider("Select number of clusters (k)", 2, 10, 3)
    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(pca_df)
    pca_df["Cluster"] = clusters

    fig, ax = plt.subplots()
    sns.scatterplot(x="PC1", y="PC2", hue="Cluster", palette="tab10", data=pca_df, s=40, ax=ax)
    st.pyplot(fig)

    st.write("### Cluster Counts")
    st.dataframe(pca_df["Cluster"].value_counts())

else:
    st.info("Please upload a CSV file to start.")
