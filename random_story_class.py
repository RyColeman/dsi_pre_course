import random
import string
from collections import Counter, defaultdict
import sys

class RandomStory():
    def __init__(self,f,n_grams=2):
        self.file = f
        self.n_grams = n_grams
        self.story = ''
        self.word_dict = {}

    def train(self):
        if self.n_grams == 1:
            self.word_dict = self.unigrams()
        elif self.n_grams == 2:
            self.word_dict = self.bigrams()
        elif self.n_grams == 3:
            self.word_dict = self.trigrams()
        else:
            print('Error: n_grams parameter needs to be 1, 2 or 3')


    def generate(self, num_words):
        self.story = self.make_random_story(num_words)

    def make_random_story(self, num_words=200):
        '''
        INPUT: file, integer, interger
        OUTPUT: string

        Call n_grams (unigrams, bigrams or trigrams for n_gram set at 1, 2 or 3) on
        file f and use the resulting dictionary to randomly generate text with
        num_words total words.

        Choose the next word by using random.choice to pick a word from the list
        of possibilities given the (n_gram - 1) previous words.

        Use join method to turn a list of words into a string.

        Example:
        >>> # Seed the random number generator for consistent results
        >>> random.seed('Is the looking-glass is half full or half-empty?')
        >>> # Generate a random story
        >>> with open('../data/alice.txt') as f:
        ...     story = make_random_story(f, 2, 10)
        ...     story
        stick, and tumbled head over heels in its sleep 'twinkle,
        >>> len(story.split())  # Verify story length is 10 words
        10
        '''

        if self.n_grams == 1:
            new_string = []

            for n in range(num_words):
                new_string.append(random.choice(self.word_dict[()]))

            return ' '.join(new_string)

        elif self.n_grams == 2:
            new_string = []
            new_word = random.choice(self.word_dict.keys())[0]
            new_string.append(new_word)

            for n in range(num_words-1):


                new_word = random.choice([next_word_list for word, next_word_list in self.word_dict.items() if word[0] == new_string[-1]][0])
                new_string.append(new_word)
            return ' '.join(new_string)

        elif self.n_grams == 3:
            new_string = []
            new_word_tup = random.choice(self.word_dict.keys())
            new_string.append(new_word_tup[0])
            new_string.append(new_word_tup[1])

            for n in range(num_words -2):
                new_word = random.choice(random.choice([next_word_list for word_tup, next_word_list in self.word_dict.items() if word_tup == (new_string[-2], new_string[-1])]))

                new_string.append(new_word)

            return ' '.join(new_string)


    def unigrams(self):
        '''
        INPUT: file
        OUTPUT: dictionary

        Return a dictionary where the key is an empty tuple and the only value is
        the list of all words in the file, words should appear as many times as
        they occur in the document.

        You should lowercase everything.
        Use strip and string.punctuation to strip the punctuation from the words.

        Example:
        >>> with open('../data/example.txt') as f:
        ...     d = unigrams(f)
        >>> d[()]
        ['the', 'cat', 'chased', 'the', 'dog']
        '''
        with open(self.file) as f:

            return {() : [word.strip(string.punctuation).lower() for line in f for word in line.split()]}

    def bigrams(self):
        '''
        INPUT: file
        OUTPUT: dictionary

        Return a dictionary where the keys are tuples of a single word in
        the file and the value for each key is a list of words that were found
        directly following the key.

        You should lowercase everything.
        Use strip and string.punctuation to strip the punctuation from the words.

        Words should be included in the list the number of times they appear.

        Suggestions on how to handle first words: create an entry in the dictionary
        with a first key None.

        Example:
        >>> with open('../data/alice.txt') as f:
        ...     d = bigrams(f)
        >>> d[('among', )]
        ['the', 'those', 'them', 'the', 'the', 'the', 'the', 'the', 'the', 'mad', 'the', 'them']
        '''
        with open(self.file) as f:

            word_list = [word.strip(string.punctuation).lower() for line in f for word in line.split()]

            # bi_dict = defaultdict(list)
            bi_dict = {}
            for i, word in enumerate(word_list):
                if (word,) not in bi_dict.keys():
                # if bi_dict[(word,)] == []:
                    if i != len(word_list)-1:
                        # bi_dict[(word,)].append([w for j, w in enumerate(word_list[1:]) if word_list[j] == word])
                        bi_dict[(word,)] = [w for j, w in enumerate(word_list[1:]) if word_list[j] == word]

            # bi_dict.update({(None,) : []})

            return bi_dict

    def trigrams(self):
        '''
        INPUT: file
        OUTPUT: dictionary

        Return a dictionary where the keys are tuples of two consecutive words in
        the file and the value for each key is a list of words that were found
        directly following the key.

        You should lowercase everything.
        Use strip and string.punctuation to strip the punctuation from the words.

        Words should be included in the list the number of times they appear.

        Suggestions on how to handle first words: create an entry in the dictionary
        with a first key (None, None), a second key (None, word1)

        Example:
        >>> with open('../data/alice.txt') as f:
        ...     d = trigrams(f)
        >>> d[('among', 'the')]
        ['people', 'party', 'trees', 'distant', 'leaves', 'trees', 'branches', 'bright']
        '''
        with open(self.file) as f:

            word_list = [word.strip(string.punctuation).lower() for line in f for word in line.split()]

            # tri_dict = defaultdict(list)
            tri_dict = {}
            for i, word in enumerate(word_list[:-1]):
                if (word, word_list[i+1]) not in tri_dict.keys():
                # if tri_dict[word, word_list[i+1]] == []:
                    # tri_dict[(word, word_list[i+1])].append(', '.join([w for j, w in enumerate(word_list[2:]) if word_list[j] == word and word_list[j+1] == word_list[i+1]]))
                    tri_dict[(word, word_list[i+1])] = [w for j, w in enumerate(word_list[2:]) if word_list[j] == word and word_list[j+1] == word_list[i+1]]

            # tri_dict.update({(None, None): []})
            # tri_dict.update({(None, word_list[0]) : [word_list[1]]})

            return tri_dict
