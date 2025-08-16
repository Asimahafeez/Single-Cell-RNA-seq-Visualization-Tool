# Single-Cell RNA-seq Visualization Tool

This project is an interactive Streamlit application for exploring single-cell transcriptomic data.  
Users can upload a gene expression matrix (CSV format) and generate PCA and t-SNE plots with clustering.

## Features
- Upload single-cell RNA-seq expression matrix
- Dimensionality reduction using PCA and t-SNE
- Clustering with k-means
- Example dataset included for testing

## Project Structure
AI-SingleCell-Visualization/
│── app.py              # Streamlit application  
│── requirements.txt    # Dependencies  
│── sample_data.csv     # Example dataset  
│── README.md           # Documentation  

## Installation
Clone this repository and install dependencies:

```bash
git clone https://github.com/YourUsername/AI-SingleCell-Visualization.git
cd AI-SingleCell-Visualization
pip install -r requirements.txt
