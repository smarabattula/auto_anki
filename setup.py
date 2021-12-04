from setuptools import setup, find_packages

setup(
    name='LectureAid',
    version='1.0.0',
    packages=find_packages(),
    description='Upload lecture PDFs and get relevant URLs to helpful websites',
    tests_require=['pytest'],
    author='CSC510 - Group 21',
    author_email='lectureaidnscu@gmail.com',
    url='https://github.com/SmayanaReddy/auto_anki/',
    python_requires='>=3.7',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Topic :: LectureAid",
    ],
    license='MIT',
    install_requires=[
        'google-api-python-client',
        'people_also_ask',
        'spacy==3.1.2',
        'spacy-legacy==3.0.8',
        'en-core-web-lg @ https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-3.1.0/en_core_web_lg-3.1.0-py3-none-any.whl',
        'pyfiglet',
        'PyMuPDF'

    ]
)
