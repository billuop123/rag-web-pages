from fetcher import fetch, parse
from chunker import chunk_text
from embedder import build_index, search
from generator import generate_answer


def get_valid_urls():
    user_input = input("Enter URLs separated by space: ")
    urls = [u.strip() for u in user_input.split() if u.strip().startswith(('http://', 'https://'))]
    
    if not urls:
        print("No valid URLs provided. URLs must start with http:// or https://")
    return urls


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


def run_qa_loop(index, chunks):
    print("\n" + "="*80)
    print("RAG SYSTEM READY - Ask questions (type 'quit' to exit)")
    print("="*80)
    
    while True:
        query = input("\nYour question: ").strip()
        
        if query.lower() in ['quit', 'exit', 'q']:
            break
        
        if query:
            results = search(query, index, chunks)
            generate_answer(query, results)


def main():
    urls = get_valid_urls()
    if not urls:
        return
    
    index, chunks = build_knowledge_base(urls)
    if index is None:
        return
    
    run_qa_loop(index, chunks)


if __name__ == "__main__":
    main()
