





import re
import operator
import os

BASE_DIR = (os.path.dirname(os.path.abspath(__file__)))

debug = False


def is_number(s):
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False


def load_stop_words(stop_word_file):
    
    stop_words = []
    for line in open(stop_word_file):
        if line.strip()[0:1] != "#":
            for word in line.split():  
                stop_words.append(word)
    return stop_words


def separate_words(text, min_word_return_size):
    
    splitter = re.compile(r'[^a-zA-Z0-9_\+\-/]')
    words = []
    for single_word in splitter.split(text):
        current_word = single_word.strip().lower()
        
        if len(current_word) > min_word_return_size and current_word != '' and not is_number(current_word):
            words.append(current_word)
    return words


def split_sentences(text):
    
    sentence_delimiters = re.compile(r'[!\?;:\[\]\t\"\(\)]|\s\-\s|[^0-9],[^a-zA-Z0-9]|\.[^a-zA-Z0-9]|\.$')
    sentences = sentence_delimiters.split(text)
    return sentences


def build_stop_word_regex(stop_word_file_path):
    stop_word_list = load_stop_words(stop_word_file_path)
    stop_word_regex_list = []
    for word in stop_word_list:
        word_regex = r'\b'+word+r'(?![\w-])'  
        stop_word_regex_list.append(word_regex)
    stop_word_pattern = re.compile('|'.join(stop_word_regex_list), re.IGNORECASE)
    return stop_word_pattern


def generate_candidate_keywords(sentence_list, stopword_pattern):
    phrase_list = []
    for s in sentence_list:
        tmp = re.sub(stopword_pattern, '|', s.strip())
        phrases = tmp.split("|")
        for phrase in phrases:
            phrase = phrase.strip().lower()
            if phrase != "":
                phrase_list.append(phrase)
    return phrase_list


def calculate_word_scores(phraseList):
    word_frequency = {}
    word_degree = {}
    for phrase in phraseList:
        word_list = separate_words(phrase, 0)
        word_list_length = len(word_list)
        word_list_degree = word_list_length-1
        
        for word in word_list:
            word_frequency.setdefault(word, 0)
            word_frequency[word] += 1
            word_degree.setdefault(word, 0)
            word_degree[word] += word_list_degree  
            
    for item in word_frequency:
        word_degree[item] = word_degree[item]+word_frequency[item]

    
    word_score = {}
    for item in word_frequency:
        word_score.setdefault(item, 0)
        word_score[item] = word_degree[item]/(word_frequency[item]*1.0)  
    
    return word_score


def generate_candidate_keyword_scores(phrase_list, word_score):
    keyword_candidates = {}
    for phrase in phrase_list:
        keyword_candidates.setdefault(phrase, 0)
        word_list = separate_words(phrase, 0)
        candidate_score = 0
        for word in word_list:
            candidate_score += word_score[word]
        keyword_candidates[phrase] = candidate_score
    return keyword_candidates


class Rake(object):
    def __init__(self, stop_words_path=os.path.join(BASE_DIR, "SmartStoplist.txt")):
        self.stop_words_path = stop_words_path
        self.__stop_words_pattern = build_stop_word_regex(stop_words_path)

    def run(self, text):
        sentence_list = split_sentences(text)

        phrase_list = generate_candidate_keywords(sentence_list, self.__stop_words_pattern)

        word_scores = calculate_word_scores(phrase_list)

        keyword_candidates = generate_candidate_keyword_scores(phrase_list, word_scores)

        sorted_keywords = sorted(keyword_candidates.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sorted_keywords


if __name__ == "__main__":
    text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types of systems and systems of mixed types."

    
    sentenceList = split_sentences(text)
    
    stoppath = os.path.join(BASE_DIR, "SmartStoplist.txt")  
    stopwordpattern = build_stop_word_regex(stoppath)

    
    phraseList = generate_candidate_keywords(sentenceList, stopwordpattern)

    
    wordscores = calculate_word_scores(phraseList)

    
    keywordcandidates = generate_candidate_keyword_scores(phraseList, wordscores)
    if debug: print keywordcandidates

    sortedKeywords = sorted(keywordcandidates.iteritems(), key=operator.itemgetter(1), reverse=True)
    if debug: print sortedKeywords

    totalKeywords = len(sortedKeywords)
    if debug: print totalKeywords
    print sortedKeywords[0:(totalKeywords/3)]

    rake = Rake(stoppath)
    keywords = rake.run(text)
    print keywords
