import argparse

parser=argparse.ArgumentParser(description='Calculate area of a circle')
parser.add_argument('radius', type=int, help='radius of circle')
args=parser.parse_args()

def area_is(radius):
    ar=(radius**2)*3.14
    return ar

if __name__ == '__main__':
    print(area_is(args.radius))