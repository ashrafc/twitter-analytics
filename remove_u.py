import fileinput

fout = open("out.txt", 'a')

for i in fileinput.input("print_tweets.txt"):

   str = i.replace("u\"","\"").replace("u\'","\'")

   print >> fout,str