import ollama


def create_embedding(text):
    response = ollama.embed(
        model="nomic-embed-text",
        input=text
    )
    
    return response["embeddings"][0]

if __name__ == "__main__":
    text = "PostgreSQL is the primary database used by Project Ascend."

    embedding = create_embedding(text)

    print("Embedding dimensions:", len(embedding))
    print("First 10 values:", embedding[:10])