 def get_repeat_count(data, pattern):
     count = 0
     for i in range(0,len(data)-1):
         if data[i]+data[i+1] == pattern:
             count+=1
             if i+2 <= len(data) and i+3 <= len(data) and count == 1:
                 if data[i+2]+data[i+3] == pattern:continue 
                 else:return 0
     return count