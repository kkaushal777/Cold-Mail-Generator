import uuid
import chromadb
import pandas as pd
import os

# Initialize the ChromaDB client and collection
client = chromadb.PersistentClient('vectorstore')

# def get_or_create_collection(collection_name):
#     return client.get_or_create_collection(collection_name)

def read_csv_file(csv_file_path):
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"{csv_file_path} does not exist")
    return pd.read_csv(csv_file_path)

def add_documents_to_collection(collection, df):
    if not collection.count():
        documents = df["Techstack"].tolist()
        metadatas = [{"links": link} for link in df["Links"]]
        ids = [str(uuid.uuid4()) for _ in range(len(df))]
        collection.add(documents=documents, metadatas=metadatas, ids=ids)

def query_collection(collection, query_texts, n_results):
    return collection.query(query_texts=query_texts, n_results=n_results)

def process_portfolio(csv_file_path, collection_name, query_texts, n_results):
    collection = client.get_or_create_collection(collection_name)
    df = read_csv_file(csv_file_path)
    add_documents_to_collection(collection, df)
    return query_collection(collection, query_texts, n_results)



