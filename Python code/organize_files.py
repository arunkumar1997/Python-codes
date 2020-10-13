import os
import shutil
home_path = input('!!Check readme file before running this script!!\n----Enter the folder path----\n')
os.chdir(home_path)
path_to_image = home_path + "Images"
path_to_video =  home_path + "Videos"
path_to_music = home_path + "Musics"
path_to_docs =  home_path +"Docs"
path_to_zip = home_path +"Zips"
path_to_apps = home_path +"Applications"
path_to_others = home_path +"Others"

ldir = os.listdir()
files_ = []
Image = ['jpg', 'png', 'gif', 'webp', 'tiff', 'psd', 'raw',
         'bmp', 'heif', 'indd', 'jpeg', 'svg', 'ai', 'eps']
Video = ['webm', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'ogg', 'mp4',
         'm4p', 'm4v', 'avi', 'wmv', 'mov', 'qt', 'flv', 'swf', 'avchd']
Music = ['m4a', ' flac', 'mp3', 'mp4', 'wav', 'aac']
Document = ['pdf', 'txt', 'docx', 'doc', 'xls',
            'odt', 'xlsx', 'ods', 'ppt', 'pptx', 'html']
zip_file = ['tar', 'gz', 'zip']
Applications = ['deb', 'exe', 'apk', 'apks']

for item in ldir:
    if (os.path.isfile(os.path.join(home_path, item))):
        files_.append(item)
    else:
        pass

for fname in files_:
    f = list(fname.split('.'))
    if (os.path.isfile(os.path.join(home_path, fname))):
        try:
            # image move
            if (any(x in f for x in Image)):
                if (os.path.exists('Images')):
                    shutil.move(os.path.join(home_path, fname), path_to_image)
                else:
                    os.mkdir("Images")
                    shutil.move(os.path.join(home_path, fname), path_to_image)
        # Videos move
            elif (any(x in f for x in Video)):
                if (os.path.exists('Videos')):
                    shutil.move(os.path.join(home_path, fname), path_to_video)
                else:
                    os.mkdir("Videos")
                    shutil.move(os.path.join(home_path, fname), path_to_video)
        # Musics move
            elif (any(x in f for x in Music)):
                if (os.path.exists('Musics')):
                    shutil.move(os.path.join(home_path, fname), path_to_music)
                else:
                    os.mkdir("Musics")
                    shutil.move(os.path.join(home_path, fname), path_to_music)
        # Docs move
            elif (any(x in f for x in Document)):
                if (os.path.exists('Docs')):
                    shutil.move(os.path.join(home_path, fname), path_to_docs)
                else:
                    os.mkdir("Docs")
                    shutil.move(os.path.join(home_path, fname), path_to_docs)
        # Zips move
            elif (any(x in f for x in zip_file)):
                if (os.path.exists('Zips')):
                    shutil.move(os.path.join(home_path, fname), path_to_zip)
                else:
                    os.mkdir("Zips")
                    shutil.move(os.path.join(home_path, fname), path_to_zip)
        # apps move
            elif (any(x in f for x in Applications)):
                if (os.path.exists('Applications')):
                    shutil.move(os.path.join(home_path, fname), path_to_apps)
                else:
                    os.mkdir("Applications")
                    shutil.move(os.path.join(home_path, fname), path_to_apps)
            else:
                if (os.path.exists('Others')):
                    shutil.move(os.path.join(home_path, fname), path_to_others)
                else:
                    os.mkdir("Others")
                    shutil.move(os.path.join(home_path, fname), path_to_others)

        except:
            print('error')
    else:
        pass
print("Done...\n{} files are organized 😄😄. ".format(len(files_))) if (len(files_) > 0) else print(
    'Nothing to organize!!\nFile are already in Organized manner 👍👍.')
