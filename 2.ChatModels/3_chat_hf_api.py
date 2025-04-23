from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

# using the hugging face endpoint, we create the llm model.
# for this we need the model ID and we need to specify which task do we want the model to perform
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=os.environ["HF_API_TOKEN"] # this is used to specify where the API key is stored so that it can be easily accessed
)

# we need to pass a parameter called 'llm' when we are using a model from hugging face
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is Pakistan?")

print(result.content)

