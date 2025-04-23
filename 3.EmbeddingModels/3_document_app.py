'''
GOAL OF THE APP
The app wiill take some documents as a strings in 1D list and it will also take a query as a string.

The app will tell us that the answer of this question is mostly likely to be present in which of the documents.

The app will return the document in which the answer may be present and it will also give us the cosine similarity score for it.

This is how the app will work:
1. Create an embedding of the query
2. Create an embedding of the documents
3. Find the cosine similarities between the query and each of the documents. And store them in a list.
4. Print out the document with the highest cosine similarity score

'''

'''
IMPORTANT
Because this is a very basic application, so we are not storing the embeddings that we are creating and thus our model has to create the embeddings every time we run the program which is both costly and time-consuming. It is better to store these embeddings in a vector database which we will talk about later
'''


# for embedding model
from langchain_huggingface import HuggingFaceEmbeddings

# function to find cosine similarity
from sklearn.metrics.pairwise import cosine_similarity


embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Prophet Muhammad, whose gentle leadership, profound compassion, and visionary teachings transformed the rugged sands of 7th-century Arabia into a beacon of faith and unity, continues to illuminate hearts and minds around the globe.",
    "Imam Ali, renowned for his unparalleled bravery, deep philosophical insight, and steadfast commitment to justice and equality, remains an enduring symbol of moral integrity and spiritual wisdom across generations.",
    "Jalal ad-Din Rumi, the mystical poet and Sufi sage whose lyrical verses weave intricate tapestries of divine love, inner transformation, and the eternal quest for truth, captivates and inspires a global audience to explore the depths of their own souls.",
    "Ibn Sina, celebrated both as Avicenna and a towering polymath, revolutionized medicine, philosophy, and the sciences with his insightful treatises that continue to influence the evolution of knowledge and the pursuit of truth.",
    "Ibn Battuta, whose intrepid travels spanned continents and cultures, chronicled his extraordinary adventures in vivid detail, offering a mesmerizing glimpse into the diverse, interconnected world of the medieval era.",
    "Salahuddin Ayyubi, widely admired as Saladin, showcased a rare blend of military genius, chivalric honor, and humanitarian grace, earning respect and admiration from both allies and former foes during the turbulent times of the Crusades.",
    "Malala Yousafzai, with her unwavering courage and passionate advocacy for girls’ education, has ignited a worldwide movement for human rights and equality, becoming a symbol of hope and resilience in the face of adversity.",
    "Muhammad Ali, the iconic boxer whose explosive prowess in the ring was matched only by his articulate stand on social justice and humanitarian causes, continues to inspire millions with his defiant spirit and charismatic leadership.",
    "Fatima al-Fihri, the visionary founder of one of the oldest existing universities, dedicated her life to fostering knowledge and learning, leaving an indelible legacy that champions intellectual freedom and female empowerment.",
    "Muhammad Iqbal, the poet-philosopher whose stirring verses and revolutionary ideas sparked a cultural and intellectual renaissance in the subcontinent, artfully combined spiritual depth with a passionate call for self-realization and national awakening."
]


query = input("Query: ")


query_vector = embedding_model.embed_query(query)

document_vectors = embedding_model.embed_documents(documents)

# this will give us a 2D list which weill have only one 1D list and in that list we will have the similarities
similarities = cosine_similarity([query_vector], document_vectors) # the reason why we are passing the query_vector as a 2D list is that this function takes two 2D lists and returns a 2D list

# get the first 1D list in the 2D list or in other words convert it into a 1D list
scores = similarities[0] 

# enumerate() adds a counter to an iterable and returns an enumerate object.
# This is useful when we want to use the index and the value of the iterable
# we have also converted the enumerate object into a list and this will give us a list of tuples
scores = list(enumerate(scores))

# now we need to sort this list but we need to sort this using the second value in each of the tuple in the list. this is because the first element is the index while the second element is the actual value
sorted_scores = sorted(scores, key=lambda x:x[1])


# Now we need to extract the index and the score of the documengt with the highest cosine similarity
index, score = sorted_scores[-1] # since it is sorted in ascending order, the highest is at the end of the list

# OUTPUT
print("Query: " + query)
print("Document: " + documents[index])
print("Similarity Score: ", score)





