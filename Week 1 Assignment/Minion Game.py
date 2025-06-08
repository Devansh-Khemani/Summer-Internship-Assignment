def minion_game(string):
    vowels = ['A','E','I','O','U']
    Stuart=0
    Kevin=0
    for i in range(0,len(string)):
        if string[i] not in vowels:
            Stuart+=len(string)-i
        else:
            Kevin+=len(string)-i
    if Stuart>Kevin:
        return 'Stuart '+str(Stuart)
    else:
        return 'Kevin '+str(Kevin)
print(minion_game('BANANA'))
