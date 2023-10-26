from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
llm = ChatOpenAI()

_review = input('Enter text...')

template1 = "give me a summary of this employee's performance\n{review}"
prompt1 = ChatPromptTemplate.from_template(template1)
chain1 = LLMChain(llm=llm,prompt=prompt1,output_key='review_summary')

template2 = "identify the employee's weaknesses\n {review_summary}"
prompt2 = ChatPromptTemplate.from_template(template2)
chain2 = LLMChain(llm=llm,prompt=prompt1,output_key='weakness')

template3 = "provide a recommendation plan\n {weakness}"
prompt3 = ChatPromptTemplate.from_template(template3)
chain3 = LLMChain(llm=llm,prompt=prompt1,output_key='recommendation')

seq_chain = SequentialChain(chains = [chain1,chain2,chain3],
                            input_variables=['review'],
                            output_variables=['review_summary','weakness','recommendation'])

result = seq_chain(_review)

print(result.keys())
print('\n')
print("Weaknesses")
print(result['weakness'])
print('\n')
print("Recommendations")
print(result['recommendation'])
