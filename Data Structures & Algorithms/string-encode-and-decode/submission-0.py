class Solution:

    def encode(self, strs: List[str]) -> str:
        en_str = ''
        for s in strs:
            en_str += str(len(s)) + '/:' + s
        return en_str

    def decode(self, s: str) -> List[str]:

        ret = []

        i = 0
        print(s)
        while i < len(s):
            print(i)
            delim = s.find('/:', i)

            length = int(s[i:delim])

            en_str = s[delim+2: delim+2+length]

            ret.append(en_str)

            i = delim + 2 + length

        return ret
