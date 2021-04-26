import json
import urllib.parse
import random

emojified = {}
# letters
emojified['a'] = emojified['A'] = "\U0001F170";
emojified['b'] = emojified['B'] = "\U0001F171";
emojified['c'] = emojified['C'] = "\U0001F30A";
emojified['d'] = emojified['D'] = "\U0001F4D0";
emojified['e'] = emojified['E'] = "\U0001F300";
emojified['f'] = emojified['F'] = "\U0001F38F";
emojified['g'] = emojified['G'] = "\U0001F251";
emojified['h'] = emojified['H'] = "\U00002653";
emojified['i'] = emojified['I'] = "\U00002139";
emojified['j'] = emojified['J'] = "\U00002614";
emojified['k'] = emojified['K'] = "\U0001F985";
emojified['l'] = emojified['L'] = "\U0001F6F4";
emojified['m'] = emojified['M'] = "\U000024C2";
emojified['n'] = emojified['N'] = "\U00002651";
emojified['o'] = emojified['O'] = "\U00002B55";
emojified['p'] = emojified['P'] = "\U0001F17F";
emojified['q'] = emojified['Q'] = "\U0001F5E8";
emojified['r'] = emojified['R'] = "\U0001F44E";
emojified['s'] = emojified['S'] = "\U0001F4B2";
emojified['t'] = emojified['T'] = "\U0001F334";
emojified['u'] = emojified['U'] = "\U0001F918";
emojified['v'] = emojified['V'] = "\U00002648";
emojified['w'] = emojified['W'] = "\U0001F531";
emojified['x'] = emojified['X'] = "\U0000274C";
emojified['y'] = emojified['Y'] = "\U0001F331";
emojified['z'] = emojified['Z'] = "\U0001F40D";
# numbers
emojified['0'] = "\U0001F17E";
emojified['1'] = "\U00000031\U000020E3";
emojified['2'] = "\U0001F409";
emojified['3'] = "\U00000033\U000020E3";
emojified['4'] = "\U00000034\U000020E3";
emojified['5'] = "\U00000035\U000020E3";
emojified['6'] = "\U00000036\U000020E3";
emojified['7'] = "\U00000037\U000020E3";
emojified['8'] = "\U00000038\U000020E3";
emojified['9'] = "\U00000039\U000020E3";
#special characters
emojified['.'] = "\U000025AA";
emojified[','] = "\U0001F336";
emojified['?'] = "\U00002753";
emojified['!'] = "\U00002757";
emojified[':'] = "\U0001F6A6";
emojified[';'] = "\U0001F6D0";
emojified['\''] = "\U0001F4A7";
emojified['\"'] = "\U0001F38A";
#special characters todo
# emojified['~'] = "\U00000039";
# emojified['^'] = "\U00000039";
# emojified['$'] = "\U0001F4B2";
# emojified['@'] = "\U0001F4E7";
# emojified['&'] = "\U00000039";
# emojified['|'] = "\U00000039";
# emojified['/'] = "\U0001F58A";
# emojified['\\'] = "\U00000039";
# emojified['>'] = "\U00000039";
# emojified['<'] = "\U00000039";
# emojified['#'] = "\U00000023\U000020E3";
# emojified['_'] = "\U00000039";
# emojified['-'] = "\U00000039";
# emojified['='] = "\U00000039";
# emojified['+'] = "\U00002795";
# emojified['*'] = "\U0000002A\U000020E3";
# emojified['%'] = "\U00000039";
# emojified['('] = "\U000021AA";
# emojified[')'] = "\U000021A9";
# emojified['['] = "\U00000039";
# emojified[']'] = "\U00000039";
# emojified['{'] = "\U00000039";
# emojified['}'] = "\U00000039";

unemojified = {}

for key, value in emojified.items():
    unemojified[value] = key
    
flagged = {}
flagged['a'] = flagged['A'] = "\U0001F1E6";
flagged['b'] = flagged['B'] = "\U0001F1E7";
flagged['c'] = flagged['C'] = "\U0001F1E8";
flagged['d'] = flagged['D'] = "\U0001F1E9";
flagged['e'] = flagged['E'] = "\U0001F1EA";
flagged['f'] = flagged['F'] = "\U0001F1EB";
flagged['g'] = flagged['G'] = "\U0001F1EC";
flagged['h'] = flagged['H'] = "\U0001F1ED";
flagged['i'] = flagged['I'] = "\U0001F1EE";
flagged['j'] = flagged['J'] = "\U0001F1EF";
flagged['k'] = flagged['K'] = "\U0001F1F0";
flagged['l'] = flagged['L'] = "\U0001F1F1";
flagged['m'] = flagged['M'] = "\U0001F1F2";
flagged['n'] = flagged['N'] = "\U0001F1F3";
flagged['o'] = flagged['O'] = "\U0001F1F4";
flagged['p'] = flagged['P'] = "\U0001F1F5";
flagged['q'] = flagged['Q'] = "\U0001F1F6";
flagged['r'] = flagged['R'] = "\U0001F1F7";
flagged['s'] = flagged['S'] = "\U0001F1F8";
flagged['t'] = flagged['T'] = "\U0001F1F9";
flagged['u'] = flagged['U'] = "\U0001F1FA";
flagged['v'] = flagged['V'] = "\U0001F1FB";
flagged['w'] = flagged['W'] = "\U0001F1FC";
flagged['x'] = flagged['X'] = "\U0001F1FD";
flagged['y'] = flagged['Y'] = "\U0001F1FE";
flagged['z'] = flagged['Z'] = "\U0001F1FF";

unflagged = {}

for key, value in flagged.items():
    unflagged[value] = key
    
def emojify(s):
    res = ""
    for c in s:
        if c in emojified:
            res += emojified[c]
        else:
            res += c
    return res
    
def flagify(s):
    res = ""
    for c in s:
        if c in flagged:
            res += flagged[c]
        elif c in emojified:
            res += emojified[c]
        else:
            res += c
    return res

def capitalize(s):
    res = ""
    for c in s:
        if c.isalpha():
            cur = random.randint(0, 1)
            if cur == 1:
                res += c.upper()
            else:
                res += c.lower()
        else:
            res += c
    return res
    
def decode(s):
    res = ""
    for c in s:
        if c in unflagged:
            res += unflagged[c]
        elif c in unemojified:
            res += unemojified[c]
        else:
            res += c
    return res
    
def response(message, status_code):
    return {
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Methods": '*',
            "Access-Control-Allow-Credentials" : True
            },
        }
    
def lambda_handler(event, context):
    data = json.loads(event["body"])
    str = data["word"]
    cmd = data["action"]
    res = ""
    if cmd == "emojify":
        res = emojify(str)
    if cmd == "flagify":
        res = flagify(str)
    if cmd == "capitalize":
        res = capitalize(str)
    if cmd == "decode":
        res = decode(str)
        
    return response(json.dumps({"result": res}), 200)
