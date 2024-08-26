def count_words(book_contents):
    book_contents=book_contents.split()
    no_words=len(book_contents)
    print(str(no_words)+" are in the given document")

def count_character(book_contents):
    book_contents=book_contents.lower()
    collect={}
    for i in book_contents:
        if i.isalpha()==True:
            if i in collect:
                collect[i]+=1
            else:
                collect[i]=1
        else:
            pass
    for keys,values in collect.items():
        print("The "+str(keys)+" is found "+str(values)+" times")

def count_every_words(book_contents):
    book_contents=book_contents.lower()
    book_contents=book_contents.split()
    book_contents=list(book_contents)
    collect={}
    for i in book_contents:
        if i.isalpha()==True:
            if i in collect:
                collect[i]+=1
            else:
                collect[i]=1
        else:
            pass
    print(collect)


with open("books\Frankenstein.txt") as f:
    book_contents=f.read()
    count_words(book_contents)
    count_character(book_contents)
    count_every_words(book_contents)