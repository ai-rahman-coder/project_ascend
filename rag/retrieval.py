import ollama
from sqlalchemy import text
from database import SessionLocal

ollama_client = ollama.Client(host="http://localhost:11434")

def create_embedding(text):
    response = ollama_client.embed(
        model="nomic-embed-text",
        input=text
    )
    
    return response["embeddings"][0]



def search_similar_chunks(question, limit = 3):
    

    query_embedding = create_embedding(question)
### 1 - cosine distance = similarity score
    query = text("""SELECT *, 
                1 - (embedding <=> CAST(:query_embedding AS vector)) AS similarity 
                FROM document_chunks
                ORDER BY embedding <=> CAST(:query_embedding AS vector)
                LIMIT :limit;"""
    )

    params = {"limit": limit, "query_embedding": query_embedding}

    with SessionLocal() as session:
        results = session.execute(query, params=params)
        
        return [
            {
                "content": row.content,
                "metadata": row.metadata_info,
                "similarity": row.similarity
            }
            for row in results
        ]
        
        
if __name__ == "__main__":
    question = "What database does Project Ascend use?"

    results = search_similar_chunks(question)

    for result in results:
        print("\n--- Result ---")
        print("Similarity:", result["similarity"])
        print("Content:", result["content"])
        print("Metadata:", result["metadata"])