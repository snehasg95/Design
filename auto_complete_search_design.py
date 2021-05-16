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
