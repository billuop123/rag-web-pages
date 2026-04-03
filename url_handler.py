def get_valid_urls():
    user_input = input("Enter URLs separated by space: ")
    urls = [u.strip() for u in user_input.split() if u.strip().startswith(('http://', 'https://'))]
    
    if not urls:
        print("No valid URLs provided. URLs must start with http:// or https://")
    return urls
