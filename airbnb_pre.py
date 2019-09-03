# -*- coding:utf8 -*-

'''
airbnb interview:
对下述代码a/b/c/d 字符串进行处理，处理规则：
 i.   使用 | 代替 , 进行分词；
 ii.  单层引号去掉，多层引号去掉最外层，引号内部不做分词处理；
'''

a = 'rwer321,dad,adas,ytruty,yihgf'
b = '"ha,ua",sa,da,""da,da"",dad'
c = 'dasd,""asddad"",fsfsf,gdfg,1'
d = '"ha,ua",sa,da,"""da,da""",dad'

class solution(object):
    def str_deal(self,instr):
        length = len(instr)
        flag = 0
        deep = 0
        start = end = cur = 0
        ans = []
        while cur < length:
            if instr[cur] == '"' and flag != 1:
                start = cur
                flag = 1
                while instr[cur] == '"':
                    cur += 1
                    deep += 1
            elif instr[cur] == '"' and flag == 1:
                ans.append(instr[start+1:cur+deep-1])
                flag = 0
                start = cur + deep + 1
                cur = cur + deep
                deep = 0
            elif instr[cur] == ',' and flag != 1:
                #print instr[start:cur]
                ans.append(instr[start:cur])
                start = cur + 1 
            cur += 1
        if instr[start:length]:
            ans.append(instr[start:length])
        return '|'.join(ans)

s = solution()
print s.str_deal(a)
print s.str_deal(b)
print s.str_deal(c)
print s.str_deal(d)
