class Solution():

    def Roman(self, num):
        """
        :type num: int
        :rtype: str
        """
        arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ret = ''    #用于储存罗马数字
        i = 0
        while num:
            yu = num // arabic[i]
            ret += roman[i] * yu
            num = num - yu * arabic[i]
            i += 1
        print(f'对应的罗马数字为:'+ ret)
        return ret    #返回输出的结果

n = int(input("输入数字："))
c = Solution()
c.Roman(n)
#print(c.Roman(n))
