#Complete YouTube Downloader// Will only Download in 720p or lower resolution depending on Choice and video//


from pytube import YouTube
from colorama import init, Fore

def on_complete(stream, filepath):
	print('download complete')
	print(filepath)

def on_progress(stream, chunk, bytes_remaining):
	progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%'
	print(progress_string)

init()
link = input('Youtube link: ')
video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

# information
print(Fore.RED + f'title:  \033[39m {video_object.title}')
print(Fore.RED + f'length: \033[39m {round(video_object.length / 60,2)} minutes')
print(Fore.RED + f'views:  \033[39m {video_object.views / 1000000} million')
print(Fore.RED + f'author: \033[39m {video_object.author}')

# download
print(
	Fore.RED + 'download:' + 
	Fore.GREEN + '(b)est \033[39m|' + 
	Fore.YELLOW + '(w)orst \033[39m|' + 
	Fore.BLUE + '(a)udio \033[39m| (e)xit')
download_choice = input('choice: ')

# If you have a linter below syntax might be highlighted. But the code still runs and it runs fine.///

match download_choice:
	case 'b':
		video_object.streams.get_highest_resolution().download()
	case 'w':
		video_object.streams.get_lowest_resolution().download()
	case 'a':
		video_object.streams.get_audio_only().download()

#////Some Analysis stuff down here as well as parts of the pytube package that you might want to take a look at////
#/////
#/////

# def on_complete(stream, file_path):
#     print(stream)
#     print(file_path)
# def on_progress(stream, chunk, bytes_remaining):
#     print(100 - (bytes_remaining / stream.file.size * 100))
# video_object = YouTube('https://www.youtube.com/watch?v=Rkr_tVB1Es8', on_complete_callback = on_complete, on_progress_callback = on_progress)
# # video information
# #print(video_object.title)
# #print(f'{video_object.length / 60} minutes')
# #print(video_object.views)
# #print(video_object.author)
# #print(video_object.keywords)

# # video streams
# #for stream in video_object.streams:
# #    print(stream)
# #download
# video_object.streams.get_highest_resolution().download()
#/// Would love to get this working with specific resolutions and those resolutions above 720p//////

