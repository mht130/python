#!/bin/python
from essential_generators import document_generator
import time

gen_text=document_generator.DocumentGenerator().gen_sentence()
print("Test : "+gen_text)
t1=time.time()
text=input("Enter : ")
t2=time.time()
if text.lower()==gen_text.lower():
    print("{:.3f} sec".format(t2-t1))
else:
    print("wrong input")
    
