# python扫码统计
一个使用python构建的图形化扫码统计应用

## 如何使用

### 系统支持

使用此程序，请首先确保您的设备装有摄像头，并安装python3.7（理论上python3.5、python3.6也可以使用，未测试）

使用pip安装一下库：

- opencv-python
- pyzbar
- csv
- time
- threading
- tkinter

### 文件输入

所有名单应放置在 `/dict` 文件夹中，并命名为 `xxxx.txt`

名单建议由Excel `文件>导出>制表符分隔txt文件`

并形似：
``` 
编号1 名称a
编号2 名称b
编号3 名称c
```

## 
