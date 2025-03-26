def mergeAlternately(word1, word2):
    if not word1:
        return word2
    if not word2:
        return word1
    
    merged=''
    len1=len(word1)
    len2=len(word2)
    minlen=min(len1,len2)

    if len1==len2:
        for i in range(minlen):
            merged += word1[i] + word2[i]
        return merged

    for i in range(minlen):
        merged += word1[i] + word2[i]

    if len1>len2:
        merged += word1[minlen:]

    elif len2>len1:
        merged += word2[minlen:]
    return merged

str1=input('Enter word 1:\n')
str2=input('Enter word 2:\n')

print(mergeAlternately(str1,str2))
