# Brute Force - Use a hashmap to store the counts of the input sentences coming in and use a heap(min heap) to maintain top 3 sugestions based on input string typed. 

# Min heap as we always use the opposite, min heap for max occurrences, here we maintain a size of 3 elements and anytime we exceed the size, we perform heapify and then poll the smallest freq element

# Shortcomings - Not a very optimized approach with hashmap as if we have a huge dataset to be stored, everytime to go over the hashmap and find what are all the words that start with the input given would be tedious, though lookup is O(1) that is for when you know what the word is, here we have to find what are all the words that 'startswith'

# Space - O(n * len(word)) where n is number of words
# Time - O(n * len(word))

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        
        self.hashmap = {}
        # string builder will store the current search input 
        self.input_string_builder = []
        
        # can iterate over either sentences or times array and build hashmap with all entries of words with freqs
        
        for i in range(len(sentences)):
            word = sentences[i]
            self.hashmap[word] = self.hashmap.get(word, 0) + times[i]
        

    def input(self, c: str) -> List[str]:
        
        if c == '#':
          # denotes end of search typed, so gather whatever is stored in string builder and make a string
            input_string = "".join(self.input_string_builder)
            
            # this denotes the user finished typing a particular input and we need to store the string typed up until '#' in the dict with freq 1
            
            self.hashmap[input_string] = self.hashmap.get(input_string, 0) + 1
            
            # once added to map, we initialize string builder back to empty and return [] for next inputs to be searched
            self.input_string_builder = []
            
            return
            
            
        # if c is not '#' keep adding to string builder
        self.input_string_builder.append(c)
        
        
        # now process heaps, go over all words that 'startswith' prefix typed / that is stored in string builder as inputs come... in map and add to heap 
        
        min_heap = []
        result = []
        
        for words in self.hashmap:
            if words.startswith(''.join(self.input_string_builder)):
                heappush(min_heap, comparator(self.hashmap[words], words)) # built in comparator to process any 2 entries
                
                if len(min_heap) > 3:
                    heappop(min_heap)
                    
                    
        # now heap only consists of the 3 top occurring words for input type prefix, from top to bottom are lowest frew to highest, so we add to result at zero index
        # so that evrytime next val is popped it pushes zero and goes to zero position
        # by the end result arr will have highest freq to lowest elements
        
        while min_heap:
            result.insert(0, heappop(min_heap).words)
            
        return result
    

# to process any 2 entries
# if 2 words have same freq, return one which is lex greater so that heap pops it with size limit
# if 2 words have different freq return which has smaller freq, so that it is maintained on top of heap and gets removed

# note simply- we want the heap to hold greater freq and smaller lex words, so return accordingly
class comparator:

    def __init__(self, freq, words):
        self.freq = freq
        self.words = words


    def __lt__(self, other):

        if self.freq != other.freq:
            return self.freq < other.freq

        else:
            return self.words > other.words             


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)



Optimized Solution

# In above we needed to maintain a hashmap with a whole lot of words and iterating over hashmap everytime to get the words starting with prefix is time consuming
# Instead of hashmap we can maintain a trie node with words inserted
  # along with trienode, at every node we will keep a hashmap to see what are all the words that start with current node letter  and maintain freq
  # this way, instead of going thorugh all the words in the hashmap and searching we iterate over a smaller hashmap size with words only relevant to prefix letter typed
  # example, if i typed in 'ia' in traditonal hashmap i would need to go through all n entries to see what words start with ia
  # in trie + hashmap taking adv of how tries are built at i, here by nature how design we built we have all possible words that only start with 'i'
  # Thus we save a lot of time by not going over unrelated word entries and with the map we have at each node, at 'i' now we have all words with prefix only i onwards so we need to search others which maybe i, j k etc
  # with freq counts we obtained we still use a heap and push words up till size k=3 and then remove words by comparator implemented





# Brute Force - Use a hashmap to store the counts of the input sentences coming in and use a heap(min heap) to maintain top 3 sugestions based on input string typed. 

# Min heap as we always use the opposite, min heap for max occurrences, here we maintain a size of 3 elements and anytime we exceed the size, we perform heapify and then poll the smallest freq element

# Shortcomings - Not a very optimized approach with hashmap as if we have a huge dataset to be stored, everytime to go over the hashmap and find what are all the words that start with the input given would be tedious, though lookup is O(1) that is for when you know what the word is, here we have to find what are all the words that 'startswith'

# Space - O(n * len(word)) where n is number of words
# Time - O(n * len(word))

class TrieNode: # in naive impl, we have isEnd and children, here have a map count which we maintain at every node
    
    def __init__(self):
        self.map_count = dict()
        self.children = [None] * 256 # size to account for lower, upper, special characs

        
class comparator:

    def __init__(self, word, freq):
        self.word = word
        self.freq = freq


    def __lt__(self, other):

        if self.freq != other.freq:
            return self.freq < other.freq

        else:
            return self.word > other.word


                    
class AutocompleteSystem:

    # initialize root node as Trie node and process words in sentences by inserting to trie
    def __init__(self, sentences: List[str], times: List[int]):
        
        self.root = TrieNode()
        
        self.input_string_builder = ""
        
        for i in range(len(sentences)):
            word = sentences[i]
            self.insert(word, times[i])
        
        
    # for each charac in word insert to trie and update current node's map with the count    
    def insert(self, word, count):
        current = self.root
        for i in range(len(word)):
            char = word[i]
            # we usually do ord(char) -'a' but since here input can be " " we check with this
            if current.children[ord(char) - ord(' ')] is None:
                current.children[ord(char) - ord(' ')] = TrieNode()
                
            current = current.children[ord(char) - ord(' ')]
            # for each charac node we will maintain the whole word in the hashmap
            # egs: love - at l , o, v, e we maintain hashmap with 
            current.map_count[word] = current.map_count.get(word, 0) + count
    
    
    # search for word and if it exists return the map, it will have all prefix words 
    # else return empty dict
    
    def search(self, sentence):
        
        current = self.root
        for i in range(len(sentence)):
            word = sentence[i]
            
            if current.children[ord(word) - ord(' ')] is None:
                return dict()
              
                # move pointer then return dict count
            current = current.children[ord(word) - ord(' ')]
            
        return current.map_count
    
    
    def input(self, c: str) -> List[str]:
        
        # this denotes the user finished typing a particular input and we need to store the strign typed up until '#' in the dict with freq 1
        
        if c == '#':
            self.insert(self.input_string_builder, 1)
            # in prev approach
            # self.hashmap[input_string] = self.hashmap.get(input_string, 0) + 1
            
            # once added to map, we initialize string builder back to empty and return []
            self.input_string_builder = ""
            return []
        
        self.input_string_builder += c # similar to prev where we add if char not hash
        
        # returns a dict of word, freq
        list_possible_words = self.search(self.input_string_builder)

        
        # now process heaps, go over all words that startswith prefix typed -- stored in string builder as inputs come in map and add to heap 
        
        min_heap = []
        result = []
        
        for word, freq in list_possible_words.items():
            # instead of going over hashmap go over what we retrieved from node specific map -- list_possible_words
        # for words in self.hashmap:
            if word.startswith(self.input_string_builder):
                # in prev approach we push word from hashmap that startwswith prefix and counts
                heapq.heappush(min_heap, comparator(word, freq))
                
                if len(min_heap) > 3:
                    heapq.heappop(min_heap)
                    
                    
        # now heap only consists of the 3 top occurring words for input type prefix, from top to bottom are lowest frew to highest, so we add to result at zero index
        # so that evrytime next val is popped it pushes zero and goes to zero position
        # by the end result arr will have highest freq to lowest elements
        
        while min_heap:
            result.insert(0, heapq.heappop(min_heap).word)
            
        return result
    
    


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)


Optimised Solution



class TrieNode: # in naive impl, we have isEnd and children, here have a map count which we maintain at every node
    
    def __init__(self):
        self.map_count = dict()
        self.children = [None] * 256 # size to account for lower, upper, special characs

        
class comparator:

    def __init__(self, word, freq):
        self.word = word
        self.freq = freq


    def __lt__(self, other):

        if self.freq != other.freq:
            return self.freq < other.freq

        else:
            return self.word > other.word


                    
class AutocompleteSystem:

    # initialize root node as Trie node and process words in sentences by inserting to trie
    def __init__(self, sentences: List[str], times: List[int]):
        
        self.root = TrieNode()
        
        self.input_string_builder = ""
        
        for i in range(len(sentences)):
            word = sentences[i]
            self.insert(word, times[i])
        
        
    # for each charac in word insert to trie and update current node's map with the count    
    def insert(self, word, count):
        current = self.root
        for i in range(len(word)):
            char = word[i]
            # we usually do ord(char) -'a' but since here input can be " " we check with this
            if current.children[ord(char) - ord(' ')] is None:
                current.children[ord(char) - ord(' ')] = TrieNode()
                
            current = current.children[ord(char) - ord(' ')]
            # for each charac node we will maintain the whole word in the hashmap
            # egs: love - at l , o, v, e we maintain hashmap with 
            current.map_count[word] = current.map_count.get(word, 0) + count
    
    
    # search for word and if it exists return the map, it will have all prefix words 
    # else return empty dict
    
    def search(self, sentence):
        
        current = self.root
        for i in range(len(sentence)):
            word = sentence[i]
            
            if current.children[ord(word) - ord(' ')] is None:
                return dict()
              
                # move pointer then return dict count
            current = current.children[ord(word) - ord(' ')]
            
        return current.map_count
    
    
    def input(self, c: str) -> List[str]:
        
        # this denotes the user finished typing a particular input and we need to store the strign typed up until '#' in the dict with freq 1
        
        if c == '#':
            self.insert(self.input_string_builder, 1)
            # in prev approach
            # self.hashmap[input_string] = self.hashmap.get(input_string, 0) + 1
            
            # once added to map, we initialize string builder back to empty and return []
            self.input_string_builder = ""
            return []
        
        self.input_string_builder += c # similar to prev where we add if char not hash
        
        # returns a dict of word, freq
        list_possible_words = self.search(self.input_string_builder)

        
        # now process heaps, go over all words that startswith prefix typed -- stored in string builder as inputs come in map and add to heap 
        
        min_heap = []
        result = []
        
        for word, freq in list_possible_words.items():
            # instead of going over hashmap go over what we retrieved from node specific map -- list_possible_words
        # for words in self.hashmap:
            if word.startswith(self.input_string_builder):
                # in prev approach we push word from hashmap that startwswith prefix and counts
                heapq.heappush(min_heap, comparator(word, freq))
                
                if len(min_heap) > 3:
                    heapq.heappop(min_heap)
                    
                    
        # now heap only consists of the 3 top occurring words for input type prefix, from top to bottom are lowest frew to highest, so we add to result at zero index
        # so that evrytime next val is popped it pushes zero and goes to zero position
        # by the end result arr will have highest freq to lowest elements
        
        while min_heap:
            result.insert(0, heapq.heappop(min_heap).word)
            
        return result
    
    


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
