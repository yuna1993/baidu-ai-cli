'''
    Commands examples: 
    python3 main.py -t (Scan all files in assets/text/*)
    python3 main.py -t -p assets/text/a.txt (Scan file of assets/text/a.txt)
'''
import argparse
from audit_cli.cli_text_audit import cli_text_audit


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text_audit", action="store_true")
    parser.add_argument("-p", "--path", type=str, required=False)
    args = parser.parse_args()

    if args.text_audit:
        cli_text_audit(args)
