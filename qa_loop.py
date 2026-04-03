from embedder import search
from generator import generate_answer


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
