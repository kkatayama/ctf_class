# coding: utf-8
flag = 'UDCTF{' + '#'*20 + '}'
print flag

print 'part_1:'
# left 
l = "ord(flag[0]) + 40"
ll = eval(l)
print l, '=', ll, '=', chr(ll)
# right
r = "ord(flag[-1])"
rr = eval(r)
print r, '=', rr, '=', chr(rr)
# ans
a = str(ll) + ' == ' + str(rr)
print 'statement:', a, eval(a)
print '\tflag[0] =', flag[0]
print '\tflag[-1] =', flag[-1]

print 'part_2:'
# left 
l = "ord(flag[-1]) - 2"
ll = eval(l)
print l, '=', ll, '=', chr(ll)
# right
r = "ord(flag[5])"
rr = eval(r)
print r, '=', rr, '=', chr(rr)
# ans
a = str(ll) + ' == ' + str(rr)
print 'statement:', a, eval(a)
print '\tflag[-1] =', flag[0]
print '\tflag[5] =', flag[5]

print 'part_4:'
l = "flag[10]"
r = "flag[15]"
print 'statement: ' + l + ' == ' + r

print 'part_5:'
l = "flag[15]"
r = "flag[20]"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[10] = tmp[15] = tmp[20] = '_'
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_6:'
l = "int(flag[6]) + int(flag[14]) + int(flag[19])"
r = "7"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[6] = '1'
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_7:'
l = "flag[14]"
r = "flag[19]"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[14] = chr(51)
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_8:'
l = "ord(flag[19])"
r = "51"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[19] = chr(51)
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_9:'
l = "flag[11:14]"
r = "'byt'"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[11:14] = 'byt'
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_10:'
l = "flag[8]"
r = "flag[23]"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[23] = chr(110)
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_11:'
l = "ord(flag[17]) % 2"
r = "0"
print 'statement: ' + l + ' == ' + r
print '\tflag =', flag

print 'part_12:'
l = "ord(flag[17]) % 3"
r = "0"
print 'statement: ' + l + ' == ' + r
print '\tflag =', flag

print 'part_13:'
l = "ord(flag[17]) % 4"
r = "0"
print 'statement: ' + l + ' == ' + r
print '\tflag =', flag

print 'part_14:'
l = "flag[17]"
r = "isdigit()"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[17] = '0'
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_15:'
l = "flag[9]"
r = "flag[13].upper()"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[9] = tmp[13].upper()
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_16:'
l = "ord(flag[8]) % 10"
r = "0"
print 'statement: ' + l + ' == ' + r
print '\tflag =', flag

print 'part_17:'
l = "ord(flag[8])"
r = "100"
print 'statement: ' + l + ' > ' + r
print '\tflag =', flag

print 'part_18:'
l = "ord(flag[8])"
r = "120"
print 'statement: ' + l + ' < ' + r
tmp = list(flag)
tmp[8] = chr(110)
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_19:'
l = "flag[22]"
r = "U"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[22] = 'U'
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_20:'
l = "ord(flag[22]) ^ 51)"
r = "ord(flag[21])"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[21] = chr(ord(flag[22]) ^ 51)
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_21:'
l = "ord(flag[16])"
r = "99"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[16] = chr(99)
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_22:'
l = "ord(flag[18]) - ord(flag[16])"
r = "1"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[18] = chr(ord(flag[16])+1)
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_23:'
l = "ord(flag[18]) + 15"
r = "ord(flag[7])"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[7] = chr(ord(flag[18])+15)
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_24:'
l = "ord(flag[25])"
r = "33"
print 'statement: ' + l + ' == ' + r
tmp = list(flag)
tmp[24] = '?'
tmp[25] = chr(33)
flag = ''.join(tmp)
print '\tflag =', flag

print 'part_25:'
tmp = 0
for c in flag:
    tmp += ord(c)
if tmp == 2342:
    print 'success...'
# tmp = list(flag)
# tmp[18] = chr(ord(flag[16])+1)
# flag = ''.join(tmp)
print '\tflag =', flag
