books = dict()
for _ in range(int(input())):
  book = input()
  if book in books :
    books[book] += 1
  else:
    books[book] = 1


m = max(books.values())
tmp = []
for k, v in books.items():
  if v == m : 
    tmp.append(k)

print(sorted(tmp)[0])