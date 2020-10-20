# Python学习笔记
1.Python的文件路径  
问题描述：使用windows路径格式打开文件时报错  
报错原因：windows文件路径中的"\"被认为是转义字符  

Python中描述路径的方式  

方式一:转义的方式

`'d:\\a.txt'`

方式二:显式声明字符串不用转义

`'d:r\a.txt'`

方式三:使用Linux的路径/

`'d:/a.txt'`
