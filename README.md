 # Auto Anki

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/usmanwardag/auto_anki)

[![Build Status](https://app.travis-ci.com/usmanwardag/auto_anki.svg?branch=main)](https://app.travis-ci.com/usmanwardag/auto_anki)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5646662.svg)](https://doi.org/10.5281/zenodo.5646662)
[![codecov](https://codecov.io/gh/usmanwardag/auto_anki/branch/main/graph/badge.svg?token=EEGIC8T7QM)](https://codecov.io/gh/usmanwardag/auto_anki)

[![GitHub license](https://img.shields.io/github/license/usmanwardag/auto_anki)](https://github.com/auto_anki/research_buddy/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/usmanwardag/auto_anki)](https://github.com/auto_anki/research_buddy/issues)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/usmanwardag/auto_anki)](https://github.com/usmanwardag/auto_anki/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub stars](https://img.shields.io/github/stars/usmanwardag/auto_anki)](https://github.com/usmanwardag/auto_anki/stargazers)

If you are someone who struggles to memorise concepts taught in class, who is always in a dilemma about the topics that can be asked during exams? 
Or someone who faces extreme difficulty during revision? Then let us introduce you to revision buddy-"Auto Anki".

<img src="https://media.giphy.com/media/nMjVMvWm2JIT8Rd1Gt/giphy.gif" width="300" height="300">

Yes, you read that right. 

Auto Anki, is a tool which extracts important concepts from lectures and frames questions based on it. It searches for the answer on the web and provides the right answer to the respective questions. And not only this, you can also rate the difficulty level by the end of every question thereby making it very easy for you to memorise the tougher questions. 

## Why should you use Auto Anki?

- Personalised Revision Buddy “Auto Anki”.
- It breaks down the lecture pdf into questions and answers.
- Creates Flashcards for easy memorisation.
- It will save time which eventually will provide you with extra time to revise.

<img src="https://media.giphy.com/media/7TMZ8O1bbf1UAnS4Ve/giphy.gif" width="400" height="300">

## Check out the video!

https://user-images.githubusercontent.com/89510237/140457745-198c016b-645a-47b5-9c0d-90df793fb122.mp4

# Installation

- Clone the repository 
 ` git clone https://github.com/usmanwardag/auto_anki`
- Install all requirements
 ` pip install -r requirements.txt`
- Install project as Python package
 ` pip install .`
- Clone Anki library
 ` git clone https://github.com/kerrickstaley/genanki; cd genanki`
- Install Anki library
 ` python setup.py install`

## Code Documentation

`Using Pycco for python code documentation:`

   Run the following commands on the terminal:
- pip install pycco
- pycco auto_anki/**/*.py -p

## How to Contribute
  
We would be happy to receive contributions! If you'd like to, please go through our [CONTRIBUTING.md](https://github.com/usmanwardag/auto_anki/blob/main/CONTRIBUTING.md). 

For any feedback, issues, or bug reports, please create an issue [here](https://github.com/usmanwardag/auto_anki/issues/new).

## Future RoadMap
#### Build a GUI interface for the user
  -  Currently, we are using command line interface to get the user input such as the path of the file to be uploaded or the name of the Anki deck. This is can be improved by building a GUI for the user input.
#### Support for additional file types other than .pdf
  - As of now, our appliation is capable of processing only .pdf files. Other file types such as .ppt, .doc can be added in scope.
#### Build a browser extension with the current functionality
  - A browser extension which will extract contents of the current webpage which the user is on and produce a new deck of anki cards based on the material.
#### Improve word extraction logic
  - Currently Spacy is being used to extract noun phrases from each slide/page of the document. Then the high frequency noun phrases are calculated and used in the final search query. However this causes an issue when every slide has the document’s author name and email address listed. The author name is considered as a noun phrase, and since it appears on every slide has a high frequency, and thus appears on the final search query.


## Contributors

* [Kriti Khullar](https://github.com/kriti0207)
* [Muskan Gupta](https://github.com/muskan7828)
* [Suneha Bose](https://github.com/sbosenc)
* [Usman Mahmood Khan](https://github.com/usmanwardag)


 


