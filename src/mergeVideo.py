from moviepy.editor import *
import os
from natsort import natsorted

def mergeVideos(outputfilename):
    L =[]
    # print(os.getcwd())
    if os.path.exists(outputfilename):
        os.remove(outputfilename)
    for root, dirs, files in os.walk('output/'):
        files = natsorted(files)
        # print("9 ", root)
        for file in files:
            if os.path.splitext(file)[1] == '.mp4':
                filePath = os.path.join(root, file)
                video = VideoFileClip(filePath)
                L.append(video)
    #print(len(L))
    final_clip = concatenate_videoclips(L)

    final_clip.to_videofile(outputfilename, fps=10, remove_temp=False)
    deleteIntermediateFiles()

def deleteIntermediateFiles():
    for root, dirs,files in os.walk('output/'):
        # print(files)
        for file in files:
            if file.startswith("dummy"):
                print(file)
                os.remove('output/'+file)


#for testing
if __name__=="__main__":
    mergeVideos('../output/human_life_span')
    #mergeVideos()