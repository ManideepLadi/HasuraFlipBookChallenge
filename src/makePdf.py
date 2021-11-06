import os

from PyPDF2 import PdfFileMerger
from fpdf import FPDF

from Tokens.Frames import Frames
from Tokens.Image import Image


class MakePDF(Frames, Image):
	def __init__(self, start_frame, end_frame, image,outputfilename):
		Image.__init__(self, "images/"+image)
		Frames.__init__(self, start_frame, end_frame)
		self.outfilename=outputfilename

	def eval(self):
		image = self.image
		start_frame = self.start_frame
		end_frame = self.end_frame
		# original output or merged pdf
		output_path = self.outfilename
		pdf_merger = PdfFileMerger()
		for i in range(1, end_frame-start_frame+1):
			pdf = FPDF()
			pdf.add_page()
			pdf.image(image,x=25,y=25)
			output = 'output/dummy_flipbook'+str(start_frame)+'.pdf'
			pdf.output(output, 'F')
			pdf_merger.append(output)
			os.remove(output)
			print('done')

		with open(output_path, 'wb') as fileobj:
			pdf_merger.write(fileobj)
