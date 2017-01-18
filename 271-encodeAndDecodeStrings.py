class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded=[]
        for i in xrange(len(strs)):
            encoded.append(`len(strs[i])`)
            encoded.append('/')
            encoded.append(strs[i])
        return ''.join(encoded)

        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        decoded=[]
        p=0
        while p<len(s):
            intEnd=s.find('/',p)
            length=int(s[p:intEnd])
            p=intEnd+length+1
            decoded.append(s[intEnd+1:p])
            

        return decoded

if __name__ == '__main__':
    c=Codec()
    print c.decode(c.encode([
        'hello',
        'kitty'
        ]))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))