class Solution:

    codepart = '#'
    sizepart = ','

    def encode(self, strs):
        encode_front = []
        encode_back = []
        for strs_single in strs:
            encode_back.extend(strs_single)
            encode_front.extend(str(len(strs_single)))
            encode_front.extend(self.sizepart)

        encode_front.extend(self.codepart)
        encode_front.extend(encode_back)
        return "".join(encode_front)
    
    def decode(self, s):
        encoded_front = s.split(self.codepart)[0]
        encoded_back = s.split(self.codepart,1)[1]
        curr = 0
        results = []
        for num in encoded_front.split(self.sizepart):
            if not num:
                continue
            len = int(num)
            results.append("".join(encoded_back)[curr:curr+len])
            curr += len
        return results
