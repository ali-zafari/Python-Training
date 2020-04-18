numOfLines = int(input())

dictionary = {}

for i in range(numOfLines):
    input_sequence = input().split()
    target_word = input_sequence[0]
    for i in range(3):
        dictionary[input_sequence[i+1]] = target_word
#print(dictionary)

sentence = input()
translated = list(map(lambda x: dictionary[x] if(x in dictionary.keys()) else x, sentence.split()))
print(' '.join(word for word in translated))