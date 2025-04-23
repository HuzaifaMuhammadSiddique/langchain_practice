import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core import prompts
from langchain_core.prompts import PromptTemplate, load_prompt


def format_output(string):
    array = string.split()
    for i in range(len(array)):
        if array[i].lower() == '<|assistant|>':
            new_array = array[i+1:]
            break

    result = " ".join(new_array)
    return result



model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0" 

llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# the model is ready, now we can use it


# WEB PAGE #

st.header("DSA Questions Generator")

number = st.selectbox("Number of Questions", ["1", "2", "5", "10", "15", "20", "30", "50"])

topic = st.selectbox("Select topic", ["Arrays", "Stacks", "Queues", "Trees","Binary Trees", "Graphs"])

style = st.selectbox("Select Style of Questions", ["MCQs", "FIBs", "Theoritical", "Code Writing", "Code Output Tracing", "Coding FIBs"])

prog_lang = st.selectbox("Programming Language", ["C++", "Python", "Java", "JavaScript"])

answer = st.selectbox("Answers", ["With Answers", "Without Answers"])

question_type = st.selectbox("Question Type", ["Understanding-Based","Knowledge-Based"])

tricky = st.selectbox("Tricky Questions?", ["Yes", "No"])

template = load_prompt("template.json")

# we fit the user selections with our dynamic prompt template
prompt = template.invoke({
    "number" : number,
    "topic" : topic,
    "style" : style,
    "prog_lang" : prog_lang,
    "answer" : answer,
    "question_type" : question_type,
    "tricky" : tricky
}
)

if st.button("Generate!"):
    result = model.invoke(prompt)
    st.write(format_output(result.content))





