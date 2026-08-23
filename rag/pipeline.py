from rag.retrieval import search_similar_chunks


def build_rag_messages(messages, question):
    
    chunks = search_similar_chunks(question)
    
    
    print("RETRIEVED CHUNKS:")
    for chunk in chunks:
        print(chunk["content"])
    context = "\n\n".join(chunk["content"] for chunk in chunks)
    
    prompt=f"""
    Answer the question using the context below.
    
    Context:
    {context}
    
    Question:
    {question}
    """
        
    messages[-1]["parts"][0]["text"] = prompt
    
    return messages