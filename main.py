from pytube import YouTube

link = input("Link: ")
""" Denemek icin https://www.youtube.com/watch?v=dQw4w9WgXcQ kullanabilirsiniz."""
yt = YouTube(link)
ys = yt.streams.get_by_resolution(resolution="360p")

print("İndirilme başladı...")
print(" ")

ys.download(filename="song.mp4")

print(" ")
print("... İndirilme bitti.")