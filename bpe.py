import os
import json
import regex as re
from functools import lru_cache

# fix indentation
def fix_Indent(parsed: List[tokenizer.ParsedToken]) -> List[tokenizer.ParsedToken]:
    res: List[tokenizer.ParsedToken] = []
    indentation = 0
    indented = False
    for t in parsed:
        if t.type == tokenizer.TokenType.indent:
            indentation += 1
        elif t.type == tokenizer.TokenType.dedent:
            indentation -= 1
        elif t.type in [tokenizer.TokenType.new_line,
                        tokenizer.TokenType.eof]:
            indented = False
            res.append(t)
        else:
            if not indented:
                for _ in range(indentation):
                    res.append(tokenizer.ParsedToken(tokenizer.TokenType.indent, 0))
                indented = True

            res.append(t)
    return res

# remove empty lines
def fix_Lines(parsed: List[tokenizer.ParsedToken]) -> List[tokenizer.ParsedToken]:
    tokens = [tokenizer.TokenType.new_line, tokenizer.TokenType.new_line]
    res = []
    for p in parsed:
        for i in range(1):
            tokens[i] = tokens[i + 1]
        tokens[-1] = p.type
        all_new_line = True
        for t in tokens:
            if t != tokenizer.TokenType.new_line:
                all_new_line = False

        if all_new_line:
            continue
        else:
            res.append(p)

    return res   

# converting bytes to unicode
def bytes_to_unicode():
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]
    n = 0
    for b in range(2 ** 8):
        if b not in bs:
            bs.append(b)
            cs.append(2 ** 8 + n)
            n += 1
    cs = [chr(n) for n in cs]
    return dict(zip(bs, cs))


# group the input into pairs of characters
def get_pairs(word):
    pairs = set()
    prev_char = word[0]
    for char in word[1:]:
        pairs.add((prev_char, char))
        prev_char = char
    return pairs

# self-defined class
class Encoder:
    def __init__(self, encoder, bpe_merges):
        self.encoder = encoder
        self.decoder = {v: k for k, v in self.encoder.items()}
        self.byte_encoder = bytes_to_unicode()
        self.byte_decoder = {v: k for k, v in self.byte_encoder.items()}
        self.bpe_ranks = dict(
            zip(bpe_merges,
                range(len(bpe_merges))))
        self.cache = {}

    # identify foreign words
    def bpe(self, token):
        # check if already have or not
        if token in self.cache:
            return self.cache[token]

        word = tuple(token) 
        pairs = get_pairs(word)

        # too short for tearing
        if not pairs:
            return token

        while True:  
            bigram = min(pairs, key=lambda pair: self.bpe_ranks.get(pair, float('inf'))) 

            if bigram not in self.bpe_ranks:
                break

            first, second = bigram  
            new_word = []
            i = 0
            while i < len(word):
                try:
                    j = word.index(first, i)  
                    new_word.extend(word[i:j])  
                    i = j  
                except:
                    new_word.extend(word[i:])  
                    break

                if word[i] == first and i < len(word) - 1 and word[i + 1] == second:
                    new_word.append(first + second)
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1
                    
            new_word = tuple(new_word)
            word = new_word
            
            if len(word) == 1:
                break
            else:
                pairs = get_pairs(word)
        word = ' '.join(word)
        self.cache[token] = word
        return word

    # for not stored words
    def encode(self, text):
        bpe_tokens = []
        token = ''.join(self.byte_encoder[b] for b in text.encode('utf-8'))
        bpe_tokens.extend(self.encoder[bpe_token] for bpe_token in self.bpe(token).split(' '))
        return bpe_tokens

    def decode(self, tokens):
        text = ''.join([self.decoder[token] for token in tokens])
        text = bytearray([self.byte_decoder[c] for c in text]).decode('utf-8')
        return text


def get_encoder(model_name, models_dir):
    with open(os.path.join(models_dir, model_name), 'r') as f:
        encoder = json.load(f)
    with open(os.path.join(models_dir, model_name), 'r', encoding="utf-8") as f:
        bpe_data = f.read()
    bpe_merges = [tuple(merge_str.split()) for merge_str in bpe_data.split('\n')[1:-1]]
    return Encoder(
        encoder=encoder,
        bpe_merges=bpe_merges
    )


optimizer = tf.keras.optimizers.Adam(learning_rate=3e-5, epsilon=1e-08, clipnorm=1.0)
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
metric = tf.keras.metrics.SparseCategoricalAccuracy('accuracy')
model.compile(optimizer=optimizer, loss=[loss, *[None] * model.config.n_layer], metrics=[metric])    
