word=input('Enter the word: ')
last,n='',0
for ch in word:
    if ch.isalpha():
        if ch not in ('aeiou'):
            last+=ch
            n+=1
        else:
            break
if last=='':
    print('The pig latin translation is: ',word,'ay', sep='')
else:
    print('The pig latin translation is: ',word[n:],last,'ay', sep='')
