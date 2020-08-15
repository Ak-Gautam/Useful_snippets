print(" This script downloads a particular video from youtube\nThe link has to be specified by the user and the user also has to input the preferred quality from the list of options available.\n")


from pytube import YouTube


url = input("Enter a valid youtube url\n")
obj = YouTube(url)

print("The list of available formats is\n")
for st in obj.streams:
    print(st, "\n")

print("Note that only the videos \"progressive=True\" contains both the video and audio.\n")
print("List of the playable videos available\n")
filters = obj.streams.filter(progressive = True, file_extension = "mp4")
for fil in filters:
    print(fil, "\n")

print("Choose the quality of video from above list and enter. e.g: 480p\n")
qual = input("Enter the video quality choice\n")

print("Current dowmload path is : F:\Akshay Files\YouTube_Vids\n")

filters.get_by_resolution(qual).download(output_path="F:\Akshay Files\YouTube_Vids")