# Implement Trie (Prefix Tree)

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various 
# applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

#     -Trie() Initializes the trie object.
#     -void insert(String word) Inserts the string word into the trie.
#     -boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#     -boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True

 

# Constraints:

#     -1 <= word.length, prefix.length <= 2000
#     -word and prefix consist only of lowercase English letters.
#     -At most 3 * 104 calls in total will be made to insert, search, and startsWith.



class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        t = self.trie
		# The idea is to insert words in a linked fashion. For example "cars" will be inserted as
		# {'c':{'a':{'r':{'s':{}}}}
        for w in word:
          # If the starting letter is not in the trie
          if w not in t:
            t[w] = {} # Start with an empty object
          t = t[w]  #Then insert the word in the linked fashion
		# Another key named "end" will distinguish that the word  "cars" actually exists
		# Without the end key it simply means that the traversed part is just prefix
        t["end"] = True
        

    def search(self, word: str) -> bool:
        t = self.trie
		# Traverse through the word
        for w in word:
          if w in t:
            t = t[w]
          else:
            return False
		# As the end key denotes the existence of the word
        return "end" in t

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
		# Traverse through the word
        for w in prefix:
          if w in t:
            t = t[w]
          else:
            return False
		# Here it is okay to find whether we had traversed the entire prefix or not
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)