# OpenAIEmbedding is the class that enables us to intereact with the OpenAI Embedding model using an API
from langchain_openai import OpenAIEmbeddings

# import API key loader
from dotenv import load_dotenv

# call API key loader and load key
load_dotenv()


# we have created an object using the embedding class and this object will allow us to create embeddings of queries and documents
embedding_object = OpenAIEmbeddings(model="model_name", dimensions=32) # dimensions parameter specifies the number of dimensions of the vector (embedding) that will be produced

# this is the query of which we will make the embedding
query = "Why is the sky blue?"


'''
.embed_query() is a method that allows us to create a vector of the query. It takes in a string and gives us a 1D list of floats
'''
vector = embedding_object.embed_query(query)

# we convert the float list into a string for aesthetics
print(str(vector))


# we can also create a vectors for  documents.
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

vectors = embedding_object.embed_documents(documents)

# This will be a 2D list i.e. a list contain vectors where vectors themselves are 1D lists
print(str(vectors))



