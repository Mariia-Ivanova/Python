def verbing(s: str) -> str:
    if len(s) < 3:
        return s
    if s.endswith('ing'):
        return s[0:-3] + 'ly'
    return s + 'ing'


def not_bad(s: str) -> str:
    not_pos = s.find('not')
    bad_pos = s.find('bad')
    if bad_pos > not_pos and not_pos != -1 and bad_pos != -1:
        return s[0:not_pos] + 'good' + s[bad_pos + 3:]
    return s
