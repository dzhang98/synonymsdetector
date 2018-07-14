import math

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    dot_pd = 0.0
        
    for x in vec1:
        if x in vec2:
            dot_pd += vec1[x]*vec2[x]
    
    norm_pd = norm(vec1)*norm(vec2)
    
    return dot_pd/norm_pd

#---------part 2 functions---------
def euc_similarity(vec1, vec2):
    v_sim = {}
    for x in vec1:
        if x in vec2:
            v_sim[x] = vec1[x]-vec2[x]
    sim = -norm(v_sim)

    return sim
    
def euc_norm_similarity(vec1, vec2):
    v_sim = {}
    for x in vec1:
        if x in vec2:
            v_sim[x] = vec1[x]/norm(vec1)-vec2[x]/norm(vec2)
    sim = -norm(v_sim)

    return sim
    
#----------------------------------
def build_semantic_descriptors(sentences):
    outer_dict = {}
    for sentence in sentences:
        for outer_word in set(sentence):
            if outer_word not in outer_dict:
                outer_dict[outer_word] = {}
            for inner_word in set(sentence):
                if inner_word in outer_dict[outer_word]:
                    outer_dict[outer_word][inner_word] += 1
                elif inner_word != outer_word:
                    outer_dict[outer_word][inner_word] = 1   
    return outer_dict
        

def build_semantic_descriptors_from_files(filenames):
    dict_comb = {}
    
    for file in filenames:
        f = open(file, "r", encoding="latin1")
        text = f.read()

        #lower case
        text = text.lower()
        #separates sentences
        text = text.replace("?", ".")
        text = text.replace("!", ".")
        #ignores punctuations of
        text = text.replace(",", "")
        text = text.replace("-", " ")
        text = text.replace("--", " ")
        text = text.replace(":", "")
        text = text.replace(";", "")

        text = text.split(".")#splits into lists of sentences
        # text = text.split(". ") #splits into lists of sentences
        
        list_txt = []
        for sent in text: #for each sentence
            list_txt.append(sent.split()) 
            
        dict_sd = build_semantic_descriptors(list_txt) #dictionary_semantic_desctriptors
        
        for outer_word in dict_sd:
            if outer_word not in dict_comb.keys():
                dict_comb[outer_word] = dict_sd[outer_word]
            else:#outer_word in dict_comb
                for inner_word in dict_sd[outer_word]:
                    if inner_word not in dict_comb[outer_word].keys():
                        dict_comb[outer_word][inner_word] = dict_sd[outer_word][inner_word]
                    else:
                        dict_comb[outer_word][inner_word] += dict_sd[outer_word][inner_word]
    return dict_comb

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    '''This function takes in a string word, a list of strings choices, and a dictionary semantic_descriptors which is built according to the requirements for build_semantic_descriptors, and returns the element of choices which has the largest semantic similarity to word, with the semantic similarity computed using the data in semantic_descriptors and the similarity function similarity_fn'''
    
    max = -2
    max_i = 0
    
    for i in range(len(choices)):
        if (word not in semantic_descriptors.keys()) or (choices[i] not in semantic_descriptors.keys()):
            sim = -1
        else: 
            vec_word = semantic_descriptors[word]
            vec_choice = semantic_descriptors[choices[i]]
            sim = similarity_fn(vec_word, vec_choice)
        
        if sim>max:
            max = sim
            max_i = i
    
    return choices[max_i]


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    '''This function takes in a string filename which is the name of a file in the same format as test.txt, and returns the percentage (i.e., float between 0.0 and 100.0) of questions on which most_similar_word() guesses the answer correctly using the semantic descriptors stored in semantic_descriptors, using the similarity function similariy_fn'''
    f = open(filename, "r", encoding="latin1")
    text = f.read()
    
    lines = text.split("\n")
    
    total_n = len(lines)
    incorrect_n = 0
    
    for line in lines:
        words = line.split(" ")
        if most_similar_word(words[0], words[2:len(words)+1], semantic_descriptors, similarity_fn)!=words[1]:
            incorrect_n += 1

    # print((total_n-incorrect_n)/total_n)
    return (total_n-incorrect_n)/total_n
            
        
   
if __name__ == "__main__":
     
    filenames = ["novel1.txt","novel2.txt"] 
    sd = build_semantic_descriptors_from_files(filenames)
    
    print(run_similarity_test("test.txt", sd, cosine_similarity))

    
    
    

    
    
    