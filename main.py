ENCODING = "cp1252"
NEWLINE = "\r\n"

READMODE = "r"
WRITEMODE = "w"


def get_lines(filename):
    with open(filename, READMODE, encoding=ENCODING, newline=NEWLINE) as file:
        return [ line for line in file ]
    
def copy_file_replacing(input_filename, output_filename, conditional_prefix="|Y601|", old_content="|Y601|", new_content="|Y750|"):
    with open(input_filename, READMODE, encoding=ENCODING, newline=NEWLINE) as input:
        with open(output_filename, WRITEMODE, encoding=ENCODING, newline="") as output:
            for line in input:
                if line.startswith(conditional_prefix):
                    output.write(line.strip(NEWLINE).replace(old_content, new_content) + NEWLINE)
                else:
                    output.write(line.strip(NEWLINE) + NEWLINE)

def print_file(filename):
    with open(filename, READMODE, encoding=ENCODING, newline=NEWLINE) as file:
        print(get_lines(filename))

def print_when_starts_with(filename, prefix="|Y601|"):
    with open(filename, READMODE, encoding=ENCODING, newline=NEWLINE) as file:
        for number, line in enumerate(file, start=1):
            if line.startswith(prefix):
                print(f"line {number}: {line.strip(NEWLINE)}")

if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"

    copy_file_replacing(input_filename, output_filename)
    print_file(output_filename)
        
