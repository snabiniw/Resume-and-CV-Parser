import os
import utils
import spacy
import pprint
from spacy.matcher import Matcher
import multiprocessing as mp

class ResumeParser(object):
    def __init__(self, resume):
        nlp = spacy.load('en_core_web_sm')
        self.__matcher = Matcher(nlp.vocab)
        self.__details = {
            'name'                 : None,
            'email'                : None,
            'mobile_number'        : None,
            'technical_skills'     : None,
            'soft_skills'          : None,
            'education'            : None,
            'nationality'          : None,
            # 'address'              : None,
            'languages'            : None,
            'experience'           : None,
        }
        self.__resume      = resume
        self.__text        = utils.extract_text(self.__resume, os.path.splitext(self.__resume)[1])
        self.__text        = ' '.join(self.__text.split())
        self.__nlp         = nlp(self.__text)
        self.__noun_chunks = list(self.__nlp.noun_chunks)
        self.__get_basic_details()

    def get_extracted_data(self):
        return self.__details

    def __get_basic_details(self):
        name                 = utils.extract_name(self.__nlp, matcher=self.__matcher)
        email                = utils.extract_email(self.__text)
        mobile               = utils.extract_mobile_number(self.__text)
        technical_skills     = utils.extract_skills(self.__nlp, self.__noun_chunks)
        soft_skills          = utils.extract_non_technical_skills(self.__nlp, self.__noun_chunks)
        edu                  = utils.extract_education([sent.string.strip() for sent in self.__nlp.sents])
        nationality          = utils.extract_nationality(self.__nlp, self.__noun_chunks)
        languages            = utils.extract_languages(self.__nlp, self.__noun_chunks)
        #               = utils.extract_address(self.__text)
        experience           = utils.extract_experience(self.__text)
        
        self.__details['name']             = name
        self.__details['email']            = email
        self.__details['mobile_number']    = mobile
        self.__details['technical_skills'] = technical_skills
        self.__details['soft_skills']      = soft_skills
        self.__details['education']        = edu
        self.__details['nationality']      = nationality
        self.__details['languages']        = languages
        # self.__details['address'] = address
        self.__details['experience']       = experience
        return

def resume_result_wrapper(resume):
        parser = ResumeParser(resume)
        return parser.get_extracted_data()

if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())

    # resumes = ['./input_data/CV-Sunil-Ghimire.pdf', './input_data/1.pdf', './input_data/2.docx', './input_data/3.pdf', './input_data/4.pdf',
    # './input_data/5.pdf', './input_data/6.pdf', './input_data/7.pdf', './input_data/8.pdf', 
    # './input_data/9.pdf', './input_data/10.pdf']
    resumes = ['./input_data/CV-Sunil-Ghimire.pdf']
    data = []
    for root, directories, filenames in os.walk('resumes'):
        for filename in filenames:
            file = os.path.join(root, filename)
            resumes.append(file)

    results = [pool.apply_async(resume_result_wrapper, args=(x,)) for x in resumes]

    results = [p.get() for p in results]

    pprint.pprint(results)

