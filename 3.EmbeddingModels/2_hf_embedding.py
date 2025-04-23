from langchain_huggingface import HuggingFaceEmbeddings

# this time we will directly down the embedding model on out system and we will use it locally
# this means that we do not need to use any APIs so we will not load any API callers

# we put using the HuggingFaceEmbedding class to create an object of it and then use that object to create an embedding model which we will have locally on our machine
embedding_object = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


query = "Why is the sky blue?"

vector = embedding_object.embed_query(query)
# for i in range(len(vector)):
    # print(vector[i])
# print(vector)

# print(len(vector))

documents = [
    "Imran Khan is a charismatic leader and former cricket star.",
    "Abdul Sattar Edhi is remembered as a kind humanitarian who helped many.",
    "Benazir Bhutto was a trailblazing politician and the first woman to lead a Muslim-majority nation.",
    "Nusrat Fateh Ali Khan was a legendary qawwali singer whose music touched hearts globally.",
    "Shahid Afridi is a celebrated cricketer known for his explosive batting and bowling skills.",
    "Wasim Akram is revered as one of the greatest fast bowlers in cricket history.",
    "Abida Parveen is a soulful Sufi singer whose voice enchants audiences worldwide.",
    "Atif Aslam is a popular singer whose melodious voice has won the hearts of millions.",
    "Ali Zafar is a multi-talented artist known for his contributions to music, film, and art."
]

# we have created vectors for each of the document
vectors_list = embedding_object.embed_documents(documents)

# this will be a 2D list
print(vectors_list)
