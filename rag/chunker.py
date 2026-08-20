import re


def load_document(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# 1. Character-based
def character_chunks(text, chunk_size=100):
    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]


# 2. Sentence-based
def sentence_chunks(text, max_sentences=2):
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    chunks = []

    for i in range(0, len(sentences), max_sentences):
        chunks.append(" ".join(sentences[i:i + max_sentences]))

    return chunks


# 3. Paragraph-based
def paragraph_chunks(text):
    return [
        paragraph.strip()
        for paragraph in text.split("\n\n")
        if paragraph.strip()
    ]


# 4. Recursive splitting
def recursive_split(text, chunk_size=200, overlap=50):
    text = text.strip()

    if len(text) <= chunk_size:
        return [text]

    paragraphs = text.split("\n\n")

    if len(paragraphs) > 1:
        chunks = []

        for paragraph in paragraphs:
            chunks.extend(recursive_split(paragraph, chunk_size, overlap))

        return merge_with_overlap(chunks, overlap)

    sentences = re.split(r"(?<=[.!?])\s+", text)

    if len(sentences) > 1:
        chunks = []

        for sentence in sentences:
            chunks.extend(recursive_split(sentence, chunk_size, overlap))

        return merge_with_overlap(chunks, overlap)

    words = text.split()

    chunks = []
    current = ""

    for word in words:
        candidate = f"{current} {word}".strip()

        if len(candidate) <= chunk_size:
            current = candidate
        else:
            if current:
                chunks.append(current)

            current = word

    if current:
        chunks.append(current)

    return merge_with_overlap(chunks, overlap)


def merge_with_overlap(chunks, overlap):
    if not chunks:
        return []
    
    result = [chunks[0]]
    
    for chunk in chunks[1:]:
        previous = result[-1]
        
        overlap_text = previous[-overlap:]
        
        result.append(
            overlap_text + " " + chunk
        )
    
    return result

def print_chunks(title, chunks):
    print(f"\n{'=' * 20} {title} {'=' * 20}")

    for index, chunk in enumerate(chunks):
        print(f"\n--- Chunk {index} ---")
        print(chunk)


if __name__ == "__main__":
    document = load_document("documents/project_ascend.txt")

    print_chunks(
        "CHARACTER",
        character_chunks(document)
    )

    print_chunks(
        "SENTENCE",
        sentence_chunks(document)
    )

    print_chunks(
        "PARAGRAPH",
        paragraph_chunks(document)
    )

    print_chunks(
        "RECURSIVE WITH OVERLAP",
        recursive_split(document)
    )