'''
AUTHOR:KRISTAL SHRESTHA
DATE:6/4/2024
PURPOSE:LEARNING PYTHON SIMPLE SEARCHENGINE CONCEPT
'''


def matchingWords(sentence1,sentence2): #here sentence1 is a querty string,the string that we search 
    words1=sentence1.strip().split(" ")
    words2=sentence2.strip().split(" ")
    score=0 #to count the total matching words with query sentence

    for word1 in words1:
        for word2 in words2:
            if(word1.lower()==word2.lower()):#for case insensitiveness
                 #however this search has limitation,it will count again for duplication
                score+=1
    return score

if __name__=="__main__":
    Sentences = ["Python is cool", "python is good", "python is not python snake"]

    query=input("enter the query string: ")
    #query string is something you want to search

    score_sentences=[matchingWords(query,sentence) for sentence in Sentences]
    #it will return a list of scores corresponding to member of Sentences
    #for above example [1,1,2] if you search python
    # print(score_sentences)
    
    sorted_score_sentences=[sorted_score
    for sorted_score in sorted(zip(score_sentences,Sentences),reverse=True)
    if sorted_score[0]!=0
    ]
    #here zip works like this
    #a=[1,2,3,4]
    #b=[a,b,c,d]
    #then zip(a,b)=[(1,a),(2,b),(3,c),(4,d)] i.e creates list of tuple of 1st-1st member ,2nd-2nd member and so on
    #sorted will sort the list based on the first member by default
    #reverse will reverse the sorted order of list,last member becomes first,secondlast member becomes second and so on
    #thus we got the most searches matched sentences on first then second matches on second and so on
    #sorted_score[0]!=0 case will handle the zero matched sentences,it wont include such sentences on the sorted_score_sentences

    #print(sorted_score_sentences)

    print(f"{len(sorted_score_sentences)} results found!")
    # 5 results found ! - to get this type of message

    for score,item in sorted_score_sentences:
        print(f"\"{item}\": with a matching score of {score}")

# \"{}\" to use double quotation inside fstring use \" \"


