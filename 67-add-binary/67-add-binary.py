class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # a = "11"
        # b = "1"
        output = ""
        if(len(a) > len(b)):
            diff = len(a) - len(b)
            b = ("0"*diff) + b
        else:
            diff = len(b) - len(a)
            a = ("0"*diff) + a

        # a = "11"
        # b = "01"
        remainder = 0
        for i in range(len(a)-1,-1,-1):
            if a[i] == "1" and b[i] == "1":
                if remainder == 0:
                    output = "0" + output 
                    remainder = 1
                else:
                    output = "1" + output        
            elif a[i] == "1" or b[i] == "1":
                if remainder == 0:
                    output = "1" + output 
                else:
                    output = "0" + output 
            elif a[i] == "0" and b[i] == "0":
                if remainder == 0:
                    output = "0" + output 
                else:
                    output = "1" + output 
                    remainder = 0
            # else:
            #     if remainder == 0:
            #         output = "1" + output 
            #     else:
            #         output = "0" + output
                    
        if remainder == 1:
            output = "1" + output

        return output
        
    