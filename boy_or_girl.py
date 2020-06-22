#https://codeforces.com/problemset/problem/236/A

words=input()
unique_words=''

for word in words:
  if word not in unique_words: unique_words+=word

print('CHAT WITH HER!' if len(unique_words)%2==0 else 'IGNORE HIM!')
