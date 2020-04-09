'''
word = input('단어를 입력하세요:')

is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1 -i]:
        is_palindrome = False
        break
print(is_palindrome)
print(word == word[::-1])
print(list(word) == list(reversed(word)))
print(word == ''.join((reversed(word))))
'''
text = 'Hello'

for i in range(len(text) - 1):
    print(text[i], text[i + 1], sep = '')

text = 'this is python script'
words = text.split()
for i in range(len(words) - 1):
    print(words[i], words[i + 1])

text = 'hello'

two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep = '')

two_gram = [text[i:] for i in range(3)]
print(two_gram)

two_gram = list(zip(*[text[i:] for i in range(3)]))
print(two_gram)

with open('words.txt', 'r') as file:
    lines = file.read().split()
    for line in lines:
        if line == line[::-1]:
            print(line)