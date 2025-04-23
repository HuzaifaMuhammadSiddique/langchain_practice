from langchain_core.prompts import prompt

# This allows us to use the locally installed model through the standard langchain LLM interface

import streamlit as st  # open-source
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline

# AutoTokenizer will be used for converting the prompt into tokens.
# AutoModelForCasualLM is used to load our model in the program
# Casual signifies the concept that the model is a kind of model that predicts the next word given the context.
# Pipeline does the job of input processing, tokenizing and output processing for us
# from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM


# We are not able to access the modelusing the Hugging Face API because there is a problem in the server.
# Since we have installed the model locally on our system, we will access it directly and we will load it into # # our program.
# For this we will use the transformers library


# model_path = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


# # This allows us to get the tokenizer and model loader
# tokenizer = AutoTokenizer.from_pretrained(model_path)
# local_model = AutoModelForCausalLM.from_pretrained(model_path)

# # We have specified the task, the model and the tokenizer
# local_pipeline = pipeline("text-generation", model=local_model, tokenizer=tokenizer)

# # We have loaded the model through and used a langchain wrapper here using the transformer pipeline
# llm = HuggingFacePipeline(pipeline=local_pipeline)

def format_output(string):
    array = string.split()
    for i in range(len(array)):
        if array[i].lower() == '<|assistant|>':
            new_array = array[i+1:]
            break

    result = " ".join(new_array)
    return result


llama = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # id of model
    task="text-generation",
)

model = ChatHuggingFace(llm=llama)



# SIMPLE WEB PAGE #

# header
st.header("Mini Bot")
st.write("This bot can answer any general knowledge question within seconds!")

# input box
user_input = st.text_input("ASK anything!")
# summary_prompt = "Summarize the following text: " + user_input
# button
is_clicked = st.button("Ask")


# sending user input to model
if is_clicked:
    result = model.invoke(user_input)  # getting response from the model 
    st.write(format_output(result.content))  # displaying the responses


