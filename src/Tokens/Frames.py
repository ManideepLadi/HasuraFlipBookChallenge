from rply.token import BaseBox


class Frames(BaseBox):
	def __init__(self, start_frame, end_frame):
		self.start_frame = start_frame
		self.end_frame = end_frame

