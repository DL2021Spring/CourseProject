import os
import re






entities = ['Ingredient','Amount','Unit','Recipe']
auto_tag_set = []
nonauto_tag_set = []

def init_dict(dictOfdict):
	for e in entities:
		if not (e in dictOfdict):
			dictOfdict[e] = dict()

def get_xml_content(file_path):
	f = open(file_path)
	content = f.read()
	content = pre_format(content)
	return get_xml_entity(content)

def get_ann_content(file_path):
	f = open(file_path)
	content = f.read()
	return get_ann_entity(content)

def process_files_in_dir(dir):
	dir = os.path.dirname(os.path.realpath(__file__)) + ('/'+dir)
	for root, dirs, files in os.walk(dir):
		for file in sorted(files):
			if(file.endswith('.xml')):
				auto_tag_set.append(get_xml_content(os.path.join(root,file)))
			if(file.endswith('.ann')):
				nonauto_tag_set.append(get_ann_content(os.path.join(root,file)))

def get_ann_entity(content):
	entity_dict = dict()
	init_dict(entity_dict)
	content = content.split('\n')
	for line in content:
		token = line.split('\t')
		if("T" in token[0]):
			tag_name = token[1].split(' ')[0]
			if(token[2] in entity_dict[tag_name]):
				entity_dict[tag_name][token[2]] += 1
			else:
				entity_dict[tag_name][token[2]] = 1
	return entity_dict


def get_xml_entity(content):
	entity_dict = dict()
	init_dict(entity_dict)
	for e in entities:
		e_reg = re.compile('<'+e + '>(?P<'+e+'>[^<]+)</'+e+'>');
		for i in e_reg.findall(content):
			if(i in entity_dict[e]):
				entity_dict[e][i] += 1
			else:
				entity_dict[e][i] = 1
	return entity_dict

def pre_format(content):

	
	content = re.sub("<entity type=\"(\w+)\">([^<]+)</entity>", "<\g<1>>\g<2></\g<1>>", content)
	
	content = content.replace("<s>", "")
	content = content.replace("</B-Ingredient> <I-Ingredient>", " ")
	content = content.replace("</I-Ingredient> <I-Ingredient>", " ")
	content = content.replace("</B-Recipe> <I-Recipe>", " ")
	content = content.replace("</I-Recipe> <I-Recipe>", " ")
	content = content.replace("</B-Amount> <I-Amount>", " ")
	content = content.replace("</I-Amount> <I-Amount>", " ")
	content = content.replace("</B-Unit> <I-Unit>", " ")
	content = content.replace("</I-Unit> <I-Unit>", " ")
	content = content.replace("</I-", "</")
	content = content.replace("</B-", "</")
	content = content.replace("<B-", "<")
	content = content.replace("<I-", "<")

	return content

def calc_diff_by_entity(nonauto_tag_set,auto_tag_set):
	diff_matrix = dict()
	init_dict(diff_matrix)
	for key, value in diff_matrix.iteritems():
		value['FP'] = 0
		value['TP'] = 0
		value['FN'] = 0

	for article in zip(nonauto_tag_set,auto_tag_set):
		for entity in entities:
			for key, value in article[0][entity].iteritems():
				if key in article[1][entity]:
					if article[1][entity][key] - value > 0:
						diff_matrix[entity]['FP'] += (article[1][entity][key] - value)
					else: 
						diff_matrix[entity]['FN'] += (value - article[1][entity][key])
					diff_matrix[entity]['TP'] += min(article[1][entity][key],value)
				else:
					diff_matrix[entity]['FN'] += value
			for key, value in article[1][entity].iteritems():
				if not key in article[0][entity]:
					diff_matrix[entity]['FP'] += value

	return diff_matrix

process_files_in_dir('tagged_data')
confusion_matrix = calc_diff_by_entity(nonauto_tag_set,auto_tag_set)
for key, value in confusion_matrix.iteritems():
	if value['TP'] == 0:
		precision = 0
		recall = 0
		f_measure = 0
	else:
		precision = 1.0 * value['TP'] / (value['TP'] + value['FP'])
		recall = 1.0 * value['TP'] / (value['TP'] + value['FN'])
		f_measure = 2.0 * (precision * recall)/(precision + recall)

	print key+':\tPrecision-'+str("{0:.4f}".format(precision))+'\tRecall-'+str("{0:.4f}".format(recall))+'\tF-measure-'+str("{0:.4f}".format(f_measure))



