"""リモートUACを解除するには、レジストリエディア (regedit)を使って管理者モードでレジストリを変更します。
UACのリモート制限を無効にする

変更(作成)するキー: \HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
変更(作成)する名前: LocalAccountTokenFilterPolicy (DWORD)
値: 1
再起動はしなくていい

ファイアーウォール
推奨環境
Windows ファイアウォールを介したプログラムまたは機能を許可する
Windows Management Indtrumentation(WMI) をチェック

再起動はしなくていい

"""

import wmi

NODE = "hokuto-3-PC"
USER = "hokuto-3"
PASS = "hokuto070222"

conn = wmi.WMI(NODE, user=USER, password=PASS)

#ホスト名
obj = conn.Win32_OperatingSystem()[0]
print("Hostname: %s" % obj.CSName)

#Cドライブ
obj = conn.Win32_LogicalDisk(DeviceID='C:')[0]

#Cドライブ容量 FreeSpace：空き領域(バイト)
#float:数値を浮動小数点として取得
#format .2:少数点第2位 f:固定少数
a=obj.FreeSpace
b=float(obj.FreeSpace)
c=float(obj.FreeSpace)/ 1024 / 1024 / 1024
c2=int((obj.FreeSpace))/ 1024 / 1024 / 1024
d=float(obj.FreeSpace)/ 1000 / 1000 / 1000
free = float(obj.FreeSpace) / 1024 / 1024 / 1024

print(a)
print(b)
print(c)
print(c2)
print(d)
print(free)
print('FreeSpace: {:.2f}'.format(free))

#ドライブ容量は小数点第1位まで記入する’多分切り捨て？
#float mathだと四捨五入になるので、目的と反する
#切り捨てか、少数1位までしか取得しないものを出す

aa=str(c)[0]
aa2=str(c2)[2]
#aa3=c2[0]
print(aa)
print(aa2)
#print(aa3)
bb=str(c)
bb2=bb.split('.')
print(bb2)
print(bb2[0])
print(bb2[1])
bb3=bb2[1]
bb4=bb3[0]
print(bb4)
bb5=bb2[0] + '.' + bb4
print(bb5)