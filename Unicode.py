try:
    str
except NameError:
    raise ImportError

from pybench import Test
from string import join

class ConcatUnicode(Test):

    version = 2.0
    operations = 10 * 5
    rounds = 60000

    def test(self):

        # Make sure the strings are *not* interned
        s = str(join(list(map(str,list(range(100))))))
        t = str(join(list(map(str,list(range(1,101))))))

        for i in range(self.rounds):
            t + s
            t + s
            t + s
            t + s
            t + s

            t + s
            t + s
            t + s
            t + s
            t + s

            t + s
            t + s
            t + s
            t + s
            t + s

            t + s
            t + s
            t + s
            t + s
            t + s

            t + s
            t + s
            t + s
            t + s
            t + s

            t + s
            t + s
            t + s
            t + s
            t + s

            t + s
            t + s
            t + s
            t + s
            t + s

            t + s
            t + s
            t + s
            t + s
            t + s

            t + s
            t + s
            t + s
            t + s
            t + s

            t + s
            t + s
            t + s
            t + s
            t + s

    def calibrate(self):

        s = str(join(list(map(str,list(range(100))))))
        t = str(join(list(map(str,list(range(1,101))))))

        for i in range(self.rounds):
            pass


class CompareUnicode(Test):

    version = 2.0
    operations = 10 * 5
    rounds = 150000

    def test(self):

        # Make sure the strings are *not* interned
        s = str(join(list(map(str,list(range(10))))))
        t = str(join(list(map(str,list(range(10))))) + "abc")

        for i in range(self.rounds):
            t < s
            t > s
            t == s
            t > s
            t < s

            t < s
            t > s
            t == s
            t > s
            t < s

            t < s
            t > s
            t == s
            t > s
            t < s

            t < s
            t > s
            t == s
            t > s
            t < s

            t < s
            t > s
            t == s
            t > s
            t < s

            t < s
            t > s
            t == s
            t > s
            t < s

            t < s
            t > s
            t == s
            t > s
            t < s

            t < s
            t > s
            t == s
            t > s
            t < s

            t < s
            t > s
            t == s
            t > s
            t < s

            t < s
            t > s
            t == s
            t > s
            t < s

    def calibrate(self):

        s = str(join(list(map(str,list(range(10))))))
        t = str(join(list(map(str,list(range(10))))) + "abc")

        for i in range(self.rounds):
            pass


class CreateUnicodeWithConcat(Test):

    version = 2.0
    operations = 10 * 5
    rounds = 80000

    def test(self):

        for i in range(self.rounds):
            s = 'om'
            s = s + 'xbx'
            s = s + 'xcx'
            s = s + 'xdx'
            s = s + 'xex'

            s = s + 'xax'
            s = s + 'xbx'
            s = s + 'xcx'
            s = s + 'xdx'
            s = s + 'xex'

            s = s + 'xax'
            s = s + 'xbx'
            s = s + 'xcx'
            s = s + 'xdx'
            s = s + 'xex'

            s = s + 'xax'
            s = s + 'xbx'
            s = s + 'xcx'
            s = s + 'xdx'
            s = s + 'xex'

            s = s + 'xax'
            s = s + 'xbx'
            s = s + 'xcx'
            s = s + 'xdx'
            s = s + 'xex'

            s = s + 'xax'
            s = s + 'xbx'
            s = s + 'xcx'
            s = s + 'xdx'
            s = s + 'xex'

            s = s + 'xax'
            s = s + 'xbx'
            s = s + 'xcx'
            s = s + 'xdx'
            s = s + 'xex'

            s = s + 'xax'
            s = s + 'xbx'
            s = s + 'xcx'
            s = s + 'xdx'
            s = s + 'xex'

            s = s + 'xax'
            s = s + 'xbx'
            s = s + 'xcx'
            s = s + 'xdx'
            s = s + 'xex'

            s = s + 'xax'
            s = s + 'xbx'
            s = s + 'xcx'
            s = s + 'xdx'
            s = s + 'xex'

    def calibrate(self):

        for i in range(self.rounds):
            pass


class UnicodeSlicing(Test):

    version = 2.0
    operations = 5 * 7
    rounds = 140000

    def test(self):

        s = str(join(list(map(str,list(range(100))))))

        for i in range(self.rounds):

            s[50:]
            s[:25]
            s[50:55]
            s[-1:]
            s[:1]
            s[2:]
            s[11:-11]

            s[50:]
            s[:25]
            s[50:55]
            s[-1:]
            s[:1]
            s[2:]
            s[11:-11]

            s[50:]
            s[:25]
            s[50:55]
            s[-1:]
            s[:1]
            s[2:]
            s[11:-11]

            s[50:]
            s[:25]
            s[50:55]
            s[-1:]
            s[:1]
            s[2:]
            s[11:-11]

            s[50:]
            s[:25]
            s[50:55]
            s[-1:]
            s[:1]
            s[2:]
            s[11:-11]

    def calibrate(self):

        s = str(join(list(map(str,list(range(100))))))

        for i in range(self.rounds):
            pass

### String methods

class UnicodeMappings(Test):

    version = 2.0
    operations = 3 * (5 + 4 + 2 + 1)
    rounds = 10000

    def test(self):

        s = join(list(map(chr,list(range(20)))),'')
        t = join(list(map(chr,list(range(100)))),'')
        u = join(list(map(chr,list(range(500)))),'')
        v = join(list(map(chr,list(range(1000)))),'')

        for i in range(self.rounds):

            s.lower()
            s.lower()
            s.lower()
            s.lower()
            s.lower()

            s.upper()
            s.upper()
            s.upper()
            s.upper()
            s.upper()

            s.title()
            s.title()
            s.title()
            s.title()
            s.title()

            t.lower()
            t.lower()
            t.lower()
            t.lower()

            t.upper()
            t.upper()
            t.upper()
            t.upper()

            t.title()
            t.title()
            t.title()
            t.title()

            u.lower()
            u.lower()

            u.upper()
            u.upper()

            u.title()
            u.title()

            v.lower()

            v.upper()

            v.title()

    def calibrate(self):

        s = join(list(map(chr,list(range(20)))),'')
        t = join(list(map(chr,list(range(100)))),'')
        u = join(list(map(chr,list(range(500)))),'')
        v = join(list(map(chr,list(range(1000)))),'')

        for i in range(self.rounds):
            pass

class UnicodePredicates(Test):

    version = 2.0
    operations = 5 * 9
    rounds = 120000

    def test(self):

        data = ('abc', '123', '   ', '\u1234\u2345\u3456', '\uFFFF'*10)
        len_data = len(data)

        for i in range(self.rounds):
            s = data[i % len_data]

            s.isalnum()
            s.isalpha()
            s.isdecimal()
            s.isdigit()
            s.islower()
            s.isnumeric()
            s.isspace()
            s.istitle()
            s.isupper()

            s.isalnum()
            s.isalpha()
            s.isdecimal()
            s.isdigit()
            s.islower()
            s.isnumeric()
            s.isspace()
            s.istitle()
            s.isupper()

            s.isalnum()
            s.isalpha()
            s.isdecimal()
            s.isdigit()
            s.islower()
            s.isnumeric()
            s.isspace()
            s.istitle()
            s.isupper()

            s.isalnum()
            s.isalpha()
            s.isdecimal()
            s.isdigit()
            s.islower()
            s.isnumeric()
            s.isspace()
            s.istitle()
            s.isupper()

            s.isalnum()
            s.isalpha()
            s.isdecimal()
            s.isdigit()
            s.islower()
            s.isnumeric()
            s.isspace()
            s.istitle()
            s.isupper()

    def calibrate(self):

        data = ('abc', '123', '   ', '\u1234\u2345\u3456', '\uFFFF'*10)
        len_data = len(data)

        for i in range(self.rounds):
            s = data[i % len_data]

try:
    import unicodedata
except ImportError:
    pass
else:
    class UnicodeProperties(Test):

        version = 2.0
        operations = 5 * 8
        rounds = 100000

        def test(self):

            data = ('a', '1', ' ', '\u1234', '\uFFFF')
            len_data = len(data)
            digit = unicodedata.digit
            numeric = unicodedata.numeric
            decimal = unicodedata.decimal
            category = unicodedata.category
            bidirectional = unicodedata.bidirectional
            decomposition = unicodedata.decomposition
            mirrored = unicodedata.mirrored
            combining = unicodedata.combining

            for i in range(self.rounds):

                c = data[i % len_data]

                digit(c, None)
                numeric(c, None)
                decimal(c, None)
                category(c)
                bidirectional(c)
                decomposition(c)
                mirrored(c)
                combining(c)

                digit(c, None)
                numeric(c, None)
                decimal(c, None)
                category(c)
                bidirectional(c)
                decomposition(c)
                mirrored(c)
                combining(c)

                digit(c, None)
                numeric(c, None)
                decimal(c, None)
                category(c)
                bidirectional(c)
                decomposition(c)
                mirrored(c)
                combining(c)

                digit(c, None)
                numeric(c, None)
                decimal(c, None)
                category(c)
                bidirectional(c)
                decomposition(c)
                mirrored(c)
                combining(c)

                digit(c, None)
                numeric(c, None)
                decimal(c, None)
                category(c)
                bidirectional(c)
                decomposition(c)
                mirrored(c)
                combining(c)

        def calibrate(self):

            data = ('a', '1', ' ', '\u1234', '\uFFFF')
            len_data = len(data)
            digit = unicodedata.digit
            numeric = unicodedata.numeric
            decimal = unicodedata.decimal
            category = unicodedata.category
            bidirectional = unicodedata.bidirectional
            decomposition = unicodedata.decomposition
            mirrored = unicodedata.mirrored
            combining = unicodedata.combining

            for i in range(self.rounds):

                c = data[i % len_data]
