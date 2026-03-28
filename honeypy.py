import argparse
from ssh_honeypot import honeypot as ssh_honeypot
from web_honeypot import run_web_honeypot

# Parse Arguments

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--address", type=str, required=True)
    parser.add_argument("-p", "--port", type=int, required=True)
    parser.add_argument("-u", "--username", type=str)
    parser.add_argument("-pw", "--password", type=str)

    parser.add_argument('-s', "--ssh", action="store_true")
    parser.add_argument("-w", "--http", action="store_true")

    args = parser.parse_args()

    try:
        if args.ssh:
            print("[ - ] Running SSH honeypot ...")
            ssh_honeypot(args.address, args.port, args.username, args.password)
        elif args.http:
            print("[ - ] Running HTTP Wordpress Honeypot ...")
            run_web_honeypot(port=args.port, input_username=args.username, input_password=args.password)
        else:
            print("Choose a honeypot to run")
    except Exception as e:
        print(f"\n Exiting honeypy due to error: {e}")
        pass