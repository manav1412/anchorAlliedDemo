import ollama

response = ollama.chat(
    model = 'gemma3:latest',
    messages = [{
        'role': 'user',
        'content': 'What is in this image?',
        'images': ['/home/neebal/Desktop/POC/anchor-allied/Sample_PO/kitbi.jpg']
    }]
)

print(response.content)