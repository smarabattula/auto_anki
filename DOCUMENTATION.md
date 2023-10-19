# Functionalities added to the older version:
### Making flash cards using ChatGPT
In the previous version, flash cards were created using google(People also asked section which was not accurate enough for generating Flash card answers. In this version, you have the option to choose to create the flash cards using ChatGPT 4 which is more accuarate and reliable)


### Answer search
In the previous version, only a relevant web link for a question was being extracted. In this version, we search the web for the relevant answers as well, and then find the best answer. Therefore, we do only show the user different questions but provide an end-to-end solution with both questions and answers.

### Anki Integration
We integrated a software tool called Anki with the current code, so that the question and answers can be stored as flashcards on Anki.

### Anki Decks
For each lecture, we create a deck, and then create multiple cards in the deck. Each card in the denotes a single question answer pair. We also developed logic to correctly store the cards, for Anki to use later.

### Improved UI
We made several improvements to the UI. For example, user can provide custom deck names, and specify where to store decks. We also made the onboarding easier to make the process of generating decks easier.

### Improved Test coverage (64% -> 96%)
We significantly improved the test coverage from 64% to 96%. To improve the coverage, we did not only write several additional tests, but also removed any redundant code that was not being used. 

### Improved Documentation
We generated the code documentation using a new format called Pycco. We also revamped the readme and other docs for better readability and user experience.

 
