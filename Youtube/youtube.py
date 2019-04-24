import pytube

url=input("Enter the url : ")
r=pytube.YouTube(url)
video=r.streams.first()
video.download('.')
