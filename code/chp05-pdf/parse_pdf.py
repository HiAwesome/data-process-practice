# coding=utf-8
"""
    slate 需要依赖 PDFParser 这个库

    Mac OS 安装 PDFParser 需要先安装 poppler => brew install poppler
    参考这里 https://stackoverflow.com/a/53967295

    slate 需要依赖 pdfminer 这个库

    python2 提供的版本为 pdfminer.six => pip install pdfminer.six
    参考这里 https://pypi.org/project/pdfminer/

    根据书中特定版本的指示运行成功 => pip install slate==0.3 pdfminer==20110515
    参考这里 https://github.com/timClicks/slate/issues/5#issuecomment-53450633
"""
import slate

with open('../../data/chp5/EN-FINAL Table 9.pdf') as f:
    doc = slate.PDF(f)

for page in doc[:2]:
    print page
