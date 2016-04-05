"""
    Trie Implementations with arrays
    Only implements add and search currently
    This Trie is intended for english words, case insensitive.
    Hector Ramos
    4/04/2016
"""

# Trie assumes it'll be handling only the 26 letters of the english alphabet
class Trie(object):
    def __init__(self):
        self.root = Trie.TrieNode()

    # Adds string to the trie, creating nodes along the way if necessary.
    def add(self, string):
        if not string:
            print "Empty string entered!"
            return

        current_string = string
        current_node = self.root

        # Traverse through trie for each character in the string
        while current_string:
            # Find the character index for the current first character in string
            index = get_character_index(current_string[0])

            # If there isn't a node at this index yet, make one
            if not current_node.character_array[index]:
                current_node.character_array[index] = Trie.TrieNode()
            
            # Move down trie
            current_node = current_node.character_array[index]

            # "Pops" the first character from current string
            current_string = current_string[1:]

        # Current node's path is now a valid word
        current_node.is_word = True

    # Searches if string is in the trie currently, returns bool
    def search(self, string):
        current_string = string
        current_node = self.root

        # Traverse through trie for each character in the string
        while current_string:
            # Find the character index for the current first character in string
            index = get_character_index(current_string[0])

            # If there's no path to the word, this word doesn't exist in trie
            if not current_node.character_array[index]:
                return False

            # Move down trie
            current_node = current_node.character_array[index]

            # "Pops" first character from the current string
            current_string = current_string[1:]

        # Return true only if last node for string is a word in the trie
        if current_node.is_word:
            return True
        else:
            return False

    # Given its own function for readability. Assumes character is an english
    # alphabet character, and returns its given index in the array of pointers
    def get_character_index(self, c):
        # Ord returns an integer representation for a ASCII string
        # lower converts the character to lowercase if it's in uppercase
        index = ord(character.lower())
        # Lower case english characters start from integer 97
        # Subtract that, then take the mod it by 26(# of chars) to get the index
        index = (index - 97) % 26

        return  index = (ord(character.lower()) - 97) % 26
         
    @staticmethod
    class TrieNode(object):
        def __init__(self, is_word=False):
            self.is_word = is_word
            self.character_array = [None for x in xrange(26)]


if __name__ == "__main__":
    trie = Trie()

    trie.add("Bat")
    trie.add("Bath")
    trie.add("Test")
    trie.add("Zebra")
    trie.add("Zebras")

    print "Should all be true (Case insensitive)"
    print trie.search("Bat")
    print trie.search("Bath")
    print trie.search("Test")
    print trie.search("test")
    print trie.search("zebra")
    print trie.search("zebras")

    print "Should all be false"
    print trie.search("Baths")
    print trie.search("tests")
    print trie.search("Bats")
    print trie.search("tests")