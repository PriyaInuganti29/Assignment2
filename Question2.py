#!/usr/bin/env python
# coding: utf-8

# In[8]:



import re
link=[]
uniqueValueMaxTen = []
def validateLinks(url,n):
    
    status = re.match(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", url)
    
    if status == None:
        raise Exception("Not matching WIKI URL format")
    if(n >=4 or n ==0):
        raise Exception("Only 1 to 3 allowed")
    else:
        if(len(link)==0 or url not in link):
            link.append(url)
        i=1
        while(i<n):
            s = list(set(url))
            if len(s)>10:
                uniqueValueMaxTen.append(s[:10])
                
            i=i+1
   
    return link,uniqueValueMaxTen

# def addLinkToList(url,n):
#     if len(link) == 0:
#         link.append(url)
#     else:
#         validateLinks(url,n)
        
    

link,uniqueValueMaxTen = validateLinks('https://www.geeksforgeeks.org/count-the-number-of-unique-characters-in-a-string-in-python/',2)
print("Links : ",link)
print("Unique 10 char count: ",uniqueValueMaxTen)


# In[ ]:





# In[ ]:




