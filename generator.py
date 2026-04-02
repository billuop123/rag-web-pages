import google.generativeai as genai
import os

conversation_history = []

def generate_answer(query, results):
    """Generate answer using Gemini 2.5 Flash based on retrieved context."""
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("\nError: Set GEMINI_API_KEY environment variable")
        return
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Display evidence
    print("\n" + "="*80)
    print("RETRIEVED EVIDENCE:")
    print("="*80)
    for i, result in enumerate(results, 1):
        print(f"\n[{i}] Source: {result.get('url', 'Unknown')}")
        print(f"    Title: {result.get('title', 'Unknown')}")
        print(f"    Score: {result['score']:.4f}")
        print(f"    Text: {result['text'][:200]}...")
    print("="*80)
    
    # Build context
    context = "\n\n".join([f"[Source: {r.get('url', 'Unknown')}]\n{r['text']}" for r in results])
    
    # Build conversation history
    history = "\n".join([f"Q: {h['question']}\nA: {h['answer']}" for h in conversation_history[-3:]])
    
    prompt = f"""Based on the following context from web pages, answer the question.

Context:
{context}

Previous conversation:
{history}

Current question: {query}

Answer:"""
    
    response = model.generate_content(prompt, stream=True)
    print("\n" + "="*80)
    print("ANSWER:")
    print("="*80)
    
    answer_text = ""
    for chunk in response:
        print(chunk.text, end='', flush=True)
        answer_text += chunk.text
    
    print("\n" + "="*80)
    
    # Store in history
    conversation_history.append({"question": query, "answer": answer_text})
