from langchain_caai.caai_emb_client import caai_emb_client

embeddings = caai_emb_client(
    api_key="your CAAI api key",
    api_url="your CAAI api url",
)

query_result = embeddings.embed_query("Whats up dawg")
print(query_result)