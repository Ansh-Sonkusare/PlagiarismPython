import click
from difflib import SequenceMatcher
import math
@click.command()
@click.argument('path1')
@click.argument('path2')

def main(path1,path2):
    # print('hi')
    try:
        with open(path1) as f1 , open(path2) as f2:
            text1 = ''.join(f1.readlines())
            text2 = ''.join(f2.readlines())
            sq = SequenceMatcher(None , text1 , text2)
            print(str(math.floor(sq.ratio()*100)) + '%')
    except EnvironmentError:
        print(EnvironmentError)
main()