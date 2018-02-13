import sys
from secretcode import SecretCode
from attempt import MakeAttempt

MAX_ATTEMPT = 6


class Game():

    def __init__(self):
        self.attempt = 0
        self.user_attempts = []
        self.user_scores = []

    def print_game_shell(self):
        print "=-=" * 22
        print " " * 20, "Mini MASTER MIND"
        print "=-=" * 22
        print "available colours:"
        for k, v in SecretCode.available_colours.items():
            print "%10s: %20s" % (k, v)
        print "Choose any 4 from above"
        print "Type BYE to EXIT the game..."

    def printable_scores(self, scores):
        return [SecretCode.score_colours[ccode] for ccode in scores]

    def lock_attempt(self, codes, score):
        self.attempt += 1
        self.user_attempts.append(codes)
        self.user_scores.append(score)


if __name__ == '__main__':
    g = Game()
    g.print_game_shell()
    # create a new secret code
    s = SecretCode()
    scode = s.set_secret_code()
    # make max 6 attempt
    while g.attempt < MAX_ATTEMPT:
        values = raw_input(
            "Enter your colour codes separated by space: ").strip()
        try:
            codes = map(lambda x: int(x), values.split())
            m = MakeAttempt(codes)
        except ValueError:
            if values.upper() == 'BYE':
                print "Thank you for attempt, See you again :)"
                sys.exit(0)
            print "Please enter valid colour codes again: "
            continue
        else:
            option = raw_input("Want to lock this option Y/N ? ")
            if option.lower() == 'y':
                scores = m.score(scode)
                g.lock_attempt(codes, scores)
                pscores = g.printable_scores(scores)
                print "Your score for attempt %d: %s" % (g.attempt, pscores)
            else:
                print "Try Again !!!"
                continue
    #
    # EOC
