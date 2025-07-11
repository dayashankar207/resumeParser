import fitz
import spacy

nlp=spacy.load('en_core_web_sm')

def parse_resume_text(file_bytes: bytes)->dict:
    #Extract raw text from pdf
    doc=fitz.open(stream=file_bytes,filetype='pdf')
    text= "".join([page.get_text() for page in doc])

    #Run spacy NLP pipeline
    parsed_doc=nlp(text)

    #Extract entities or keywords
    skills=[]
    for token in parsed_doc:
        if token.pos_ in ["NOUN","PROPN"] and not token.is_stop:
            skills.append(token.lemma_.lower())

    return {
        "text":text,
        "skills":list(set(skills))
    }
