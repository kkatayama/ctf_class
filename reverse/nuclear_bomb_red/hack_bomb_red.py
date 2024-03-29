# 0x08049558		# fgets
# 0x0804956b		# Menu Selection
# 0x08049837		# Clock Sequencd

import r2pipe

### start debugger...#
r = r2pipe.open('bomb')

### attempt to remove ptrace restriction... ###
r.cmd("(hooker, dr rax=0, dc);db $$+5 @@=`axt sym.imp.ptrace~CALL~call[1]`;dbc $$+5 .(hooker) @@=`axt sym.imp.ptrace~CALL~call[1]`")

### config settings... ###
r.cmd("e asm.emu=true;e asm.cmt.right=true;e asm.pseudo = true;e cmd.stack = true;eco solarized;e scr.utf8 = true")

### attach tty session from interact() script ###
r.cmd("e dbg.profile=bomb.rr2")
r.cmd('doo')

### bypass canary check ###
print r.cmd("aa;aac;s main;db main;s sym.red;db 0x08049864;dc;dsu 0x0804950a")
r.cmd('dss 1')
r.cmd('dss 1')

### pass stdio to interact() script... ###
r.cmd('dc')

### yay, made it here :) ###
clock_s = ''
found = False
while not found:
    func_name = r.cmdj('pdfj')['name']
    if 'sym.red' not in func_name:
        found = True
    else:
        dl = r.cmd('dr dl').strip()
        al = r.cmd('dr al').strip()
        print '|', al, dl, '|',
        dl = al
        r.cmd('dr dl='+dl)
        print r.cmd('dr al').strip(), r.cmd('dr dl').strip(), '|'
        clock_s += dl[-2:].decode('hex')
    r.cmd('dc')

print clock_s
