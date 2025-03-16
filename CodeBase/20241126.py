class Word:
    def isPalindrome(self, s):
        s1 = s[::-1]
        return s == s1
    def isAnagram(self,s, ana):
        """

        :param ana: Madam -> mad
        :return:
        """
        count = 0

        for i in range(len(s)):
            for j in range(len(ana)):
                if s[i] != ana[j]:
                    count = 0
                    break
                else:
                    count += 1
            if count == 0:
                return  True
        return False



if __name__ == '__main__':
    inp = 'stsd'
    w = Word()
    #  print(w.isPalindrome(inp))
    sen = 'matam'
    ana = 'mad'
    print(w.isAnagram(sen, ana))
#Madam