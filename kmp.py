class KMP(object):
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def get_partial_match_table(self):
        pattern_len = len(self.pattern)

        self.prefix = {}
        self.prefix[0] = 0
        pattern_idx = 0
        prefix_idx = 1  # start with 1
        while(prefix_idx < pattern_len):
            if pattern[prefix_idx] == pattern[pattern_idx]:
                pattern_idx += 1
                self.prefix[prefix_idx] = pattern_idx
                prefix_idx += 1
            else:
                if (pattern_idx > 0):
                    pattern_idx = self.prefix[pattern_idx - 1]
                else:
                    self.prefix[prefix_idx] = pattern_idx
                    prefix_idx += 1
        print(self.prefix)

    def move_prefix_table(self):
        for i in range(1, len(self.prefix))[::-1]:
            self.prefix[i] = self.prefix[i-1]
        self.prefix[0] = -1
        print(self.prefix)

    def run(self):
        self.get_partial_match_table()
        self.move_prefix_table()

        text_len = len(self.text)
        pattern_len = len(self.pattern)

        text_idx = pattern_idx = 0

        while (text_idx < text_len):
            # print pattern found
            if pattern_idx == pattern_len - 1 and self.text[text_idx] == self.pattern[pattern_idx]:
                print("Found pattern at {}".format(text_idx - pattern_idx))
                pattern_idx = self.prefix[pattern_idx]

            # if current character matched
            if self.text[text_idx] == self.pattern[pattern_idx]:
                text_idx += 1
                pattern_idx += 1
            else:
                pattern_idx = self.prefix[pattern_idx]
                if pattern_idx == -1:
                    text_idx += 1
                    pattern_idx += 1


if __name__ == '__main__':
    text = 'ABABDABCACBDABCABABCABDCACBDAABABCBCDBAC'
    pattern = 'ABABC'

    kmp = KMP(text, pattern)

    kmp.run()
