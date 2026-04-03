from fetcher import fetch, parse
from chunker import chunk_text
from embedder import build_index


def process_url(url):
    print(f"\nFetching: {url}")
    content = fetch(url)
    
    if not content:
        print(f"Unable to fetch {url}")
        return []
    
    title, text = parse(content)
    if not text:
        print(f"Unable to parse {url}")
        return []
    
    chunks = chunk_text(text)
    for chunk in chunks:
        chunk['url'] = url
        chunk['title'] = title
    
    print(f"Created {len(chunks)} chunks from {title}")
    return chunks


def build_knowledge_base(urls):
    print("Building knowledge base...")
    all_chunks = []
    
    for url in urls:
        all_chunks.extend(process_url(url))
    
    if not all_chunks:
        print("\nNo content extracted from any URLs. Exiting.")
        return None, None
    
    print(f"\nTotal chunks: {len(all_chunks)}")
    return build_index(all_chunks)
