
# Resume and CV Parser

A simple resume/cv parser used for extracting information from resume/cv

## Features

- Extract Name
- Extract Email
- Extract Mobile Number
- Extract Skills
- Extract Non Soft skills
- Extract Nationality
- Extract Language
- Extract Total Experience
- Extract College Name
- Extract Degree
- Extract Designation
- Extract Company Names
  
## Installation

- You can install this package using

```bash
 pip install pyresparser
```
- For NLP operations we use spacy and nltk. Install them using below commands:
```bash
 # spaCy
python -m spacy download en_core_web_sm

# nltk
python -m nltk.downloader words
python -m nltk.downloader stopwords
```
## Result
```bash
[{'education': [('Honors', '2017')],
  'email': 'sunilghimire64@gmail.com',
  'experience': ['S • Graduate Teaching Assistant Jan'],
  'languages': ['Hindi', 'Nepali', 'English'],
  'mobile_number': '+977 9841070311',
  'name': 'Sunil Ghimire',
  'nationality': ['Nepali'],
  'soft_skills': ['Positive attitude'],
  'technical_skills': ['Supervisor',
                       'Matplotlib',
                       'Python',
                       'Github',
                       'Tensorflow',
                       'Opencv',
                       'C',
                       'Seaborn',
                       'Pandas',
                       'Keras',
                       'Algorithms',
                       'Queries',
                       'Mysql',
                       'Machine learning',
                       'Jupyter',
                       'Nltk',
                       'Pycharm',
                       'Conda',
                       'Numpy']}]
```
