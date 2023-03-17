# Generate random bank account numbers

# Requirements

## random_uk_bank_account
`pip3 install random-uk-bank-account`

# Usage
`python rand_bank_acc.py -c` \<number of sort codes> `-a` \<number of accounts per sort code> `-f` \<file name to save>
## Example
`python rand_bank_acc.py -c 10 -a 100 -f bank_accounts.csv`

# Docker 
`docker build -t bankacc .`

Create 5 sort codes with 10 accounts each inside docker container
`docker run --name test2 bankacc -c 5 -a 10`