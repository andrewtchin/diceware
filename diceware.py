import argparse

from Crypto.Random import random


class Diceware(object):
    def __init__(self, wordlist_path):
        self.wordlist_path = wordlist_path
        self.wordlist = self.load_wordlist()

    def load_wordlist(self):
        """Read the wordlist file."""
        wordlist = {}
        with open(self.wordlist_path, 'r') as infile:
            for line in infile:
                pair = line.split()
                wordlist[pair[0]] = pair[1]
        return wordlist

    def get_word(self):
        """Randomly select word from wordlist."""
        rolls = []
        for x in range(5):
            rolls.append(str(random.randint(1,6)))
        key = ''.join(rolls)
        return self.wordlist[key]

    def generate(self, num_words):
        """Generate diceware passphrase of specified length.

        Args:
            num_words (int): number of words to select
        """
        passphrase = []
        for x in range(num_words):
            passphrase.append(self.get_word())
        return ' '.join(passphrase)


def parse_args():
    parser = argparse.ArgumentParser(description='Generate a Diceware passphrase.')
    parser.add_argument('--wordlist',
                        default='wordlist.txt',
                        help='Alternative wordlist.')
    parser.add_argument('--words',
                        default=5,
                        type=int,
                        help='Number of words to select for passphrase.')
    return parser.parse_args()


def main():
    args = parse_args()

    dw = Diceware(args.wordlist)
    print dw.generate(args.words)


if __name__ == '__main__':
    main()
