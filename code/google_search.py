# MIT License
#
# Copyright 2023 auto_anki
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" google_search.py """
import re
import people_also_ask


def get_people_also_ask_links(search_term: str) -> list:
    """
    Given a search term, returns the google People Also Ask links

    :param search_term: The query to google
    :type: str
    :rtype: list
    :return: list of links returned by people also ask
    """
    rel_qns = people_also_ask.get_related_questions(search_term)
    result = []
    if rel_qns:
        for rel_qn in rel_qns:
            question = re.search(r"[^?]*", rel_qn).group(0) + "?"
            answer = people_also_ask.get_answer(question)
            if answer["has_answer"]:
                result.append(
                    {
                        "Question": answer["question"],
                        "Answer": answer["response"],
                        "Related Link": answer["link"]
                    }
                )
    return result
