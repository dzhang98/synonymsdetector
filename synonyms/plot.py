import numpy as np
import matplotlib.pyplot as plt
import synonyms
from timeit import default_timer as timer

filenames = ["novel1.txt","novel2.txt"]
y_list = []
y2_list = []
x_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list_txt = []
combined_text = ""
time = 0
for i in range(1, 11):
    for file in filenames:
        start = timer()
        f = open(file, "r", encoding="latin1")
        full_text = f.read() 
        text = full_text[:int(len(full_text)*(0.1*i))]

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
    
        combined_text.append(text)
    final_text = combine_text.split(".")#splits into lists of sentences
        
    #--------------------------------------------------------
    
    for sent in final_text: #for each sentence    
        list_txt.append(sent.split())  
    
    sd = synonyms.build_semantic_descriptors(list_txt)
    end = timer()
    time = end-start
    y = synonyms.run_similarity_test("test.txt", sd, synonyms.cosine_similarity)
    y_list.append(y)
    y2_list.append(time)
    print(y, time)
    
plt.subplot(211)
plt.plot(x_list, y_list)
plt.ylim([0, 100])
plt.xlabel("Percentage of Text Used(%)")
plt.ylabel("Correctness of Similarity Test(%)")
plt.title("Accuracy of Similarity Test")

plt.subplot(212)
plt.plot(x_list, y2_list)
plt.ylim([0, 10])
plt.xlabel("Percentage of Text Used(%)")
plt.ylabel("Running Time(s)")
plt.title("Runtime Plot")

            

