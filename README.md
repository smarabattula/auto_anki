# Auto Anki

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![CodeCov](https://img.shields.io/badge/Codecov-F01F7A?style=for-the-badge&logo=Codecov&logoColor=white)
![GHActions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

![Build Status](https://img.shields.io/badge/build-passing-green)
[![DOI](https://zenodo.org/badge/713026474.svg)](https://zenodo.org/doi/10.5281/zenodo.10211336)
[![codecov](https://codecov.io/gh/smarabattula/auto_anki/graph/badge.svg)](https://codecov.io/gh/smarabattula/auto_anki)<br>
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![GitHub license](https://img.shields.io/github/license/smarabattula/auto_anki)](https://github.com/smarabattula/auto_anki/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/smarabattula/auto_anki)](https://github.com/smarabattula/auto_anki/issues)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/smarabattula/auto_anki)](https://github.com/smarabattula/auto_anki/issues?q=is%3Aissue+is%3Aclosed)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/smarabattula/auto_anki/pulls)
![version](https://img.shields.io/badge/version-3.0-blue)
![Test Cases](https://img.shields.io/badge/tests-passing-green)
![Test Cases](https://img.shields.io/badge/test%20cases-20-green)



## [Click here to see Auto Anki's Demo video](https://youtu.be/hLsI2FBElr0)

<!-- TABLE OF CONTENTS -->

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#why-should-you-use-auto-anki">Why should you use Auto Anki?</a></li>
    <li><a href="#check-out-the-video">Check out the video!</a></li>
    <li><a href="#Sucessful-usecases">Sucessful usecases</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#docker-deployment">Docker Deployment</a></li>
    <li><a href="#code-documentation">Code Documentation</a></li>
    <li><a href="#how-to-contribute">How to Contribute</a></li>
    <li><a href="#future-roadmap">Future RoadMap</a></li>
   <li><a href="#contributors">Contact us(Contributors)</a></li>
    <li><a href="#Funding">Project's Funding</a></li>
   <li><a href="#acknowledgements">Acknowledgements</a></li>
   <li><a href="#Recommended-citation">Recommended citation</a></li>
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

## Quick Start
Install Auto-Anki with ChatGPT, provide your study lectures or documents, and your APKG file will be ready! You can import it into the Anki application and dive into your materials. It's quick and easy peasy!

Here's a series of pictures to demonstrate the features we've added and how to use them:

### First Feature: Enhanced User Interface
We've revamped the user interface and introduced a convenient drop-down menu, this was not available in the previous version. Also we improved overall appereance.

<img src="https://github.com/tran4code/auto_anki/assets/113017516/0f8d4620-e795-473e-ae37-15840db64b6e" width="400" />

### Second Feature: ChatGPT Integration
To provide more accurate answers, we integrated the ChatGPT API. Now, users can generate highly precise flashcards with Auto-Anki powered by ChatGPT. In the previous version they could only use google(people aslo asked answers) to generate flash cards.


When you run Auto-Anki, you'll be greeted by this user-friendly interface where you can choose between Google or ChatGPT to generate your flashcards.

<img src="https://github.com/tran4code/auto_anki/assets/113017516/ca20b1dd-9972-4af1-a883-a665f321b9b6" width="400" />

<img src="https://github.com/tran4code/auto_anki/assets/113017516/ad87793c-fa1e-49f5-ab44-e0ee4bd871d1" width="400" />

Here, you can upload your document:

<img src="https://github.com/tran4code/auto_anki/assets/113017516/bc38ce0a-c838-49f5-b125-57c9b46a8365" width="400" />

It produces an APKG file, and with the Anki application, you can open it and enjoy a new and enhanced studying experience.

<img src="https://github.com/tran4code/auto_anki/assets/113017516/a388c8f0-a4a6-486a-8495-d3f49be9042b" width="400" />

## Check out the video!

https://github.com/tran4code/auto_anki/assets/113017516/ab847e56-d290-4faf-9db6-d9967bc955d3

# Successful usecases

🎉️ Case study : Kimia

Background: Student majoring in Computer Science

Scenario:

* Kimia was struggling with managing large amounts of information from complex textbooks.
* Kimia started using Auto-Anki with ChatGPT to extract key content from PDF textbooks and create flashcards automatically.
* Result: Kimia noticed a significant improvement in her ability to absorb and retain information. Kimia achieved a good grade in her Software Engineering midterm exam and now has more free time for other activities.

🎉️ Case Study: Language Learning

User: Mohammed

Background: Language Enthusiast

Scenario:

* Mohammed was passionate about learning new languages and wanted to create flashcards to improve his vocabulary.
* He used Auto-Anki with ChatGPT to extract phrases and sentences from Spanish language textbooks and websites.
* Result: Mohammed  could expand his vocabulary and language skills in only 2 weeks that he has used Auto-Anki, making his conversations more fluent and enjoyable.

# Installation

1. Clone the repository
`git clone https://github.com/smarabattula/auto_anki`
2. Set up a virtual environment (Optional, but highly recommended):
    - Create the virtual environment:
    ``python -m venv myenv``
    -  Activate the virtual environment: ``source myenv/bin/activate``(for MacOS) and ``source myenv/Scripts/activate`` (for Windows).
    - **Note**: In future runs, you won't need to create the virtual environment again, just activate it.
3. Install all required packages:
  `pip install -r requirements.txt`
4. Download a required model:
  `python -m spacy download en_core_web_lg`
5. Add the Anki library as submodule in your project folder
  `git submodule add https://github.com/kerrickstaley/genanki genanki`
6. Navigate into the cloned directory and Install the Anki library:
  `cd genanki;  python setup.py install`
7. Navigate to Project folder again The command to run the project is:
 `python3 code/ui.py`
8. Install the project as a Python package(Optional):
  `pip install .`

# Docker Deployment

1. Create Docker Account (`https://www.docker.com/`)

2. Install Docker Dektop (`https://www.docker.com/products/docker-desktop/`)

3. In Search bar at top of docker desktop application search for `auto_anki`

4. Pull `msills23/auto_anki` image

5. Click the run action on the image

6. Expand the optional settings and enter `5000` for the port number

7. Run the new container

8. Go to containers tab and click on the square with an arrow through it to the right of the port numbers

This will open the GUI in your web browser

## Code Documentation

Documentation of the entire codebase is generated using [Pycco](https://github.com/pycco-docs/pycco).
You can find the documentation [here](https://github.com/tran4code/auto_anki/tree/main/docs).

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
  `cd code`
  `python -m coverage run -m unittest discover`
- For viewing the report run
  `python -m coverage report`


| Name              | Stmts | Miss | Cover |
| ----------------- | ----- | ---- | ----- |
| anki.py           | 17    | 1    | 94%   |
| extract_sizes.py  | 49    | 16   | 67%   |
| user_cli.py       | 34    | 2    | 94%   |
| wordprocessing.py | 125   | 4    | 97%   |
| TOTAL             | 238   | 23   | 90%   |

## How to Contribute

We would be happy to receive contributions! If you'd like to, please go through our [CONTRIBUTING.md](https://github.com/tran4code/auto_anki/blob/main/CONTRIBUTING.md).

For any feedback, issues, or bug reports, please create an issue [here](https://github.com/tran4code/auto_anki/issues/new).

## Future RoadMap

#### Build a browser extension with the current functionality

- A browser extension which will extract contents of the current webpage which the user is on and produce a new deck of anki cards based on the material.

#### Improve word extraction logic

- Currently Spacy is being used to extract noun phrases from each slide/page of the document. Then the high frequency noun phrases are calculated and used in the final search query. However this causes an issue when every slide has the document’s author name and email address listed. The author name is considered as a noun phrase, and since it appears on every slide has a high frequency, and thus appears on the final search query.


## Contact us(Contributors):

We are here to support you. Feel free to email us with any question or bug reports. We try our best to reply as soon as possible.

* Sasank Marabattula (smaraba@ncsu.edu)
* Varun Deepak Gudhe (vgudhe@ncsu.edu)
* MatthewSills (msills@ncsu.edu)

## Project's funding

Our project is currently not funded, and we operate on a volunteer and open-source basis , and currently,improvement of the project solely relies on the dedication of our team and contributions from the open-source community.

## Acknowledgements

We have built this code on top of the stack from the project [
](https://github.com/tran4code/auto_anki)https://github.com/tran4code/auto_anki

## Recommended citation

You can cite us like this:

Auto-Anki with ChatGPT. Version 1.0. Keith Tran,Benyamin Tabarsi, Kimia Fazeli, Mohammed Fazian. 2023. [https://github.com/tran4code/auto_anki]
