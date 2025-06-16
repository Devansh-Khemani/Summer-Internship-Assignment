def solve(s):
    name=s.split(' ')
    for i in range(0,len(name)):
        if name[i] and name[i][0].islower():
            name[i] = name[i][0].upper()+name[i][1::]
    ans=''
    for i in name:
        ans = ans+i+' '
    return ans
