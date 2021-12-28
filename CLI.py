import argparse

parser=argparse.ArgumentParser(description='My name is')
parser.add_argument('name', type=str, help='What is your name ?')
args=parser.parse_args()

def my_name_is(name):
    ba=name
    return ba

if __name__ == '__main__':
    print(my_name_is(args.name))
    

