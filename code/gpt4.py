import openai
from dotenv import load_dotenv
import os


def get_gpt_link_answers(url):
    load_dotenv()
    API_KEY = os.environ["API_KEY"]
    openai.api_key = API_KEY
    completion = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": url+'''

    Go through this link and Can you create 3 anki cards on important topics in this?
    "Generate the anki cards in the following format. I will provide an example below. Make sure to have contain in the brackets '[]' " \
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
                                "(called the first principal component), the second greatest variance on the second coordinate, and so on.'}] " \"
                                ''',
            },
        ],
    )
    print(completion.choices[0].message.content)
