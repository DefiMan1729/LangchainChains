# Employee Performance Review Automation
The code uses LangChain to create a chain of language models that perform different tasks such as summarizing the employee’s performance, identifying their weaknesses, and providing a recommendation plan. The code takes a manager's feedback about an employee through the command line and outputs the results of each task as a dictionary. The code can be useful for managers who want to automate the process of writing performance reviews for their employees

## LangChain
LangChain is a Python library that allows you to create and execute natural language processing (NLP) tasks using a chain of language models. You can use LangChain to perform tasks such as summarization, sentiment analysis, text generation, and more.

## Installation
To install LangChain, you can use pip:

```bash
pip install langchain
```

## Usage
To use LangChain, you need to import the `langchain` module and the language models that you want to use. For example, if you want to use OpenAI's GPT-3 model, you can import the `ChatOpenAI` class from the `langchain.chat_models` module. You also need to import the `ChatPromptTemplate` and `HumanMessagePromptTemplate` classes from the `langchain.prompts.chat` module to create prompts for the language models.

Then, you can create a chain of language models using the `LLMChain`, `SimpleSequentialChain`, or `SequentialChain` classes from the `langchain.chains` module. A chain is a sequence of language models that take the output of the previous model as input and produce an output for the next model. You can specify the input and output variables for each chain and the final output of the whole chain.

For example, suppose you want to create a chain that takes a review text as input and produces a summary of the employee's performance, their weaknesses, and a recommendation plan as output. You can use the following code:

```python
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain

# Initialize the OpenAI model
# Note: I have already set my OpenAI keys as an environment variable. You need to do the same.
llm = ChatOpenAI()

# Create prompts for each task
template1 = "give me a summary of this employee's performance\n{review}"
prompt1 = ChatPromptTemplate.from_template(template1)
template2 = "identify the employee's weaknesses\n {review_summary}"
prompt2 = ChatPromptTemplate.from_template(template2)
template3 = "provide a recommendation plan\n {weakness}"
prompt3 = ChatPromptTemplate.from_template(template3)

# Create chains for each task
chain1 = LLMChain(llm=llm,prompt=prompt1,output_key='review_summary')
chain2 = LLMChain(llm=llm,prompt=prompt2,output_key='weakness')
chain3 = LLMChain(llm=llm,prompt=prompt3,output_key='recommendation')

# Create a sequential chain that combines all the chains
seq_chain = SequentialChain(chains = [chain1,chain2,chain3],
                            input_variables=['review'],
                            output_variables=['review_summary','weakness','recommendation'])

# Execute the chain with an example review text
_review = "The employee has shown great initiative and creativity in their projects. They have delivered high-quality work on time and within budget. They have also demonstrated excellent communication and collaboration skills with their team members and clients. The employee is a valuable asset to the company and deserves recognition for their achievements."

result = seq_chain(_review)

# Print the results
print(result.keys())
print('\n')
print("Review Summary")
print(result['review_summary'])
print('\n')
print("Weaknesses")
print(result['weakness'])
print('\n')
print("Recommendations")
print(result['recommendation'])
```

The output of this code would be something like:

```python
dict_keys(['review', 'review_summary', 'weakness', 'recommendation'])


Review Summary
The employee is a high-performing and creative professional who delivers quality work and communicates well with others.

Weaknesses
The employee does not have any major weaknesses, but they could improve their skills in some areas such as data analysis, leadership, or time management.

Recommendations
The employee should be given more opportunities to learn new skills and take on more responsibilities. They should also be rewarded for their outstanding performance and encouraged to continue their growth.
```

## Documentation
For more information on how to use LangChain, please refer to the [documentation].

## License
LangChain is licensed under the [MIT License].
