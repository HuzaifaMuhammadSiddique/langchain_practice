from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
template="""
Please generate {number} of questions on the following topic of Data Structures in Computer Science: {topic}.
The style of the questions will be {style}.
I want you to generate the questions in the following programming language: {prog_lang}.
All of the questions should be {answer}
The questions should we unique.
I want you to test my {question_type}
Should the questions be very tricky questions? {tricky}
""",
input_variables=["number", "topic", "style", "prog_lang", "answer", "question_type", "tricky"],
validate_template=True
)


template.save("template.json")