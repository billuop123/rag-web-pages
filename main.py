from fetcher import fetch, parse
from chunker import chunk_text
from embedder import build_index, search
from generator import generate_answer

def main():
    urls = [
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://en.wikipedia.org/wiki/Artificial_intelligence"
    ]
    
    print("Building knowledge base...")
    all_chunks = []
    
    for url in urls:
        print(f"\nFetching: {url}")
        webContent = fetch(url)
        
        if not webContent:
            print(f"Unable to fetch {url}")
            continue
        
        title, text = parse(webContent)
        if not text:
            print(f"Unable to parse {url}")
            continue
        
        chunks = chunk_text(text)
        # Add source URL to each chunk
        for chunk in chunks:
            chunk['url'] = url
            chunk['title'] = title
        
        all_chunks.extend(chunks)
        print(f"Created {len(chunks)} chunks from {title}")
    
    print(f"\nTotal chunks: {len(all_chunks)}")
    index, all_chunks = build_index(all_chunks)
    
    print("\n" + "="*80)
    print("RAG SYSTEM READY - Ask questions (type 'quit' to exit)")
    print("="*80)
    
    while True:
        query = input("\nYour question: ").strip()
        
        if query.lower() in ['quit', 'exit', 'q']:
            break
        
        if not query:
            continue
        
        results = search(query, index, all_chunks)
        generate_answer(query, results)

if __name__ == "__main__":
    main()
    
