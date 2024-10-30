def is_stopword(word):
    k=open('stopwords.txt','r')
    new=k.readline().strip()
    x=new.split(', ')
    if word.lower() in x:
        return True
    else:
        return False
    return x
    k.close()
n = input()
a = is_stopword(n)
print(a)