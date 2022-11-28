import random,string

class shorten_url:
    token_size = 4
    def __init__(self, token_size=None):
        self.token_size = token_size if token_size  is not None else 4

    def issuce_token():
        leters = string.ascii_letters
        return ''.join(random.choice(leters) for i in range(self.token_size))