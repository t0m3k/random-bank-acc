import sys, getopt, os, random, csv


def random_sort_code():
    sort_codes = read_csv()
    return random.choice(sort_codes)[0:6]


def read_csv():
    with open(os.path.join(sys.path[0], "sort_codes.csv"), "r") as f:
        reader = csv.reader(f)
        next(reader)
        return [row[0] for row in reader]


def get_params():
    usage = "Usage: python bank-accounts -c <number of sort codes> -a <number of accounts per sort code> -f <file name to save>"

    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hc:a:f:", ["help", "codes=", "accounts=", "file="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    codes = 10
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