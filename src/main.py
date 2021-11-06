#create a programming language for reading input file using primitives
# Eg: startFrame endFrame Image will be stored in human_life_span.flip file
# further enhancements like adding position of image

import os
import sys
from PyPDF2 import PdfFileMerger
from Lexer import Lexer
from src.mergeVideo import mergeVideos
from src.parser import Parser
import getopt


def compilefunction(fname, output_path, pdf_merger):
    with open(fname) as f:
        text_input = f.read()
        lines = text_input.split('\n')
        for line in lines:
            if line == "":
                continue
            print(line)
            lexer = Lexer().get_lexer()
            tokens = lexer.lex(line)
            print(tokens)

            pg = Parser(output_path)
            pg.parse()
            parser = pg.get_parser()
            parser.parse(tokens).eval()
            if output_path.endswith(".pdf"):
                pdf_merger.append(output_path)
                os.remove(output_path)
    if output_path.endswith(".pdf"):
        with open(output_path, 'wb') as fileobj:
            pdf_merger.write(fileobj)
    else :
        mergeVideos(output_path)



if __name__=="__main__":
    input_file_name = "human_life_span.flip"
    output_file_name = "human_life_span.pdf"
    input_file_name = sys.argv[1]
    argv = sys.argv[2:]

    try:
        opts, args = getopt.getopt(argv, "o:")
    except:
        sys.exit("Error in command format. Please try again.")

    for opt, arg in opts:
        if opt in ['-o']:
            output_file_name = arg

    print("Reading from input file: "+input_file_name + "\n" + "Given Output file: "+output_file_name)

    output_path = "output/"+output_file_name
    filename = "input/"+input_file_name

    pdf_merger = PdfFileMerger()
    compilefunction(filename, output_path, pdf_merger )

