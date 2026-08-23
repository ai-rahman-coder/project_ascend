import ollama
import math


def create_embedding(text):
    response = ollama.embed(
        model="nomic-embed-text",
        input=text
    )

    return response["embeddings"][0]


def cosine_similarity(vector_a, vector_b):
    dot_product = sum(
        a * b
        for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    return dot_product / (magnitude_a * magnitude_b)


if __name__ == "__main__":

    texts = [
        "PostgreSQL is the primary database used by Project Ascend.",
        "Project Ascend stores its application data in PostgreSQL.",
        "Docker packages applications into containers.",
        "The weather is sunny today."
    ]

    embeddings = [
        create_embedding(text)
        for text in texts
    ]

    query = "Where does Project Ascend store its data?"

    query_embedding = create_embedding(query)

    for text, embedding in zip(texts, embeddings):

        similarity = cosine_similarity(
            query_embedding,
            embedding
        )

        print(f"\nSimilarity: {similarity:.4f}")
        print(f"Text: {text}")