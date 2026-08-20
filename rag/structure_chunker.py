import re


def load_document(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def structure_aware_chunks(text):
    chunks = []

    current_section = None
    current_subsection = None
    current_content = []

    for line in text.splitlines():

        if line.startswith("# "):
            if current_content:
                chunks.append(
                    create_chunk(
                        current_section,
                        current_subsection,
                        current_content
                    )
                )

            current_section = line[2:].strip()
            current_subsection = None
            current_content = []

        elif line.startswith("## "):
            if current_content:
                chunks.append(
                    create_chunk(
                        current_section,
                        current_subsection,
                        current_content
                    )
                )

            current_subsection = line[3:].strip()
            current_content = []

        elif line.strip():
            current_content.append(line.strip())

    if current_content:
        chunks.append(
            create_chunk(
                current_section,
                current_subsection,
                current_content
            )
        )

    return chunks


def create_chunk(section, subsection, content):
    return {
        "text": " ".join(content),
        "metadata": {
            "section": section,
            "subsection": subsection
        }
    }


if __name__ == "__main__":
    document = load_document("documents/architecture.md")

    chunks = structure_aware_chunks(document)

    for index, chunk in enumerate(chunks):
        print(f"\n--- Chunk {index} ---")
        print("Text:", chunk["text"])
        print("Metadata:", chunk["metadata"])