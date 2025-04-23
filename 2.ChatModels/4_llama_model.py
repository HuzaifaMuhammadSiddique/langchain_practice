# This code will help us in installing a specific model from HuggingFace

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # id of model
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Generate a simple programming question of DSA")

print(result.content)

