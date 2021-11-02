import genanki

def get_model():
    my_model = genanki.Model(
      1607392319,
      'Anki Model',
      fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
      ],
      templates=[
        {
          'name': 'Card',
          'qfmt': '{{Question}}',
          'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
      ])

    return my_model

def get_deck(deck_name):
    my_deck = genanki.Deck(
      2059400110,
      deck_name)
    return my_deck



def add_question(question, answer, model):
    my_note = genanki.Note(
      model=model,
      fields=[question, answer])
    return my_note


model = get_model()
deck = get_deck(deck_name='Capitals of the world')
qa = add_question(question='Capital of Argentina', answer='Buenos Aires', model=model)
deck.add_note(qa)
qa = add_question(question='USA', answer='DC', model=model)
deck.add_note(qa)

output_fname = 'capitals'
genanki.Package(deck).write_to_file(f'anki_decks/{output_fname}.apkg')


