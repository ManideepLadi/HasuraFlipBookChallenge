from lexer import Lexer


#create a programming language for reading input file using primitives
# Eg: startFrame endFrame Image will be stored in human_life_span.flip file
# further enhancements like adding position of image

fname = "Testfiles/human_life_span.flip"
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
        #
        # pg = Parser()
        # pg.parse()
        # parser = pg.get_parser()
        # parser.parse(tokens).eval()
        # pdf_merger.append(output_path)
        # os.remove(output_path)

# with open(output_path, 'wb') as fileobj:
#     pdf_merger.write(fileobj)