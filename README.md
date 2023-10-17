# Auto Anki

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/SmayanaReddy/auto_anki)

![Build Status](https://img.shields.io/badge/build-passing-green)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5745931.svg)](https://doi.org/10.5281/zenodo.5745931)
![codecov](https://img.shields.io/badge/codecov-85%25-green)

[![GitHub license](https://img.shields.io/github/license/SmayanaReddy/auto_anki)](https://github.com/SmayanaReddy/auto_anki/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/SmayanaReddy/auto_anki)](https://github.com/SmayanaReddy/auto_anki/issues)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/SmayanaReddy/auto_anki)](https://github.com/SmayanaReddy/auto_anki/issues?q=is%3Aissue+is%3Aclosed)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/SmayanaReddy/auto_anki/pulls)
![version](https://img.shields.io/badge/version-3.0-blue)
![github workflow](https://github.com/SmayanaReddy/SRIJAS/actions/workflows/unit_test.yml/badge.svg)
![github workflow](https://github.com/SmayanaReddy/SRIJAS/actions/workflows/style_checker.yml/badge.svg)
![github workflow](https://github.com/SmayanaReddy/SRIJAS/actions/workflows/main.yml/badge.svg)
![github workflow](https://github.com/SmayanaReddy/SRIJAS/actions/workflows/code_cov.yml/badge.svg)

## [Demo Video](https://drive.google.com/file/d/12h5izedNfEth56KhbKFRBYDFKU2PPChQ/view?usp=sharing)


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#why-should-you-use-auto-anki">Why should you use Auto Anki?</a></li>
    <li><a href="#check-out-the-video">Check out the video!</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#code-documentation">Code Documentation</a></li>
    <li><a href="#how-to-contribute">How to Contribute</a></li>
    <li><a href="#future-roadmap">Future RoadMap</a></li>
   <li><a href="#contributors">Contributors</a></li>
   <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## Introducing Auto Anki – Your Ultimate Flashcard Companion Powered by ChatGPT 4!

Auto Anki revolutionizes your learning experience by effortlessly transforming your lecture materials into highly accurate and effective flashcards. This version of Auto Anki incorporates the advanced capabilities of ChatGPT 4, ensuring precision and relevance in every flashcard.

Auto Anki, building upon the intelligent Anki flashcard platform [Anki](https://apps.ankiweb.net/)  , generates flashcards from your lectures, making studying a breeze. It's the perfect tool for anyone who struggles to memorize class concepts, faces revision challenges, or simply prefers a more convenient note-taking approach.

## Here's what Auto Anki with ChatGPT 4 can do for you:

Extract crucial concepts from your lectures and generate questions based on them.
Search the web for the most relevant answers, guaranteeing the accuracy of your flashcards.
Utilize Anki's robust features, allowing you to rate the difficulty level of each question, making tough concepts easier to memorize.

## Why should you choose Auto Anki with ChatGPT 4?

Summarize entire lectures into flashcards, perfect for memorization.
Eliminate the manual effort of creating lecture flashcards in Anki.
Break down lecture PDFs into concise and effective question-and-answer pairs.
Create straightforward flashcards for effortless memorization and revision.
Auto Anki 4.0 is here to enhance your study experience and empower your academic success! 😊

## Check out the video!

https://user-images.githubusercontent.com/32881355/144337381-2c38d27d-9118-497e-a664-5d0433fedca7.mp4

# Installation

- Clone the repository
  ` git clone https://github.com/SmayanaReddy/auto_anki
- Install all requirements
  ` pip install -r requirements.txt`
- Install project as Python package
  ` pip install .`
- Clone Anki library
  ` git clone https://github.com/kerrickstaley/genanki; cd genanki`
- Install Anki library
  ` python setup.py install`

## Code Documentation

Documentation of the entire codebase is generated using [Pycco](https://github.com/pycco-docs/pycco).
You can find the documentation [here](https://github.com/SmayanaReddy/auto_anki/tree/main/docs).

If you are a developer, and want to update documentation:

- Install Pycco
  `pip install pycco`
- Use Pycco to generate docs.
  `pycco auto_anki/**/*.py -p`

## Code Coverage

For checking code coverage,

- Install Coverage (https://pypi.org/project/coverage/)
  `pip install coverage`
- For generating the report run
  `coverage run user_cli.py`
- For viewing the report run
  `coverage report`


| Name              | Stmts | Miss | Cover |
| ------------------- | ------- | ------ | ------- |
| anki.py           | 14    | 3    | 83%   |
| extract_sizes.py  | 55    | 6    | 89%   |
| google_search.py  | 13    | 2    | 87%   |
| user_cli.py       | 53    | 7    | 87%   |
| wordprocessing.py | 125   | 23   | 81%   |
| TOTAL             | 260   | 57   | 85%   |

## How to Contribute

We would be happy to receive contributions! If you'd like to, please go through our [CONTRIBUTING.md](https://github.com/SmayanaReddy/auto_anki/blob/main/CONTRIBUTING.md).

For any feedback, issues, or bug reports, please create an issue [here](https://github.com/SmayanaReddy/auto_anki/issues/new).

## Future RoadMap

#### Build a browser extension with the current functionality

- A browser extension which will extract contents of the current webpage which the user is on and produce a new deck of anki cards based on the material.

#### Improve word extraction logic

- Currently Spacy is being used to extract noun phrases from each slide/page of the document. Then the high frequency noun phrases are calculated and used in the final search query. However this causes an issue when every slide has the document’s author name and email address listed. The author name is considered as a noun phrase, and since it appears on every slide has a high frequency, and thus appears on the final search query.

## Contributors

* Keith Tran (ktran24@ncsu.edu)
* Benyamin Tabarsi(btaghiz@ncsu.edu)
* Kimia Fazeli(kfazeli@ncsu.edu)
* Muhammed Faizan (mfaizan@ncsu.edu)

## Acknowledgements

We have built this code on top of the stack from the project [
](https://github.com/SmayanaReddy/auto_anki)https://github.com/SmayanaReddy/auto_anki
