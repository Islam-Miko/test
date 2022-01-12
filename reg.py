text = """
Java et ultrices ex. Proin ac dignissim eros.
Phasellus consequat nisi ut mauris laoreet,
vel dapibus risus ultrices. Donec cursus
nunc scelerisque eros python23 porta.
Suspendisse potenti.  molestie
sollicitudin nisl, id imperdiet tellus
consectetur a. Nulla aliquet, lorem sit
amet  imperdiet, mi neque ultricies enim,
at 22python libero nunc non metus. Integer rutrum auctor pretium.
In tincidunt sed nisl et pharetra. Fusce consequat sapien eget dolor
ultricies, id vestibulum diam facilisis.

Aenean fermentum, ex in pulvinar lobortis, tellus metus elementum sem, a ultrices lectus erat eu nisl.
Sed aliquet lorem vel neque mattis consequat. Nullam tortor dolor, +996777845123 lorem vitae, porttitor dignissim mauris.
Integer tempor arcu quis lorem varius egestas. Vestibulum python euismod urna eu mollis. Nullam consequat facilisis 
pulvinar. Integer vehicula java varius semper.

Duis consequat elit id eleifend laoreet. Praesent tempor tellus sed
turpis vestibulum pulvinar aliev91@gmail.com. Suspendisse congue viverra elit. Vivamus
fermentum pharetra laoreet. 996555784512 at venenatis nisl. Maecenas
sapien dui, laoreet ac enim non, imperdiet vulputate massa. In nec
velit vestibulum, pellentesque neque ac, venenatis nulla. Curabitur 
dui ipsum, 0555424578 vitae dapibus sed, maximus id justo. Suspendisse
ac sollicitudin risus, et venenatis felis.

456-1231-4565
456 1231 4595
456*1231*4545
456.1231.4515
456/1231/4115
456-231-4569
"""
tokenn = "token1:1234567.996555504512+almaz.kg"
tokens = [
    "token1:1234567.996555504512+almaz.kg",
    "token2:1634567.996555518512+kiyan.ru",
    "token3:4534567.996555334512+kim.usa",
    "token4:1234567.996500504512+alym.ru",
    "token5:1211567.996772504512+erbol.kz",
    "token6:9934567.996559504512+erlan.uz"
]

ids = """
id:123
id:124
id:1980
id:456
id:00213
id:1123123
id:34534
id:890
"""
numbers = [
    '123123',
    '234456',
    '234432',
    '678090',
    '111215',
    '234439',
    '234222',
    '234787',
]

import re


def get_ids():
    pattern = re.compile(r"id:\d{3}")
    all_true_ids = pattern.findall(ids)
    print(all_true_ids)


def find_pj():
    pattern = re.compile(r'\d{3}[./ -]\d{4}[./ -]\d{4}')
    result = pattern.findall(text)
    print(result)


def validate_number(number: str) -> bool:
    pattern = re.compile(r"[+]?996\d{9}$")
    result = pattern.match(number)
    if result is None:
        return False

    return True
validate_number('996772898989')

def get_code():
    new = []
    pattern = re.compile(r'2\d\d\d\d7')
    print(numbers)
    for num in numbers:
        mat = pattern.match(num)
        if mat is not None:
            new.append(num)
    print(new)


# def number(num):
#     pattern = re.compile(r'1\d{5}')
#     return pattern.match(num) is not None


def token_decode(text):
    pattern = re.compile(r'[.:+]')
    result = pattern.split(text)
    return result


def tokens_decode(list_tokens):
    pattern = re.compile(r'[.:+]')
    names_numbers = []
    for token in list_tokens:
        # t, id, number, name, country = pattern.split(token)
        *head, number, name, country = pattern.split(token)
        couple = (number, name)
        names_numbers.append(couple)
    return names_numbers


result_token = tokens_decode(tokens)



def code_re(char):
    codes = {
        'a': '1',
        'e': '2',
        'i': '3',
        'o': '4',
        'u': '5'
    }
    return codes.get(char.group())

# text = 'a23 + u234 - 67i'


def code(text):
    pattern = re.compile(r'[aeiou]')
    new_str = pattern.sub(code_re, text)
    print(new_str)



html = """
<a href='sdfasdf'>Click me!</a>
<div class='ok'>
<p>python is pl</p>
<p class='ok'>python is pl2</p>
</div>
"""

def findbytag(text):
    pattern = re.compile(r"<p class='ok'>.+</p>")
    result = pattern.findall(text)
    print(result)

findbytag(html)