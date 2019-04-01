from urllib import request
from termcolor import colored
while(True):
    url=input("Enter the url : ")
    url=url.replace("https://","")
    url=url.replace("www.","")
    file_name=url+'.txt'
    url="https://www."+url
    print(colored(url,"green")+'\n')
    try:
        server_res=request.urlopen(url)
        file=open(file_name,'w')
        file.write(url+'\n\n')
        for a,b in server_res.headers.items():
            print(colored(a,"blue")+" = "+colored(b,"green"))
            print('----------------------------------------------')
            file.write(a+' = '+b+'\n')
            file.write("----------------------------------------------\n")
        file.close()
    except:
        print(colored("Error","red"))
