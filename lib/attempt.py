import random
from secretcode import AvailableColours, SecretCode


class MakeAttempt():

    def __init__(self, codes):
        self.codes = self.validate(codes)

    def validate(self, codes):
        if len(set(codes)) != 4 or \
                not all(code in SecretCode.available_colours for code in codes):
            raise ValueError
        return codes

    def score(self, scode):
        scores = []
        for index, char in enumerate(self.codes):
            if char == scode[index]:
                scores.append(AvailableColours.Black)
            elif char in scode:
                scores.append(AvailableColours.White)
            else:
                scores.append(AvailableColours.NotAvailable)
        random.shuffle(scores)
        return scores
