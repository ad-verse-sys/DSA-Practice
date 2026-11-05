class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp_num = x
        reverse_num = 0
        while temp_num > 0:
            digit = temp_num  % 10
            reverse_num = reverse_num* 10 + digit
            temp_num = temp_num // 10
        
        if x == reverse_num:
            return True
        else:
            return False