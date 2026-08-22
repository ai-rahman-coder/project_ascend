from rag.structure_chunker import structure_aware_chunks
import ollama
from database import SessionLocal, DocumentChunks

ollama_client = ollama.Client(host="http://host.docker.internal:11434")

### loading document 
def load_document(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
def create_embedding(text):
    response = ollama_client.embed(
        model="nomic-embed-text",
        input=text
    )
    
    return response["embeddings"][0]

document = load_document("rag/documents/architecture.md")

### structure aware chunk imported and used
chunks = structure_aware_chunks(document)

### for each chunk calling ollama embedding
with SessionLocal() as session:
    for chunk in chunks:
        text = chunk["text"]
        embedding = create_embedding(text)
        
        document_chunk = DocumentChunks(
            content = text,
            metadata_info = chunk["metadata"],
            embedding = embedding            
        )
        
        session.add(document_chunk)
    
    session.commit()