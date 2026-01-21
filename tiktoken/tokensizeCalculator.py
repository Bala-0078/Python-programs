import tiktoken
encoding_model=tiktoken.encoding_for_model("gpt-4o-mini")
text="Hello, how are you?"
tokens=encoding_model.encode(text)
print(tokens)