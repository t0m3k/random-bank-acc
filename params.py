import sys, getopt

def get_params():
    usage = "Usage: python rand_bank_acc.py -c <number of sort codes> -a <number of accounts per sort code> -f <file name to save>"

    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hc:a:f:", ["help", "codes=", "accounts=", "file="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    codes = 100
    accounts = 50
    file = "accounts.csv"

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(usage)
            sys.exit()
        elif opt in ("-c", "--codes"):
            codes = int(arg)
        elif opt in ("-a", "--accounts"):
            accounts = int(arg)
        elif opt in ("-f", "--file"):
            file = arg


    return codes, accounts, file