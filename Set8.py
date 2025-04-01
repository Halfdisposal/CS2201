import numpy as np
import matplotlib.pyplot as plt
import math 
import time
import random
import scipy.integrate as sp

def Simpson(f, domain, n):
    N = 2*n 
    a, b = domain 
    integral = f(a) + f(b)
    x, h = np.linspace(a, b, N + 1, retstep=True)
    for x0 in x[1:-1]:
        if (np.where(x==x0)[0][0]) % 2 == 0:
            integral += 2 * f(x0)
        else:
            integral += 4 * f(x0)
    return integral*h/3

def f(x):
    return (25 - x**2)**0.5

def Q3():
    done = False
    rs = []
    throws = []
    throw = 0
    while not done:
        r = random.randint(1, 6)
        throw += 1
        throws.append(throw)
        rs.append(r)
        if r == 6:
            done = True
    plt.plot(throws, rs, 'o-r')
    plt.show()


def preprocess(input_string):
    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    processed_string = input_string.split(" ")
    processed_string = list(map(lambda x: x.lower(), processed_string))
    output_list = np.setdiff1d(processed_string, stopwords)
    return output_list.tolist()

def Q5():
    string = "Information Retrieval is the science of search engines"
    output_list = preprocess(string)
    print(output_list)

def Q67():
    doc1 = "Information Retrieval is the science of search engines"
    doc2 = "This is the age of information technology"
    doc3 = "Mathematics in the language of science" 
    doc4 = "Efficient retrieval of important data is the feature of any sound search system."
    doc5 = "Gerard Salton is the father of Information Retrieval"
    q = "All Information Technology are good"
    new_q = preprocess(q)
    doc_list = [list(map(lambda x: x.lower(), doc1.split(" "))), list(map(lambda x: x.lower(), doc2.split(" "))), list(map(lambda x: x.lower(), doc3.split(" "))), list(map(lambda x: x.lower(), doc4.split(" "))), list(map(lambda x: x.lower(), doc5.split(" "))), ]
    for d in doc_list:
        if any(word in new_q for word in d):
            print(d)
    doc_dict = {'doc1' : 0, 'doc2' : 0, 'doc3' : 0, 'doc4' : 0, 'doc5' : 0}
    for d in doc_list:
        for word in new_q:
            if word in d:
                doc_dict['doc' + str(doc_list.index(d) + 1)] += 1
    sorted_dict = dict(sorted(doc_dict.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict.keys())



def Q8():
    radius_board = 5
    rn = np.random.normal(loc=radius_board, scale=2, size=100)
    bin_width = radius_board/5
    counts = {'bulls_eye' : 0, 'pro' : 0, 'seasoned' : 0, 'improver' : 0, 'beginner' : 0, 'miss' : 0}
    for val in rn:
        if val >= 0 and val < bin_width:
            counts['bulls_eye'] += 1
        elif val >= bin_width and val < 2*bin_width:
            counts['pro'] += 1
        elif val >= 2*bin_width and val < 3*bin_width:
            counts['seasoned'] += 1
        elif val >= 3*bin_width and val < 4*bin_width:
            counts['improver'] += 1
        elif val >= 4*bin_width and val < 5*bin_width:
            counts['beginner'] += 1
        else:
            counts['miss'] += 1
    plt.pie(list(counts.values()), labels=list(counts.keys()))
    plt.show()


def Q9():
    def f6(x):
        return (6**2 - x**2)**0.5
    def f5(x):
        return (5**2 - x**2)**0.5
    integral2 = Simpson(f6, (0, 6), 100)
    integral1 = Simpson(f5, (0, 5), 100)
    net_integral = integral2 - integral1 
    absolute_integral = sp.quad(f6, 0, 6)[0] - sp.quad(f5, 0, 5)[0]
    error = abs(absolute_integral - net_integral)*100/absolute_integral
    print("Simpson integral ", net_integral)
    print("Actual Integral ", absolute_integral)
    print("Percent error ", error)
    

    
