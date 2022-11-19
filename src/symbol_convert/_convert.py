# -*- coding: UTF_8 -*-

import re

def convert(string: str) -> str:
    """中文特殊符号转英文特殊符号"""

    #中文特殊符号批量识别
    pattern = re.compile('[。“”【】《》、‘’『』「」﹃﹄〔〕—·]')
    
    #re.compile: 编译一个正则表达式模式，返回一个模式（匹配模式）对象。
    #[...]用于定义待转换的中文特殊符号字符集

    #re.findall: 搜索string，以列表形式返回全部能匹配的子串。
    fps = re.findall(pattern, string)

    #对有中文特殊符号的文本进行符号替换
    if len(fps):
        string = string.replace('。', '.')
        string = string.replace('“', '"')
        string = string.replace('”', '"')
        string = string.replace('【', '[')
        string = string.replace('】', ']')
        string = string.replace('《', '<')
        string = string.replace('》', '>')
        string = string.replace('、', ',')
        string = string.replace('‘', "'")
        string = string.replace('’', "'")
        string = string.replace('『', "[")
        string = string.replace('』', "]")
        string = string.replace('「', "[")
        string = string.replace('」', "]")
        string = string.replace('﹃', "[")
        string = string.replace('﹄', "]")
        string = string.replace('〔', "{")
        string = string.replace('〕', "}")
        string = string.replace('—', "-")
        string = string.replace('·', ".")
    
    """全角转半角"""
    #转换说明：
    #全角字符unicode编码从65281~65374 （十六进制 0xFF01 ~ 0xFF5E）
    #半角字符unicode编码从33~126 （十六进制 0x21~ 0x7E）
    #空格比较特殊，全角为 12288（0x3000），半角为 32（0x20）
    #除空格外，全角/半角按unicode编码排序在顺序上是对应的（半角 + 0x7e= 全角）,所以可以直接通过用+-法来处理非空格数据，对空格单独处理。

    rstring = ""
    for uchar in string:
        inside_code = ord(uchar)
        if inside_code == 12288:                                #全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):   #全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring


if __name__ == "__main__":
    old_str = '这是一个，【个人】ｄｅｂｏｋｅ：'
    en_str = convert(old_str)
    print(old_str)
    print(en_str)

