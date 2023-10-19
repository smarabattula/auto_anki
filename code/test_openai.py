from langchain.llms import OpenAI

from dotenv import load_dotenv
import os

#This script loads environment variables and prepares a request for generating Anki flashcards using the OpenAI API, with a prompt and format requirements for questions and answers related to principal components

load_dotenv()
API_KEY = os.environ["API_KEY"]

llm = OpenAI(openai_api_key=API_KEY)
text = "Can you create 3 anki cards on topic of principal components?"
dictionary_requirement = "Generate the anki cards in the following format. I will provide an example below. Make sure to have contain in the brackets '[]' " \
                         "[{'Question': 'What do principal components mean?', 'Answer': 'Principal components " \
                         "are new variables that are constructed as linear combinations or mixtures of the initial " \
                         "variables.'}, " \
                         "{'Question': 'What is principal component in PCA?', " \
                         "'Answer': 'Principal component analysis, or PCA, is a dimensionality reduction method that is " \
                         "often used to reduce the dimensionality of large data sets, by transforming a large set of " \
                         "variables into a smaller one that still contains most of the information in the large set.'}, " \
                         "{'Question': 'What is the principal component theory?', 'Answer': 'PCA is defined as an orthogonal " \
                         "linear transformation that transforms the data to a new coordinate system such that the greatest " \
                         "variance by some scalar projection of the data comes to lie on the first coordinate " \
                         "(called the first principal component), the second greatest variance on the second coordinate, and so on.'}] " \

chatgpt_prompt = text + dictionary_requirement

# Uncomment this to run the the prompt in chatgpt
print(llm.predict(chatgpt_prompt))


# test = "principal components"
# result = get_people_also_ask_links(test)
# print(result)


# test = "principal components"
# result = get_people_also_ask_links(test)
# print(result)


# import re
# import people_also_ask


# def get_people_also_ask_links(search_term: str) -> list:
#     """
#     Given a search term, returns the google People Also Ask links
#
#     :param search_term: The query to google
#     :type: str
#     :rtype: list
#     :return: list of links returned by people also ask
#     """
#     rel_qns = people_also_ask.get_related_questions(search_term)
#     result = []
#     if rel_qns:
#         for rel_qn in rel_qns:
#             question = re.search(r"[^?]*", rel_qn).group(0) + "?"
#             answer = people_also_ask.get_answer(question)
#             if answer["has_answer"]:
#                 result.append({"Question": answer["question"], "Answer": answer["response"], "Related Link": answer["link"]})
#     return result
