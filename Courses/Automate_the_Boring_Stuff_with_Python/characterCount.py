import pprint
msg = 'Uma mensagem para estes dias'
count = {}

for character in msg:
	count.setdefault(character, 0)
	count[character] = count[character] + 1
pprint.pprint(count)
