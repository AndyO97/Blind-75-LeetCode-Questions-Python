# Add and Search Words Data Structure

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

#     -WordDictionary() Initializes the object.
#     -void addWord(word) Adds word to the data structure, it can be matched later.
#     -bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True


# TrieNode class to be used for the root of the WordDicitionary Class
class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary for storing the characters of the Word (one per level of TrieNode)
        self.is_word = False # Flag for setting the end of the word
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode() # Initialize the root as a TrieNode 

    def addWord(self, word):
        current_node = self.root
        # The setdefault() method returns the value of the item with the specified key.
        # If the key does not exist, insert the key, with the specified value
        # dictionary.setdefault(keyname, value)
        for character in word:
            current_node = current_node.children.setdefault(character, TrieNode()) # returns value of the character if it is in the dictionary or the trieNode if key the is not in the dictionary
        current_node.is_word = True # Set the flag that the last TrieNode is a word
        
    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.is_word
               
            if word[index] == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
                    
            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            
            return False
    
        return dfs(self.root, 0)