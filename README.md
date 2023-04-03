# YGOpro-s2tw

YGOpro Simplified Chinese to Traditional Chinese  
![圖示](icons/icon.png)  

## 說明

此工具用來翻譯簡體中文版的YGOpro文字  
步驟:  

1. 選擇cards.cdb(卡牌資料庫)
2. 翻譯完成產生cardscards.cdb.cdb(備分原資料庫)
3. 選擇strings.conf(系統文字)
4. 翻譯完成產生strings_backup.conf(備分原系統文字)

## 建置說明  

```bash
pip install -r requirements.txt
```

```bash
pyinstaller YGOpro_s2tw.spec 
```  

由於繁轉簡函數本身有路徑問題，建置時請參閱  
[pyinstaller opencc 打包exe出错提示](https://blog.csdn.net/qq_42347124/article/details/125251959)
