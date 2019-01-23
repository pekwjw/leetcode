# -*- coding:utf-8 -*-

# dfs
class Solution(object):
    def restoreIpAddress(self,s):
        def dfs(s,sub,ips,ip):
            if sub == 4:
                if s == '':
                    ips.append(ip[1:])
                return
            for i in range(1,4):
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        dfs(s[i:],sub+1,ips,ip+'.'+s[:i])
                    if s[0] == '0':
                        break
        ips = []
        dfs(s,0,ips,'')
        return ips
        
def main():
    a = "102343521"
    so = Solution()
    print so.restoreIpAddress(a)
    
if __name__ == "__main__":
    main()
    
# output:
# ['10.234.35.21', '102.34.35.21']
