
n= 121188535871798118811428322495136173485838157702837603009744079502828661170574654643712519826693731103670617468427120197687519224611728159372629028899279680740201176466228593180097000630667826923128885153190352359299571456927587933797154384731664367396394374086703053646510220882981791309024543386831488440013
e= 3
ct=562749201081331837108793477890957823131652438537884071933174193752437171468017571141298760057052425504923794842817741207
#siccome e è molto piccolo l'RSA mod(n) può non essere considerato 
#print(pwn(ct,1/e)) #fatto con wolfram alpha perchè input troppo grande

dflag = 38321129010652577449732081681654175472762802386790781
hexflag = (hex(dflag))
flag = bytes.fromhex(hexflag[2:])
print(flag)