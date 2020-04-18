bagOfWords = input().split( sep=' ' )
#print(bagOfWords)

#newBagOfWords = []
i = 1
final_words         = []
final_words_indices = []
while(i < len(bagOfWords)):
    #newBagOfWords.append(''.join((filter(str.isalnum, bagOfWords[i]))))
    if(bagOfWords[i][0].isupper() == True):
        final_words.append(''.join((filter(str.isalnum, bagOfWords[i]))))
        final_words_indices.append(i)
    if('.' in bagOfWords[i]):
        #print(bagOfWords[i])
        i += 1
    i += 1

#print(newBagOfWords)
if(len(final_words) == 0):
    print('None')
else:
    for i in range(len(final_words)):
        print(final_words_indices[i]+1, ':', final_words[i], sep='')