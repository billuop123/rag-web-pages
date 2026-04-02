from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
model=SentenceTransformer('all-MiniLM-L6-v2')

def build_index(all_chunks):
    """
    takes the list of all chunks and builds a FAISS index
    """
    texts=[chunk['text'] for chunk in all_chunks]
    embeddings=model.encode(texts, show_progress_bar=True)
    dimension=embeddings.shape[1]
    index=faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index, all_chunks

def search(query,index,all_chunks,top_k=3):
    """
    Embed the user query and search the index and return the top n results
    """
    query_vector=model.encode([query]).astype('float32')
    distances, indices=index.search(query_vector,k=top_k)
    results=[]
    for i,idx in enumerate(indices[0]):
        results.append({
            "text":all_chunks[idx]['text'],
            "score":distances[0][i],
            "url":all_chunks[idx].get('url', 'Unknown'),
            "title":all_chunks[idx].get('title', 'Unknown')
        })
    return results

    