from langchain.langchain import LangChain
from deeplake.deeplake import DeepLake

langchain = LangChain()
deeplake = DeepLake()

langchain.load_model()
deeplake.load_model()

def answer_question(question):
    # Generate chain of related questions using LangChain
    chain = langchain.generate_chain(question)

    # Find the most relevant question from the chain using DeepLake
    relevant_question = deeplake.find_relevant_question(chain)

    # Get the answer for the relevant question using DeepLake
    answer = deeplake.get_answer(relevant_question)

    return answer

question = "What is the capital of France?"
answer = answer_question(question)
print("Question:", question)
print("Answer:", answer)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
