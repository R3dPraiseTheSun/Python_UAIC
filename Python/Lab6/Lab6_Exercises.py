from Lab6_Functions import extract_words, ex_2, ex_3, ex_4, ex_5, ex_6, ex_7, ex_8


# Ex_1
print('Ex1:', extract_words("text, ana, are mere"))

# Ex_2
print('Ex2:', ex_2(r"\w+", "text, ana, are mere", 3))

# Ex_3
print('Ex3:',ex_3(["text, are mere", "ana, 0753355294"], [r"\b\w{3}\b", r"075\d{7}", ]))

# Ex_4
print('Ex4:',ex_4("example.xml", {"class": "url", "name": "url-form", "data-id": "item"}))

# Ex_5
print('Ex5:',ex_5("example.xml", {"class": "url", "name": "url-form", "data-id": "item"}))

# Ex_6
print('Ex6:',ex_6("absefgei ara ara cha"))

# Ex_7
print('Ex7:',ex_7("1730110155203"))

# Ex_8
print('Ex8:',ex_8(".", ".*example.*"))
