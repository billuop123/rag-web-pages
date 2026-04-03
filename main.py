from url_handler import get_valid_urls
from processor import build_knowledge_base
from qa_loop import run_qa_loop


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
