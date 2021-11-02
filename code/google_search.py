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
                result.append({"Question": answer["question"], "Answer": answer["response"], "Related Link": answer["link"]})
    return result
