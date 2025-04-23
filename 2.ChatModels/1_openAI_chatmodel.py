from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# temperature is between 0 and 2 and it is a measure of creativity and randomness
# max_completion_tokens is a measure of how many tokens will be returned by the model
model = ChatOpenAI(model="model_name", temperature=2, max_completion_tokens=10)

result = model.invoke("prompt message")

# directly printing the result variable will give us the JSON representation of the output give by the model
print(result)

# So just to access the content (text) of the response, we can access the content attribute of our result variable
print(result.content)