import re
from bs4 import BeautifulSoup

def formatting(content):
	regex  = re.compile('#.*#')
	paragraphs = [i.replace('\n', '') for i in content.split('-') if i]
	images = [paragraph.group().replace(' ', '').strip('#') for paragraph in paragraphs for paragraph in re.finditer(regex, paragraph)]

	all_paragraphs = []
	for paragraph in paragraphs:
		paragraph = paragraph.replace('#', '#\n')
		paragraph = paragraph.replace('#', '').strip()
		paragraph = paragraph.split('\n')

		if len(paragraph) > 1:
			for i in range(len(paragraph)):
				all_paragraphs.append([paragraph[i]])
		else:
			all_paragraphs.append(paragraph)

	all_paragraphs = [i for i in all_paragraphs if i[0]]

	final_html = ''
	for i in all_paragraphs:
		if (i[0]).strip() in images:
			formated_image = f'<p class="mt-5 mb-5"><a href="/media/aboutpage/images/{i[0].strip()}" target="_blank"><img src="/media/aboutpage/images/{i[0].strip()}" alt="" class="img-fluid"></a></p>'
			final_html += formated_image
		else:
			formated_paragraph = f'<p class="text-justify">{i[0].strip()}</p>'
			final_html += formated_paragraph

	final_html = BeautifulSoup(final_html, 'html.parser').prettify()
	return final_html


def formatting_(content):
	regex  = re.compile('#.*#')
	paragraphs = [i.replace('\n', '') for i in content.split('-') if i]
	images = [paragraph.group().replace(' ', '').strip('#') for paragraph in paragraphs for paragraph in re.finditer(regex, paragraph)]

	all_paragraphs = []
	for paragraph in paragraphs:
		paragraph = paragraph.replace('#', '#\n')
		paragraph = paragraph.replace('#', '').strip()
		paragraph = paragraph.split('\n')

		if len(paragraph) > 1:
			for i in range(len(paragraph)):
				all_paragraphs.append([paragraph[i]])
		else:
			all_paragraphs.append(paragraph)

	all_paragraphs = [i for i in all_paragraphs if i[0]]

	final_html = ''
	for i in all_paragraphs:
		if (i[0]).strip() in images:
			formated_image = f'<p><a href="/media/blogpage/images/{i[0].strip()}" target="_blank"><img src="/media/blogpage/images/{i[0].strip()}" alt="" class="img-fluid"></a></p>'
			final_html += formated_image
		else:
			formated_paragraph = f'<p class="text-justify">{i[0].strip()}</p>'
			final_html += formated_paragraph

	final_html = BeautifulSoup(final_html, 'html.parser').prettify()
	return final_html
