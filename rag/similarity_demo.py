import math


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
    vector_a = [1, 2, 3]
    vector_b = [1, 2, 3]
    # try these examples to experiment
    # vector_a = [1, 2, 3]
    # vector_b = [1, 2, 4]
    
    # vector_a = [1, 0]
    # vector_b = [0, 1]

    similarity = cosine_similarity(vector_a, vector_b)

    print("Similarity:", similarity)