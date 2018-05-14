import sys
script, encoding, error= sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:#if it is true then run the following code
          print_line(line, encoding, errors)##print_line function
          return main(language_file, encoding, errors)##go to the next line


def print_line(line, encoding, errors):
    next_lang = line.strip()#striping of the trailing \n on the line string
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)#what does the errors mean
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")
main(languages, encoding, error)
