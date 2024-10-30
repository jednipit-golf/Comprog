def social_media_data(file_in):
    x = {}
    fn = open(file_in,encoding="utf-8")
    f1 = fn.readline()
    for i in fn:
        a,b,c,d,e,f,g,h,i,j,k,l,m = i.strip().split(',')
        x[a] = [b.strip(),f.strip(),int(g.strip()),int(h.strip()),i.strip(),j.strip()]
    fn.close()
    return x

def is_stopword(word):
    x = {}
    stopword = []
    n = ''
    fn = open('stopwords.txt','r')
    f = fn.readline().split(',')
    for i in f:
        stopword.append(i.strip().lower())
    word = word.strip().lower()
    for i in word:
        if i == "'":
            pass
        else:
            n += i
    if n in stopword:
        return True
    else:
        return False
    fn.close()
def count_words_from_text(word_count_dict, text):
    n= ''
    for i in text.lower():
        if i in '.,:;?()[]"{}-/|_!':
            i += ' '
        elif i in "'":
            i += ' '
        else:
            n += i 
    t = n.split()
    tt = []
    for i in t:
        a = is_stopword(i)
        if a == True:
            pass
        elif a == False:
            tt.append(i)
    for i in tt:
        if i in word_count_dict:
            word_count_dict[i] += 1
        else:
            word_count_dict[i] = 1
    return word_count_dict

def count_words_from_data_dict(data_dict, year, country, platform):
    s = {}
    for i,b in data_dict.items():
        t = b[0]
        p = b[1]
        r = b[2]
        l = b[3]
        c = b[4]
        y = b[5]
        if y == year and c == country and p == platform:
            s = count_words_from_text(s,t)
        elif y == year and c == country and platform == 'all':
            s = count_words_from_text(s,t)
        elif y == year and country == 'all' and p == platform:
            s = count_words_from_text(s,t)
        elif year == 'all' and c == country and p == platform:
            s = count_words_from_text(s,t)
        elif year == 'all' and country == 'all' and p == platform:
            s = count_words_from_text(s,t)
        elif year == 'all' and c == country and platform == 'all':
            s = count_words_from_text(s,t)
        elif y == year and country == 'all' and platform == 'all':
            s = count_words_from_text(s,t)
        elif year == 'all' and country == 'all' and platform == 'all':
            s = count_words_from_text(s,t)
    return s

def top_k_words(word_count_dict, k):
    d = {}
    j = []
    ans = []
    for i,b in word_count_dict.items():
        if b not in d:
            d[b] = [i]
        else:
            d[b] = d[b]+[i]
    kk = sorted(d)[::-1]
    c = 0
    for i in kk:
        s = d[i]
        h = sorted(s)
        for hh in h:
            ans.append(hh)
        c += len(h)
        if c >= k:
            break
    return ans
 
def count_word_summary(file_in, file_out, k, year, country, platform):
    h = social_media_data(file_in)
    o = count_words_from_data_dict(h, year, country, platform)
    z = top_k_words(o, k)
    f = open(file_out, 'w')
    if z == []:
        f.write('No data')
    else:
        for i in z:
            f.write(i+':'+str(o[i]))
            f.write('\n')
    f.close()
#    return z
#h = count_word_summary('social_media_data.csv','summary.txt',3,'2023','Thailand','all')

#n = input().strip()
#ZZ = social_media_data(n)
#aa = is_stopword(n)
#print(aa)
#social_media_data.csv

#a = count_words_from_data_dict("social_media_data.csv",'all','all','all')
#b = count_words_from_data_dict("social_media_data.csv",'2023','USA','Facebook')
#c = count_words_from_data_dict("social_media_data.csv",'all','Thailand','all')
#d = count_words_from_data_dict("social_media_data.csv",'2023','Thailand','all')
#e = count_words_from_data_dict("social_media_data.csv",'2020','Japan','Twitter')
#f = count_words_from_data_dict("social_media_data.csv",'2020','japan','twitter')
#print(a)
#print(b)   
#print(c)   
#print(d)
#print(e)
#print(f)