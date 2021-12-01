"""
・事前作業です

・リモートUACを解除するには、レジストリエディア (regedit)を使って管理者モードでレジストリを変更します。
UACのリモート制限を無効にする

変更(作成)するキー: \HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
変更(作成)する名前: LocalAccountTokenFilterPolicy (DWORD)
値: 1
再起動はしなくていい

・ファイアーウォール
推奨環境
Windows ファイアウォールを介したプログラムまたは機能を許可する
Windows Management Indtrumentation(WMI) をチェック
再起動はしなくていい

関数化する場合必要な変数
  DRIVENAME ドライブ（C、D、E、F）
  NODE
  USER
  PASS
"""

#関数名
#なんだこれ？
#from win32api import EndUpdateResource


def rimote_drive(NODE,USER,PASS,DRIVENAME):

  #wmiライブラリを使用
  import wmi

  try:
    #関数の引数 1～3
    #NODE：コンピュータ名、またはIPアドレス
    #USER：ユーザー名
    #PASS：パスワード
    #IPアドレスだと少し時間かかる？
    
    # try内の文で、接続失敗すると、ここで処理終了
    try:
      conn = wmi.WMI(NODE, user=USER, password=PASS)
    except:
      print(DRIVENAME,'接続できない')
      return

    #ホスト名
    #obj = conn.Win32_OperatingSystem()[0]
    #print("Hostname: %s" % obj.CSName)

    #ドライブ

    #関数の引数 4
    #DRIVENAME;"C:" "D:" "E:" "F:"
    obj = conn.Win32_LogicalDisk(DeviceID=DRIVENAME)[0]

    #ドライブ容量 FreeSpace：空き領域(バイト)
    #画面に表示される空き領域：パソコンは2進数で計算するので、1000を1024で計算する
    # 2の30乗で割っているのは、バイト→ギガバイトに変換するから
    #float:数値を浮動小数点として取得
    #format .2:少数点第2位 f:固定少数

    #C Dはなくても「0.0」として出力してくれるらしい（それ以外はエラーになる）

    free = float(obj.FreeSpace) / 1024 / 1024 / 1024
    
    #「0.0」（ドライブがないか、容量が0とする）なら、ここで処理終了
    if DRIVENAME=="D:" or DRIVENAME=="C:":
      if free==0:
        print(DRIVENAME,'がない、または、',DRIVENAME,'の空き容量が0')
        return

    
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
    #「整数」+「少数第1.2位」
    str_free_result=str_free_array_int + '.' + str_free_array_de[0] + str_free_array_de[1]
    #「整数」+「少数第1.2位」 結果
    print(NODE,'情報  ',DRIVENAME,str_free_result)
 
  #異常発生時（ほとんどはE,Fドライブがないときに来るはずや）
  except:
    print(DRIVENAME , '失敗。そのサーバーに',DRIVENAME,'はない')
  

#関数の終わり

#関数使います
rimote_drive("hokuto-3-PC","hokuto-3", "hokuto070222","C:")
rimote_drive("hokuto-3-PC","hokuto-3", "hokuto070222","D:")
rimote_drive("hokuto-3-PC","hokuto-3", "hokuto070222","E:")
rimote_drive("hokuto-3-PC","hokuto-3", "hokuto070222","F:")