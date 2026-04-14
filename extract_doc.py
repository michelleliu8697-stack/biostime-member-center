# -*- coding: utf-8 -*-
import zipfile
import xml.etree.ElementTree as ET
import re

docx_path = r'D:/michelle.liu.luci.喵/品牌/合生元/合生元京东会员中心策划方案0413(1)(5).docx'
output_path = r'e:/workbuddy/biostime-member-center/new-plan.txt'

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

text_parts = []

with zipfile.ZipFile(docx_path, 'r') as z:
    xml_content = z.read('word/document.xml')
    
tree = ET.fromstring(xml_content)

for elem in tree.iter():
    tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
    if tag == 't' and elem.text:
        text_parts.append(elem.text)
    elif tag == 'p':
        text_parts.append('\n')
    elif tag == 'tab':
        text_parts.append('\t')

full_text = ''.join(text_parts)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(full_text)

print(f"Extracted {len(full_text)} characters to {output_path}")
