def to_Thai(n):
    ans =''
    n = str(n)
    w = {'1':'et','2':'song','3':'sam','4':'si','5':'ha','6':'hok','7':'chet','8':'paet','9':'kao','0':'soon'}
    N = len(n)
    if N == 1:
        if n == '1':
            ans += 'neung'
        else:  
            ans += w[n[-1]]
    elif N == 2:
        if n[-2] == '1':
            if n[-1] == '0':
                ans += 'sip'
            else:
                ans += 'sip'+' '+w[n[-1]]
        elif n[-2] == '2':
            if n[-1] == '0':
                ans += 'yi'+' '+'sip'
            else:
                ans += 'yi'+' '+'sip'+' '+w[n[-1]] 
        else:
            if n[-1] == '0':
                ans += w[n[-2]]+' '+'sip'
            else:
                ans += w[n[-2]]+' '+'sip'+' '+w[n[-1]]
    elif N == 3:
        if n[-3] == '1':
            ans += 'neung'+' '+'roi'+' '
            if n[-2] == '0':
                if n[-1] == '0':
                    pass
                else:
                    ans += w[n[-1]]
            elif n[-2] == '1':
                if n[-1] == '0':
                    ans += 'sip'
                else:
                    ans += 'sip'+' '+w[n[-1]]         
            elif n[-2] == '2':
                if n[-1] == '0':
                    ans += 'yi'+' '+'sip'
                else:
                    ans += 'yi'+' '+'sip'+' '+w[n[-1]]         
            else:
                if n[-1] == '0':
                    ans += w[n[-2]]+' '+'sip'
                else:
                    ans += w[n[-2]]+' '+'sip'+' '+w[n[-1]]                
        else:
            ans += w[n[-3]]+' '+'roi'+' '
            if n[-2] == '0':
                if n[-1] == '0':
                    pass
                else:
                    ans += w[n[-1]]
            elif n[-2] == '1':
                if n[-1] == '0':
                    ans += 'sip'
                else:
                    ans += 'sip'+' '+w[n[-1]]         
            elif n[-2] == '2':
                if n[-1] == '0':
                    ans += 'yi'+' '+'sip'
                else:
                    ans += 'yi'+' '+'sip'+' '+w[n[-1]]         
            else:
                if n[-1] == '0':
                    ans += w[n[-2]]+' '+'sip'
                else:
                    ans += w[n[-2]]+' '+'sip'+' '+w[n[-1]]
    elif N == 4:
        if n[-4] == '1':
            ans += 'neung'+' '+'pan'+' '
            if n[-3] == '0':
                if n[-2] == '0':
                    if n[-1] == '0':
                        pass
                    else:
                        ans += w[n[-1]]
                elif n[-2] == '1':
                    if n[-1] == '0':
                        ans += 'sip'
                    else:
                        ans += 'sip'+' '+w[n[-1]]         
                elif n[-2] == '2':
                    if n[-1] == '0':
                        ans += 'yi'+' '+'sip'
                    else:
                        ans += 'yi'+' '+'sip'+' '+w[n[-1]]         
                else:
                    if n[-1] == '0':
                        ans += w[n[-2]]+' '+'sip'
                    else:
                        ans += w[n[-2]]+' '+'sip'+' '+w[n[-1]]
                
            elif n[-3] == '1':
                ans += 'neung'+' '+'roi'+' '
                if n[-2] == '0':
                    if n[-1] == '0':
                        pass
                    else:
                        ans += w[n[-1]]
                elif n[-2] == '1':
                    if n[-1] == '0':
                        ans += 'sip'
                    else:
                        ans += 'sip'+' '+w[n[-1]]         
                elif n[-2] == '2':
                    if n[-1] == '0':
                        ans += 'yi'+' '+'sip'
                    else:
                        ans += 'yi'+' '+'sip'+' '+w[n[-1]]         
                else:
                    if n[-1] == '0':
                        ans += w[n[-2]]+' '+'sip'
                    else:
                        ans += w[n[-2]]+' '+'sip'+' '+w[n[-1]]                
            else:
                ans += w[n[-3]]+' '+'roi'+' '
                if n[-2] == '0':
                    if n[-1] == '0':
                        pass
                    else:
                        ans += w[n[-1]]
                elif n[-2] == '1':
                    if n[-1] == '0':
                        ans += 'sip'
                    else:
                        ans += 'sip'+' '+w[n[-1]]         
                elif n[-2] == '2':
                    if n[-1] == '0':
                        ans += 'yi'+' '+'sip'
                    else:
                        ans += 'yi'+' '+'sip'+' '+w[n[-1]]         
                else:
                    if n[-1] == '0':
                        ans += w[n[-2]]+' '+'sip'
                    else:
                        ans += w[n[-2]]+' '+'sip'+' '+w[n[-1]]
        else:
            ans += w[n[-4]]+' '+'pan'+' '
            if n[-3] == '0':
                if n[-2] == '0':
                    if n[-1] == '0':
                        pass
                    else:
                        ans += w[n[-1]]
                elif n[-2] == '1':
                    if n[-1] == '0':
                        ans += 'sip'
                    else:
                        ans += 'sip'+' '+w[n[-1]]         
                elif n[-2] == '2':
                    if n[-1] == '0':
                        ans += 'yi'+' '+'sip'
                    else:
                        ans += 'yi'+' '+'sip'+' '+w[n[-1]]         
                else:
                    if n[-1] == '0':
                        ans += w[n[-2]]+' '+'sip'
                    else:
                        ans += w[n[-2]]+' '+'sip'+' '+w[n[-1]]
                
            elif n[-3] == '1':
                ans += 'neung'+' '+'roi'+' '
                if n[-2] == '0':
                    if n[-1] == '0':
                        pass
                    else:
                        ans += w[n[-1]]
                elif n[-2] == '1':
                    if n[-1] == '0':
                        ans += 'sip'
                    else:
                        ans += 'sip'+' '+w[n[-1]]         
                elif n[-2] == '2':
                    if n[-1] == '0':
                        ans += 'yi'+' '+'sip'
                    else:
                        ans += 'yi'+' '+'sip'+' '+w[n[-1]]         
                else:
                    if n[-1] == '0':
                        ans += w[n[-2]]+' '+'sip'
                    else:
                        ans += w[n[-2]]+' '+'sip'+' '+w[n[-1]]                
            else:
                ans += w[n[-3]]+' '+'roi'+' '
                if n[-2] == '0':
                    if n[-1] == '0':
                        pass
                    else:
                        ans += w[n[-1]]
                elif n[-2] == '1':
                    if n[-1] == '0':
                        ans += 'sip'
                    else:
                        ans += 'sip'+' '+w[n[-1]]         
                elif n[-2] == '2':
                    if n[-1] == '0':
                        ans += 'yi'+' '+'sip'
                    else:
                        ans += 'yi'+' '+'sip'+' '+w[n[-1]]         
                else:
                    if n[-1] == '0':
                        ans += w[n[-2]]+' '+'sip'
                    else:
                        ans += w[n[-2]]+' '+'sip'+' '+w[n[-1]]

    return ans.strip()
exec(input().strip()) 