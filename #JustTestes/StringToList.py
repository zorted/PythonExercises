book = "The Hitchhicker's Guide to  the Galaxy"
booklist = list(book)
print (booklist)
print(booklist[0:3])
print(''.join(booklist[0:3]))
print(''.join(booklist[-6:]))

backwards = booklist[::-1]
print(''.join(backwards))

every_other = booklist[::2]
print(''.join(every_other))
