from pyignite import Client
from threading import Thread
import random


#establish connection
client = Client()
client.connect('34.72.162.100', 10800)

try:
    client_cache = client.create_cache("client_cache")
except:
    client_cache.destroy()

def read_file(file_name):
    with open(file_name,'r',encoding="utf8") as f:
        for line in f:
            for word in line.split():
                client_cache.put(word,random.randint(0,500))


def search_word(file_name):
    with open(file_name,'r',encoding="utf8") as f:
        for line in f:
            for word in line.split():
                try:
                    client_cache.get(word)
                    print("Achou" + word)
                except:
                    print("Nao achou" + word)
                
                

                
reader_one = Thread(target=read_file,args=['txt-biblia.txt'])
reader_two = Thread(target=read_file,args=['txt-hp1.txt'])
reader_three = Thread(target=read_file,args=['txt-hp2.txt'])
reader_four = Thread(target=read_file,args=['txt-hp3.txt'])
reader_five = Thread(target=read_file,args=['txt-hp4.txt'])

searcher_one = Thread(target=search_word,args=['txt-hp5.txt'])


reader_one.start()
reader_two.start()
reader_three.start()
reader_four.start()
reader_five.start()

searcher_one.start()

client_cache.destroy()
'''
testim = client.create_cache("testim")

for x in range(10000000):
    print(x)
    testim.put(x,"hmmm coxa de frango")
    

for x in range(10000000):
    value = testim.get(x)
    print(value)

testim.destroy()
'''