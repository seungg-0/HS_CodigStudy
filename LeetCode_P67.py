class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # a,b 문자열 길이 맞춰주기
        if len(b) >=len(a):
            a = a.zfill(len(b))
        else:
            b = b.zfill(len(a))
            
        # 입력값 각각 reverse
        a = a[::-1]
        b = b[::-1]
        
        # c == a, b각 자릿수 합
        c = []
        for i in range(0, len(a)):
            c.append(int(a[i]) + int(b[i]))
        
        # 풀이
        for i in range(0, (len(c) - 1)):
            if c[i] >= 2:
                if c[i] == 2:
                    c[i] = 0
                elif c[i] == 3:
                    c[i] = 1        
                if (c[i + 1] == 0):
                    c[i + 1] = 1
                elif (c[i + 1] == 1):
                    c[i + 1] = 2
                else:
                    c[i + 1] = 3
                
        # 풀이_마지막값 처리
        if c[-1] >= 2:
            if c[-1] == 2:
                c[-1] = 0
            else:
                c[-1] = 1    
            c.append(1)
            
        c = ''.join(map(str,c))
     
        return c[::-1]
