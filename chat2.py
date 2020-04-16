# LINE對話紀錄裡講了幾個字、幾個圖片

def read_file(fileName):
	lines = []
	with open(fileName, 'r', encoding='utf-8-sig')as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None # 避開第一行line不是人名

	allen_word_count = 0
	allen_sticker_count = 0
	allen_img_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_img_count = 0

	for line in lines:
		s = line.split(' ') # 切割完會變清單
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_img_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_img_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)

	print('allen說了', allen_word_count, '個字，傳了', allen_sticker_count, '個貼圖和', allen_img_count, '個圖片')
	print('viki說了', viki_word_count, '個字，傳了', viki_sticker_count, '個貼圖和', viki_img_count, '個圖片')
		# print(s)
	return new

def write_file(fileName, lines):
	with open(fileName, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines) # lines就是覆蓋再覆蓋
	# write_file('output.txt', lines)

main()