# sortDataSheets
"sortDataSheets" is orgaize datasheets in your download folder.

# Demonstration

https://user-images.githubusercontent.com/64336110/177162959-eebcbd9d-7898-451c-83da-be7d4a71f942.mp4

# Features

When you are looking for electronic components, you should download datasheets. If you notice, datasheets piled up and feel lazy to separate them, aren't you? At such a time, this code will help you. 

This code converts datasheet pdf files to text files, then determines whether a "predifined reserved words" are included in the text file and classifies the type of datasheet.

# Requirement

This code uses only the standard libraries.

# Usage
Please installation unzip and place in the arbitrary folder.  
The resulting folder structure should look like this:  
    YourFolderName  
    ├── main ・・・Includes main.py and ReadText.py    
    ├── nameData ・・・Includes some text files. These files say "predifined reserved words"  

"target" folder is the place where the datasheets are placed after classification, so you can place anywhere you like.


Before using this code, you need to write downloadPath, dataSheetPath and nameDirPath on line 10 to 20 in the code.

```
#Begin setting. -------------------------------------------------  
    downloadPath = ""  
    dataSheetPath = ""  
    nameDirPath = ""  
#End setting. ---------------------------------------------------
```

* downloadPath ・・・Datasheet download path  
* dataSheetPath ・・・Destination path of the sorted datasheets  
* nameDirPath ・・・Reserved word folder path   


# Author

Nanraka
