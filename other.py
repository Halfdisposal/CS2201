doc1 = "Information Retrieval is the science of search engines"
doc2 = "This is the age of information technology"
doc3 = "Mathematics in the language of science"
doc4 = "Efficient retrieval of important data is the feature of any sound search system."
doc5 = "Gerard Salton is the father of Information Retrieval"

def preprocess(doc):
    doc = doc.lower()
    words = doc.split()
    retwords = []
    stop = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    for word in words:
        if word not in stop:
            retwords.append(word)
    return retwords

docs = [doc1, doc2, doc3, doc4, doc5]
prepdocs = list(map(preprocess, docs))
q = "Information Retrieval"
query = preprocess(q)
for doc in prepdocs:
    if any(word in query for word in doc):
        print(doc)
print('-'*50)
for doc in prepdocs:
    if all(word in query for word in doc):
        print(doc)


counts = {}
for doc in prepdocs:
    match_list = [word for word in query if word in doc]
    idx = 'doc' + str(prepdocs.index(doc) + 1)
    if idx not in counts:
        counts[idx] = len(match_list)

print(counts)
print(sorted(counts, key = counts.get, reverse=True))
