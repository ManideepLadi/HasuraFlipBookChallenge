import os
from typing import List

import moviepy.video.io.ImageSequenceClip

from src.Tokens.Frames import Frames
from src.Tokens.Image import Image


class MakeVideo(Frames, Image):
	def __init__(self, start_frame, end_frame, image):
		Image.__init__(self, "images/"+image)
		Frames.__init__(self, start_frame, end_frame)

	def eval(self):
		image = self.image
		start_frame = self.start_frame
		end_frame = self.end_frame
		# original output or merged pdf
		output_path = "output/dummy"+str(start_frame)
		image_files = [image]*5
		#image_files.append(intermediateImages)
		print(image_files)
		clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=15)
		clip.write_videofile(output_path+'.mp4')


		# with open(output_path, 'wb') as fileobj:
		# 	pdf_merger.write(fileobj)
