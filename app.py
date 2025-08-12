s='the book is red'
L = list(s)
print("L=", L)
# HW1_2: write a function for reversing a part of the list
def reverse_range(L, start, finish):
  while start < finish:
    L[start], L[finish] = L[finish], L[start]
    start = start + 1
    finish = finish - 1

L_test=['t', 'h', 'e', ' ', 'b', 'o', 'o', 'k', ' ', 'i', 's', ' ', 'r', 'e', 'd']
reverse_range(L_test, 4, 7)
print(L_test)


def reverse_words(L):
  n = len(L)

  # Step 1: Reverse the entire list
  reverse_range(L, 0, n - 1)

  # Step 2: Reverse each word
  start = 0
  while start < n:
    if L[start] == ' ':
      start += 1
      continue
    finish = start
    while finish < n and L[finish] != ' ':
      finish += 1
    reverse_range(L, start, finish - 1)
    start = finish
# test
reverse_words(L)

print(L)


def reverse_words_str(s):
  return " ".join(reversed(s.split()))

# test:
s1=reverse_words_str(s)
print(s1)
# expected output is:
# red is book the
