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

関数化する場合必要な変数
  ドライブ（C、D、E、F）
  NODE
  USER
  PASS
"""



'''NODE = "hokuto-PC"
USER = "hokuto"
PASS = "hokuto070222"
'''

#wmiライブラリを使用
import wmi

#NODE：コンピュータ名、またはIPアドレス
#USER：ユーザー名
#PASS：パスワード
#IPアドレスだと少し時間かかる？
#NODE = "192.168.0.8"
NODE = "hokuto-3-PC"
USER= "hokuto-3"
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
free = float(obj.FreeSpace) / 1024 / 1024 / 1024
print('FreeSpace: {:.2f}'.format(free))

#ドライブ容量は小数点第1位まで記入する.多分切り捨て？
#float mathだと四捨五入になるので、目的と反する
#切り捨てか、少数1位までしか取得しないものを出す
#うまく少数第1位で切り捨てができそうにないんで、無理やり抽出する手段をとる

#ドライブ空き容量を文字列に変換する
str_free=str(free)
#splitで「整数」「少数」配列に分ける
str_free_array=str_free.split('.')
#整数部分
str_free_array_int=str_free_array[0]
#少数部分
str_free_array_de=str_free_array[1]
#「整数」+「少数第1位」
str_free_result=str_free_array_int + '.' + str_free_array_de[0]
#結果
print(str_free_result)


