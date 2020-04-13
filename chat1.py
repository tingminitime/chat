
def read_file(fileName):
	lines = []
	with open(fileName, 'r', encoding='utf-8-sig')as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None # 避開第一行line不是人名
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: # 如果person有值
			new.append(person + ': ' + line)
	return new

def write_file(fileName, lines):
	with open(fileName, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines) # lines就是覆蓋再覆蓋
	write_file('output.txt', lines)

main()