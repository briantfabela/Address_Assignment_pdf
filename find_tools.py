def iter_ndigits(txt_str, n):
        '''iterates through a string and retuns only the first n ints'''

        ndigits = ''
        for char in txt_str:
            if char.isdigit():
                ndigits += char
            if len(ndigits) == n:
                return ndigits
        # did not find enough instances of digits, return all found
        return ndigits