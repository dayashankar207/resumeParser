# Cosine similarity logic

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_match(resumes: list[str],job_description:str):
    all_docs=resumes+[job_description]
    tfidf=TfidfVectorizer().fit_transform(all_docs)
    similarity_matrix=cosine_similarity(tfidf[-1],tfidf[:-1])
    return similarity_matrix.flatten().tolist()
