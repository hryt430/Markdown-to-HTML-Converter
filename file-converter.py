import markdown
import os
import sys

def convert_to_html(input_path, output_path):
    with open(input_path) as f:
        md_contents = f.read()
        html_contents = markdown.markdown(md_contents)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_contents)
    
def validate_params(argv):
    if len(argv) != 3:
        print("Invalid argument: 2 arguments")
        return False
    input_path, output_path = argv[1], argv[2]
    if not os.path.isfile(input_path):
        print("Invalid arguments: Input file does not exist")
        return False
    return (input_path, output_path)

def main():
    argv = sys.argv
    params = validate_params(argv)
    if params:
        convert_to_html(*params)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()