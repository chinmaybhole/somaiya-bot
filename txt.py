from pprint import pprint
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

with open('qts.txt') as f:
        lines = f.readlines()

lines = [i for i in lines if i != '\n']
lemmatizer = WordNetLemmatizer()

def cleaning_sentence(sent):
    sentence_words = word_tokenize(sent)
    sentence_words = [word.lower() for word in sentence_words]
    return sentence_words

def remove_tabs(li):
    new_list = list()
    for i in li:
        if i!='\n':
            new_list.append(i)
    return new_list

def remove_spaces(li):
    li = remove_tabs(li)
    new_list = list()
    for i in li:
        new_list.append(i.replace('\n',''))
    return new_list

def clean(li):
    li = remove_spaces(li)
    new_list = list()
    for i in li:
        if not i.isnumeric():
            new_list.append(i)
    return new_list


# pprint(lines[:10])
def convert_into_lists(li):
    # Seperates the qts and answers 
    li  = clean(lines)
    qts_list = list()
    # ans_list = list()
    idx_list = list()
    for idx,i in enumerate(li):
        if i[-1] == '?':
            qts_list.append(i)
            idx_list.append(idx)
            # ans_list.append('idx')
        # else:
        #     ans_list.append(i)
    qts_list=[cleaning_sentence(i) for i in qts_list]
    return qts_list,idx_list

# def sinc_ans_list(li):
# _,ans_list = convert_into_lists(lines)
# ans = list()
# for i in ans_list:
#     if i == '#':
#             # Find this 



# qts,idx = convert_into_lists(lines)
# print(qts[0])

# with open("ans.txt",'w') as a:
#     for i in ans:
#         a.write(i)
#         # a.close()
# pprint(convert_list[:10])
# pprint(a[:10])
# print(idx) #[0, 2, 4, 6, 11, 28, 42, 50, 53, 57, 71, 77, 80, 82, 84, 86, 102, 105, 112, 115, 125, 127, 129, 132, 134, 136, 138, 140, 142, 144]
# print(qts[0])
# pprint(ans[0:1])
# print(qts[1])
# pprint(ans[1:2])
# print(qts[2])
# pprint(ans[2:3])

# ra = clean(lines)

# print(qts[0])
# pprint(ra[1:2])
# print("####################################")
# print(qts[1])
# pprint(ra[3:4])
# print("####################################")
# print(qts[2])
# pprint(ra[5:6])
# print("####################################")
# print(qts[3])
# pprint(ra[7:11])
# print("####################################")
# print(qts[4])
# pprint(ra[12:28])
# ###########################################")
# print(qts[5])
# pprint(ra[29:42])
# # pprint(len(qts))
# # pprint(ans[:20])

def ans_list(li):
    clean_list = clean(li)
    qts,idx = convert_into_lists(li)
    ans_list = list()

    i = 0
    while i <len(qts):
        # print(i)

        # if not i <=29:
        try:
            ans_list.append(clean_list[(idx[i]+1):idx[i+1]])
            # break
        # print(clean_list[(idx[i]+1):idx[i+1]])
        except:
            pass
        i+=1
        # break
    ans_list.append(['Yes. Every institute form team of 24 students from all branches and this team regularly participating ROBOCON National level robotics competition. KJSIEIT ROBOCON Team bagged, 3rd , 5th ,  8th and 12th All India Rank in Asia Pacific Broadcasting Union in National Robotic Contest, in last 5 years competing with India’s prestigious institutions including IITs & NITs with Top Rank in Mumbai Region.'])
    return ans_list
# i = 0
# while i <=len(qts):
#         # i+=1
#         print(i)
#         i+=1
       
        # break

if __name__=='__main__':
    with open('qts.txt') as f:
        lines = f.readlines()

    lines = [i for i in lines if i != '\n']
    li = clean(lines)
    qts,idx = convert_into_lists(lines)
    ans = ans_list(lines)
    # pprint(li[:10])
    inp = input('> ')
    # print(inp.lower())
    # print(qts[0].lower())
    # print(inp.lower() in qts)
    # print(len(ans))What is industry institute linkage of KJSIEIT?What is industry institute linkage of KJSIEIT?
    print(cleaning_sentence(inp))
    if cleaning_sentence(inp) in qts:
    # if inp in qts:
        print(qts[0])
        # print(inp.lower())
        print(type(inp))
        print(inp)  
        idx= qts.index(cleaning_sentence(inp))
        
        #print('WHen k. j. somaiya institute of engineering and information technology is established?'.lower() =='when k. j. somaiya institute of engineering and information technology is established?'.lower() )
        # print(idx)
        # print(len(ans))
        print(ans[idx])
    else:
        print("Ask correct qts please")
        
# ans,b = ans_list(lines)

# # print(ra[(idx[0]+1):idx[0+1]])
# # print(len(idx))
# print(qts[5])
# print'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(ans[5])
# ans = ans_list(lines)
# qts,idx = convert_into_lists(lines)
# print(len(ans))
# # pprint(ans)
# print(len(qts))
# ans_list(lines)
