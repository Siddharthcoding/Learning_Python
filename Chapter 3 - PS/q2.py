letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Siddharth").replace("<|Date|>", "21st May 2025"))