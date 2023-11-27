

def process_(file, c_count):
    try:
        update_status("Processing file...")
        lect_name = file.split("/")[-1].split(".")[0]

        if file.split("/")[-1].split(".")[1] == "pdf":
            pass
        elif file.split("/")[-1].split(".")[1] == "docx":
            template = f"soffice --headless --convert-to pdf {file}"
            os.system(template)
            file = file[:-5] + ".pdf"
        elif file.split("/")[-1].split(".")[1] == "pptx":
            # template = f"unoconv -f pdf '{file}'"
            template = f"soffice --headless --convert-to pdf {file}"
            os.system(template)
            file = file[:-5] + ".pdf"

        raw_data = extract_words(file)
        raw_data = text_to_groupings(raw_data)
        keyword_data = wp.extract_noun_chunks(raw_data)
        keyword_data = wp.merge_slide_with_same_headers(keyword_data)

        keyword_data = wp.duplicate_word_removal(keyword_data)
        search_query = wp.construct_search_query(
            keyword_data)
        # print(search_query)
        if source_choice.get() == "Google":
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                # when testing use searchquery[:10 or less].
                # Still working on better threading to get faster results
                results = executor.map(
                    get_people_also_ask_links, search_query[:c_count])
        elif source_choice.get() == "GPT":
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                results = executor.map(
                    gp.get_gpt_answers, search_query[:c_count])

        # selecting random customised number of flash cards
        results_new = [qapair for result in results for qapair in result]
        results_new = random.sample(results_new, int(c_count))
        auto_anki_model = get_model()
        deck = get_deck(deck_name=lect_name)
        for qapair in results_new:
            question = qapair["Question"]
            answer = qapair["Answer"]
            qa = add_question(
                question=f'{question}', answer=f'{answer}', curr_model=auto_anki_model)
            deck.add_note(qa)
        add_package(deck, lect_name)
        messagebox.showinfo(
            "Hurray!", "The Anki deck has been created successfully.")
        update_status("File processed successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Fcuntion for processing url
def process_url(url, c_count):
    try:
        update_status("Processing URL...")
        results = gp4.get_gpt_link_answers(url, c_count)
        results_json = results.replace("'", '"')
        results_list = json.loads(results_json)
        auto_anki_model = get_model()
        lect_name = url.split("/")[-1]
        deck = get_deck(deck_name=lect_name)
        for result in results_list:
            question = result["Question"]
            answer = result["Answer"]
            qa = add_question(
                question=f'{question}', answer=f'{answer}', curr_model=auto_anki_model)
            deck.add_note(qa)
        add_package(deck, lect_name)
        update_status("File processed successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
