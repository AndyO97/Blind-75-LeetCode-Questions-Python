# Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Idea: 
# Anagrams are strings which have identical counts of characters. Therefore, sorted anagrams, result in the same string. We can take advantage of this last property.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            # We create a dictionary and for each word in the input array, we add a key to the dictionary if the sorted version of the word doesn't already exist in the list of keys.
            # The key then becomes the sorted version of the word, and the value for the key is an array that stores each anagram of the key. 
            if sortedWord not in h:
                h[sortedWord] = [word]
            # For every next word that is an anagram, sort the word, find the key that is equal to the sorted form, and add the original word to the list of values for the key.
            else:
                h[sortedWord].append(word)

        # At the end, we add every value in the dictionary to the final array.
        final = []
        for value in h.values():
            final.append(value)
        return final