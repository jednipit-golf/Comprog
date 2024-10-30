def social_media_data(file_in):
    file_in = str(file_in)
    f = open(file_in,encoding="utf-8")
    skip = f.readline().strip()
    data = {}
    for e in f:
        Id,t,s,ti,use,p,r,l,c,y,m,d,h = e.split(',')
        data[Id] = [t.strip(),p.strip(),int(r.strip()),int(l.strip()),c.strip(),y.strip()]
    return data