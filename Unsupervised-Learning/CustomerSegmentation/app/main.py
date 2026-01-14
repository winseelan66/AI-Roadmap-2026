from fastapi import FastAPI
from app.clustering import (
    load_and_prepare_data,
    elbow_method,
    apply_kmeans,
    visualize_clusters,
    summarize_clusters
)

app = FastAPI(title="Customer Segmentation API")

@app.get("/")
def health_check():
    return {"status": "Customer Segmentation API running"}


@app.get("/elbow")
def generate_elbow():
    _, scaled_data = load_and_prepare_data()
    image = elbow_method(scaled_data)
    return {"message": "Elbow chart generated", "file": image}

@app.get("/cluster")
def run_clustering(k: int = 5):
    df, scaled_data = load_and_prepare_data()
    clustered_df = apply_kmeans(df, scaled_data, k)
    image = visualize_clusters(clustered_df)
    summary = summarize_clusters(clustered_df)

    return {
        "clusters": summary,
        "visualization": image
    }