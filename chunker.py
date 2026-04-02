
def chunk_text(text,chunk_size=200,overlap=50):
    """
    text: the cleaned string from the parser
    chunk_size: the size of each chunk
    overlap: the number of words to overlap between chunks
    """
    words=text.split()
    chunks=[]
    step=chunk_size-overlap
    for i in range(0,len(words),step):
        chunk_words=words[i:i+chunk_size]
        if len(chunk_words)<20:
            break
        chunk={
            "text":" ".join(chunk_words),
            "chunk_index":len(chunks)
        }
        chunks.append(chunk)
    return chunks