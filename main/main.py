#cording:utf-8
import os
import sys
import shutil
import subprocess
import ReadText as rt



#Begin setting. -------------------------------------------------
#データシートをダウンロードした場所のパス
downloadPath = ""

#ソート後のデータシートの保存先パス
dataSheetPath = ""

#予約語フォルダのパス
nameDirPath = ""
#End setting. ---------------------------------------------------



#データシートをダウンロードしたディレクトリが空かどうかの確認1（指定されたディレクトリがないとき，ディレクトリを勝手に作る）
if os.path.isdir(downloadPath) is not True:
    os.mkdir(downloadPath)
    print("There are no files in the directory.")
    print("Please set files in the directory.")
    sys.exit(1)



#データシートをダウンロードしたディレクトリが空かどうかの確認2
files = os.listdir(downloadPath)
if len(files) == 0:
    print("There are no files in the directory.")
    print("Please set files in the directory.")
    sys.exit(1)



#テキストファイルの作成
textDirectory = downloadPath + os.sep + 'text'
if os.path.isdir(textDirectory) is not True:
    os.mkdir(textDirectory)
textPath = downloadPath + os.sep + 'text'
    


#pdfからテキスト抽出
def pdfToText(downloadPath):
    for x in files:
        s = downloadPath + os.sep + x
        try:
            #pdftotextの実行
            res = subprocess.run('pdftotext -q -enc UTF-8 {}'.format(s), shell=True) #format()によって任意の文字列を''の中に代入
            name = os.path.splitext(os.path.basename(x))[0] #演算子抜きのファイル名を表示
            
        except:
            print('Eroor: Can not convert pdf into text.')



#テキストファイルの移動
def moveText(downloadPath):
    files = os.listdir(downloadPath)
    for x in files:
        s = downloadPath + os.sep + x
        name = os.path.splitext(os.path.basename(x))[0]
        root, ext = os.path.splitext(s) #root=path #ext=拡張子
        if ext == '.txt':
            shutil.move(root + ext, textPath + os.sep + name + ext)



#ディレクトリが空であるか確認
def emptyDir(directory):
    files = os.listdir(directory)
    files = [file for file in files if not file.startswith('.')]
    if not files:
        return True
    else:
        return False


#run function
if __name__ == "__main__":
    pdfToText(downloadPath)
    moveText(downloadPath)
    rt.ReadText(textDirectory, dataSheetPath, nameDirPath)
    
    if emptyDir(textDirectory) == True:
        os.removedirs(textDirectory)
        
    print('Program finished.')
