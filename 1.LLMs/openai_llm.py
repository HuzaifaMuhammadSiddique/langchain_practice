'''
Since we are going to use OpenAI API so for this we will need OpenAI API keys. For that we actually need to make an account on platform.openai.com and then we need to buy credits to access openAI API keys. For this we may need as low as $5.
Then we create a secret key using those credits and using that secret key we use make calls ot the OpenAI API in our program.
Since we cannot make open AI keys write know so we will just take some placeholder keys.
The placeholder secret key is placed in the file named .env
'''

# langchain_openai is an integration package and in this package we have the code for using openAI API. We will import this class called OpenAI which will allow us to call and use the API of OpenAI
from langchain_openai import OpenAI

# The purpose of this is to allow us to load secret keys and other things from the .env file
from dotenv import load_dotenv

# this function load the secret API key stored in the .env file into our code
load_dotenv()

# now we will create an object of the OpenAI class and the first argument that we will give to this object is the model that we want to use
llm = OpenAI(model="model_name")


# this .invoke() method helps us in communicating with the model
result = llm.invoke("prompt text")


# we can now print the response that the model gave us
print(result)