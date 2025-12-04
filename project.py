# This is a project for Data Structures and Algorithm

def has_vowel(word):
      """
      Checks if a given word contains any vowels (case-insensitive).
    
      Args:
        word: The string to check.
    
      True will be returned if the word contains a vowel, False otherwise.
      """
      vowels = "aeiou" or "AEIOU"
      for char in word.lower():
          if char in vowels:
              return True
      return False

def binary_search_and_check_vowel(sorted_word_list, target_word):
  """
  Here, we are performing a binary search on a sorted list of words to find a wanted word
  then check if it has a vowel.

  Args:
    sorted_word_list: A list of words sorted in alphabetical order.
    target_word: The word to search for.
  """

  low = 0
  high = len(sorted_word_list) - 1

  while low <= high:
    mid = (low + high) // 2
    stranger = sorted_word_list[mid]

    if stranger == target_word:
      # Word is found, now check for a vowel
      return (True, has_vowel(stranger))
    
    if stranger < target_word:
      # The word is in the right half
      low = mid + 1
    else:
      # The word is in the left half
      high = mid - 1

  # The word was not found in the list
  return (False, None)

# --- Illustration handling ---

# A sorted or ordered list of words
word_in_list = ["apple", "banana", "crypt", "dry", "fly", "grape", "myth", "python", "rhythm", "sky"]

# --- Testing Cases ---

# 1. In this case, we are searching for a word that exists and has a vowel
print()
word_to_get1 = "python"
get1, contains_vowel1 = binary_search_and_check_vowel(word_in_list, word_to_get1)

if get1:
  print(f"{word_to_get1} was found in the list.") # F-string applied
  if contains_vowel1:
    print(f"Yes, it has a vowel.\n") # An improvement would be, identifying how many vowels are there.
  else:
    print(f"But, it does not have a vowel.\n") # This will be get2 if word_to_get1 does not have a vowel

# 2. In this case, we are searching for a word that exists and has no vowels
word_to_get2 = "dry"
get2, contains_vowel2 = binary_search_and_check_vowel(word_in_list, word_to_get2)

if get2:
  print(f"{word_to_get2} was found in the list.") # F-string applied
  if contains_vowel2:
    print(f"Yes, this word has a vowel.\n")
  else:
    print(f"But, it does not have a vowel.\n")


# 3. In this case, we are searching for a word that does not exist in the list
word_to_get3 = "zeste"
get3, _ = binary_search_and_check_vowel(word_in_list, word_to_get3)

if not get3:
  print(f"{word_to_get3} does not exist in the list.") # F-string applied
  print()