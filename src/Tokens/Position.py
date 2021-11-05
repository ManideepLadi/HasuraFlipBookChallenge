from rply.token import BaseBox


class Position(BaseBox):
	def __init__(self, left_pos, right_pos):
		self.left_pos = left_pos
		self.right_pos = right_pos