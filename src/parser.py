from rply import ParserGenerator

from Tokens.Image import Image
from Tokens.Number import Number
from makePdf import MakePDF
from src.makeVideo import MakeVideo


class Parser():
    def __init__(self,ouputfilename):
        self.ouputfilename=ouputfilename
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['FRAMES', 'NUMBER','IMAGE', 'OPEN_PAREN', 'CLOSE_PAREN','COMMA']
        )

    def parse(self):
        @self.pg.production('program : expression')
        def program(p):
            print(p)
            #print(self.ouputfilename)
            return (p[0])

        @self.pg.production('expression : FRAMES OPEN_PAREN expression COMMA expression CLOSE_PAREN  expression')
        def expression(p):
            print(20,p)
            start_frame = p[2]
            end_frame = p[4]
            image = p[6]
            print(start_frame)
            print(end_frame)
            if self.ouputfilename.endswith(".pdf"):
                return MakePDF(start_frame,end_frame,image,self.ouputfilename)
            else:
                return MakeVideo(start_frame, end_frame, image)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value).eval()

        @self.pg.production('expression : IMAGE')
        def image(p):
            return Image(p[0].value).eval()

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()