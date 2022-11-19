# symbol_convert 

**目前：**
1. 用于文本清洗中将中文符号转换为英文符号 
2. 全角符号转换为半角符号

---
## 安装
可以直接 `pip` 安装
> pip install symbol_convert


### demo
```text
from symbol_convert import convert

str = '这是一个，【个人】ｄｅｂｏｋｅ：'
en_str = convert(str)
print(str)
print(en_str)
> 这是一个，【中文】ｄｅｂｏｋｅ：
> 这是一个,[中文]deboke:
```

## 版本历程
详见 [history.md](https://github.com/Caaby/symbol_convert/blob/master/docs/history.md)

