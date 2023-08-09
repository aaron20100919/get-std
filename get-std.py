import re
import requests
import urllib.parse
import webbrowser
import pyautogui
import pyperclip

baseUrl = 'http://cn.bing.com/search?'
word = input("what's you want to search? ")
word = word[:min(len(word), 30)] + ' c++ csdn'
print(word)
word = word.encode(encoding='utf-8', errors='strict')

data = {'q': word}
data = urllib.parse.urlencode(data)

url = baseUrl+data
print(url)

r = requests.get(url)

m = re.compile(r'href="(https://blog\.csdn\.net.+?)"')

blogs = m.findall(r.content.decode())
codes = []

for blog in blogs[:min(3, len(blogs))]:
    webbrowser.open(blog)
    pyautogui.sleep(2)
    pyautogui.hotkey('ctrl', 'shift', 'j')
    pyperclip.copy("document.body.contentEditable = 'true'")
    pyautogui.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.click(600, 600)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'x')
    pyautogui.hotkey('ctrl', 'w')

    s = pyperclip.paste()
    s = re.sub(r'[\u4e00-\u9fff]+', '', s)
    code_match = re.compile('(#[\u0000-\u007f\r\n]*})[\r\n]{1,4}\\d+')

    code = code_match.findall(s)
    codes.append(code)


cnt = 0
for code in codes:
    with open('tijie%d.cpp' % cnt, 'w') as f:
        f.write(''.join(code))
    cnt += 1
