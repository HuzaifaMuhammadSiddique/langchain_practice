# Again, to access the original model we use API and for that we need API keys and for that we need to buy tokens on the official website of the model. So we will have to go to console.anthropic.com and we will have to buy tokens and create a secret key which will allow to us access the API

from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="model_name")

result = model.invoke("prompt text")

print(result.content)