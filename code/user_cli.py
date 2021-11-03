""" user_cli.py """
import shutil
import sys
import concurrent.futures
import pyfiglet
from extract_sizes import extract_words, text_to_groupings
import wordprocessing as wp
from google_search import get_people_also_ask_links
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from browser_output import output_formatter, result_display


def user_menu():
    """

    Runner class. Prompts the user for input and returns a txt file of results

    """
    format_welcome_message = pyfiglet.figlet_format("LECTURE AID")
    size = shutil.get_terminal_size(fallback=(120, 50))
    valid_choices = ["1", "2", "Q", "q"]
    print(format_welcome_message.center(size.columns) + "\n")
    print("Welcome to Lecture Aid. Choose from the following options:\n")
    print("Option 1: Press 1 to enter the file location you "
          "would like Lecture Aid to help you find resources on.")
    print("Option 2: Press 2 ")
    print()
    print("Press Q to quit the program.")

    while True:
        choice = input("Please Enter your choice:")[0]
        if choice in valid_choices:
            break

        print("That choice is not available now. Please try again")
        continue

    if choice == valid_choices[0]:
        file_path = input("Please enter the path to the file: ")
        return file_path

    if choice == valid_choices[1]:
        input("")

    elif choice in [valid_choices[-1], valid_choices[-2]]:
        print("Thank you for using Lecture Aid. Closing Program now.")
        sys.exit(0)

if __name__ == "__main__":
    file = user_menu()
    raw_data = extract_words(file)
    raw_data = text_to_groupings(raw_data)
    keyword_data = wp.extract_noun_chunks(raw_data)
    keyword_data = wp.merge_slide_with_same_headers(keyword_data)

    keyword_data = wp.duplicate_word_removal(keyword_data)
    search_query = wp.construct_search_query(
        keyword_data)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # when testing use searchquery[:10 or less].
        # Still working on better threading to get faster results
        results = executor.map(get_people_also_ask_links, search_query[:3])

    with open("results.txt", mode="w", encoding="utf-8") as f:
        for result in results:
            for qa in result:
                question = qa["Question"] + "\n"
                f.write(f"Question: {question}")
                answer = qa["Answer"] + "\n"
                f.write(f"Answer: {answer}")
                link = qa["Related Link"] +"\n"
                f.write(f"Related Link: {link}")
            f.write("\n\n")

    content = output_formatter()
    name = file.split("/")[-1].replace(".pdf", "")
    wordcloud_filename = name + ".png"
    result_display(content, wordcloud_filename)
