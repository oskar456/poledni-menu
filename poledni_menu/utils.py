
def killwhitespace(string):
    """ Merge consecutive spaces into one space. """
    return " ".join(s.strip() for s in string.split())
