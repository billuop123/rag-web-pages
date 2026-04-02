import faiss
import numpy as np
from typing import List, Tuple

class VectorStore:
    def __init__(self, dimension: int):
        """Initialize FAISS index."""
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []
        self.metadata = []
    
    def add(self, embeddings: np.ndarray, chunks: List[str], metadata: List[dict]):
        """Add embeddings and their corresponding chunks to the index."""
        self.index.add(embeddings.astype('float32'))
        self.chunks.extend(chunks)
        self.metadata.extend(metadata)
    
    def search(self, query_embedding: np.ndarray, k: int = 3) -> List[Tuple[str, dict, float]]:
        """Search for top-k most similar chunks."""
        distances, indices = self.index.search(
            query_embedding.reshape(1, -1).astype('float32'), k
        )
        
        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx < len(self.chunks):
                results.append((self.chunks[idx], self.metadata[idx], float(dist)))
        
        return results
