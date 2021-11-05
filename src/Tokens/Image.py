from rply.token import BaseBox


class Image(BaseBox):
	def __init__(self, image):
		self.image = image

	def eval(self):
		return (self.image)