#cording:utf-8
import os
import re
import shutil
import pathlib




#Begin setting. -------------------------------------------------
#このプログラムを別プログラムでimportせずに使用する場合はここに設定を書く
#テキストデータのパス
textDirPath = ""

#分類後のデータシートの保存先パス
dataSheetPath = ""

#予約語フォルダのパス
nameDirPath = ""
#End setting. ---------------------------------------------------






def ReadText(textDirPath, dataSheetPath, nameDirPath):
    
    preTextfiles = os.listdir(textDirPath) #textフォルダ内のファイルをリスト化
    preNamefiles = os.listdir(nameDirPath) #nameフォルダ内のファイルをリスト化
    
    textfiles = [preTextfiles for preTextfiles in os.listdir(textDirPath) if not preTextfiles.startswith('.')] #textフォルダ内の隠しファイル以外をリスト化
    namefiles = [preNamefiles for preNamefiles in os.listdir(nameDirPath) if not preNamefiles.startswith('.')] #nameフォルダ内の隠しファイル以外をリスト化
    
    flag = False #2重ループを一括breakするためのflag
    
    namenum = len(namefiles) #textfilesの要素数
    
    
    for x in textfiles:
        textPath = textDirPath + os.sep + x #リスト内の要素について1つずつパス（正しくは，パスが格納された配列を作る）を作る
        
        errorflag1 = 0 #例外処理用flag1
        errorflag2 = False #例外処理用flag2
        
        try:
            with open(textPath) as tf:
                textStr = tf.read(100) #textファイルの中身を文字列に変換
                
                for y in namefiles:
                    namePath = nameDirPath + os.sep + y
                    
                    try:
                        with open(namePath, encoding="utf-8", errors='ignore') as nf:
                            nameLines = nf.read().split() #nameファイルの中身をリストに変換 #リストの区切りは改行ごとにする
                            
                            for s in nameLines:
                                if re.search(s, textStr) is not None: #予約語が何かあればループから抜ける
                                    flag = True
                                    break
                            if flag:
                                    flag = False
                                    break
                                
                    except FileNotFoundError:
                        print('Unable to open namePath.')
                        
                    errorflag1 += 1
                    if namenum == errorflag1:
                        print('Text file reading error.')
                        print('Please check {}.'.format(textDirPath + os.sep + x))
                        errorflag2 = True
                        break
                    
                if errorflag2 == False:
                    
                    directoryName = os.path.splitext(os.path.basename(namePath))[0] #パス指定したファイル名（拡張子なし）を取得
                    directoryPath = dataSheetPath + os.sep + directoryName #保存するパスを指定
                                
                        
                    if os.path.isdir(directoryPath) is not True: #ディレクトリがなければ勝手に作る
                        p_directoryPath =pathlib.Path(directoryPath) #配列をパスに変換 #os.mkdir()の引数は文字列
                        os.makedirs(p_directoryPath)
                                
                    #testData内にあるファイルの移動
                    p_textPath = pathlib.Path(textDirPath) #配列をパスに変換
                    #strに.parentが使えないため，パスに変換
                    nameX = os.path.splitext(os.path.basename(x))[0] #pdfについて演算子抜きのファイル名を作成
                    nameY = os.path.splitext(os.path.basename(y))[0] #予約後フォルダについて演算子抜きのファイル名を作成

                    if os.path.exists(dataSheetPath + os.sep + nameY + os.sep + nameX + '.pdf') is not True: #移動先にファイルが存在しているか確認
                        shutil.move(str(p_textPath.parent) + os.sep + nameX + '.pdf', dataSheetPath + os.sep + nameY) #ファイルの移動 #パスに'+'が使えないためstrに変換
                        os.remove(textDirPath + os.sep + nameX + '.txt')
                    
                    else:
                        n = nameX + '.pdf'
                        print('{} is already exist.'.format(n))
                    
        except FileNotFoundError:
            print('Unable to open textPath.')

if __name__ == "__main__":
    ReadText(textDirPath, dataSheetPath, nameDirPath)
    print('program finished')
