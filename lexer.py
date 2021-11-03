from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # FRAMES
        self.lexer.add('FRAMES', r'\d+')
        # Image
        self.lexer.add('IMAGE', r'[^\s]+(\.(?i)(jpg|png|gif|bmp|jpeg))')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()