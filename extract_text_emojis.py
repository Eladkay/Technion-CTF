know_letters = {'🤘': ' ', '💪': 'a', '🐲':'i', '🌺':'t', '😃':'s', '✨':'b'}
original = '🤖🌺🍕🤖🐵🤘🤖🌺😞✨🖐😞🤘🐲🌺😃🤘👶🤖🌺😃🤘💪🍕'
next = '🤘😎💪👀🤘🐵🤖📽🎱🚩🤘😪💪🍕😎🤘🍕🍃🙂😎🎱😪'
'''
🤖🌺🍕🤖🐵 🕹🎱💪😎🐲🐵 🐲🌺😃 👶🤖🌺😃 💪🍕
it so is no 
💪🍕 -- am , it, is, in , as, at, if, 
😪💪🍕😎 

as
so
do




same
game
name
came

with
city
site

list

find
line
kind
mind

last
case
past
easy

data

life


🐲, 💪 -- a, i






--
👶🤖🌺😃 🍕😎💪👶 🕹🐲✨🐂 🍕👏 👿🤖 🎱🎵📽👏🌺😃🎵🙂🐂 2-7

'''


old_phrase = '🤘🤖🌺🍕🤖🐵🤘🕹🎱💪😎🐲🐵🤘🐲🌺😃🤘👶🤖🌺😃🤘💪🍕'

phrase = ''

for i in old_phrase:
    try:
        phrase += know_letters[i]
    except:
        phrase += i

print(phrase)
