import re
from nltk.corpus import stopwords

NAME_PATTERN      = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]


# Education (Upper Case Mandatory)
EDUCATION   = ['BE','B.E.', 'B.E', 'BS', 'B.SC','C.A.','C.A.','B.COM','B. COM','M. COM', 'M.COM','M. COM .',
            'ME', 'M.E', 'M.E.', 'MS', 'M.S', 'HONORS', 'COMPUTER SCIENCE'
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
            'PHD', 'PHD', 'PH.D', 'PH.D.','MBA','MBA', 'POST-GRADUATE','5 YEAR INTEGRATED MASTERS','MASTERS',
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
        ]

PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')

NOT_ALPHA_NUMERIC = r'[^a-zA-Z\d]'

NUMBER            = r'\d+'


# For finding date ranges
MONTHS_SHORT      = r'(jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)|(aug)|(sep)|(oct)|(nov)|(dec)'
MONTHS_LONG       = r'(january)|(february)|(march)|(april)|(may)|(june)|(july)|(august)|(september)|(october)|(november)|(december)'
MONTH             = r'(' + MONTHS_SHORT + r'|' + MONTHS_LONG + r')'
YEAR              = r'(((20|19)(\d{2})))'

STOPWORDS         = set(stopwords.words('english'))

RESUME_SECTIONS = [
                    'accomplishments',
                    'experience',
                    'education',
                    'interests',
                    'projects',
                    'professional experience',
                    'publications',
                    'skills',
                ]