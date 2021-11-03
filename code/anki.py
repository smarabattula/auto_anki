import genanki
import os


def get_model():
    """
    Define model that describes the template
    for anki deck.

    Returns
    ------
    anki model
    """

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
    """
    Define and initialize an anki deck, where we can add cards.

    Returns
    ------
    anki deck 
    """

    my_deck = genanki.Deck(
      2059400110,
      deck_name)
    return my_deck


def add_question(question, answer, curr_model):
    """
    Create a card for a question, answer pair.

    Returns
    ------
    anki card 
    """

    my_note = genanki.Note(
      model=curr_model,
      fields=[question, answer])
    return my_note


if __name__ == '__main__':
    model = get_model()
    deck = get_deck(deck_name='Capitals of the world')
    qa = add_question(question='Capital of Argentina', answer='Buenos Aires', curr_model=model)
    deck.add_note(qa)
    qa = add_question(question='USA', answer='DC', curr_model=model)
    deck.add_note(qa)

    output_fname = 'capitals'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    genanki.Package(deck).write_to_file(f'{dir_path}/{output_fname}.apkg')


