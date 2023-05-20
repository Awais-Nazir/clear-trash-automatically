import os
files = os.listdir()
files.remove("main.py")
# print(files)

def CreateFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
def move(folder,files):
    for file in files:
        os.replace(file, f"{folder}/{file}")

CreateFolder("image")
CreateFolder("document")
CreateFolder("video")
CreateFolder("audio")
CreateFolder("other")
CreateFolder("compressed")
CreateFolder("Applications")

imgExts = [".jpg",".jpeg",".png",".svg",".icon",".gif",".ico"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]


docExts = [".txt",".doc",".docx",".ppt",".pptx",".pdf",".xls",".xlsx"]
documents = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


vidExts = [".mp4", ".flv",".mkv",".avi","mpeg"]
vidoes = [file for file in files if os.path.splitext(file)[1].lower() in vidExts]


audExts = [".mp3", ".wav",".wma"]
audios = [file for file in files if os.path.splitext(file)[1].lower() in audExts]


zipExts = [".zip", ".rar",".7zip",".iso"]
zip_files = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]


appExts = [".exe", ".app",".apk",".msi",".dmg"]
app_files = [file for file in files if os.path.splitext(file)[1].lower() in appExts]


others = []
for file in files:
    exts = os.path.splitext(file)[1].lower()
    if (exts not in imgExts) and (exts not in docExts) and (exts not in vidExts) and (exts not in audExts) and (exts not in zipExts) and (exts not in appExts)and os.path.isfile(file):
        others.append(file)
# print(others)

move("video",vidoes)
move("audio",audios)
move("compressed",zip_files)
move("image",images)
move("document",documents)
move("Applications",app_files)
move("other",others)


