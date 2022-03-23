import argparse
from cgi import print_arguments
from audit_cli.cli_text_audit import cli_text_audit
from audit_cli.cli_image_audit import cli_image_audit


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text_audit", action="store_true")
    parser.add_argument("-i", "--image_audit", action="store_true")
    parser.add_argument("-p", "--path", type=str, required=False)
    args = parser.parse_args()

    '''
    Commands examples: 
    python3 main.py -t (Scan all files in assets/text/*)
    python3 main.py -t -p assets/text/a.txt (Scan file of assets/text/a.txt)
    '''

    if args.text_audit:
        cli_text_audit(args)

    '''
    Commands examples: 
    python3 main.py -i (Scan all files in assets/image/*)
    python3 main.py -t -p assets/image/a.png (Scan file of assets/image/a.png)
    '''
    if args.image_audit:
        cli_image_audit(args)
