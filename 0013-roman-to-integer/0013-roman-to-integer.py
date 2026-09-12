class Solution(object):
    def romanToInt(self, s):

        rom_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and rom_int[s[i]] < rom_int[s[i+1]]:
                total -= rom_int[s[i]] 
            
            else:
                total += rom_int[s[i]]
        
        return total