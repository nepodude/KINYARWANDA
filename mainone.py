import re
import os
import sys

def split_word(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'â', 'à', 'é', 'è', 'ê', 'î', 'ô', 'û', 'ù', 'ä', 'ö', 'ü',
              'A', 'E', 'I', 'O', 'U', 'Â', 'À', 'É', 'È', 'Ê', 'Î', 'Ô', 'Û', 'Ù', 'Ä', 'Ö', 'Ü'}
    groups = []
    i = 0
    n = len(word)
    
    # Check for leading vowels
    if n == 0:
        return groups
    if word[0] in vowels:
        j = 0
        while j < n and word[j] in vowels:
            j += 1
        groups.append(word[0:j])
        i = j
    
    # Process remaining parts as consonant-vowel pairs
    while i < n:
        # Consonant part
        consonant_start = i
        while i < n and word[i] not in vowels:
            i += 1
        consonant = word[consonant_start:i]
        
        # Vowel part
        vowel_start = i
        while i < n and word[i] in vowels:
            i += 1
        vowel = word[vowel_start:i]
        
        if consonant or vowel:
            groups.append(consonant + vowel)
    
    return groups

def main():
    input_str = input("Enter the string: ").strip()
    tokens = re.findall(r'\S+|\s+', input_str)
    array = []
    
    for token in tokens:
        if token.strip() == '':  # Space token
            array.append('x')
        else:
            substrings = split_word(token)
            array.extend(substrings)
    
    print("Generated array:", array)
    
    sound_dir = os.path.join(os.getcwd(), 'sound')
    if not os.path.exists(sound_dir):
        print(f"Directory '{sound_dir}' not found.")
        return
    
    for item in array:
        sound_file = os.path.join(sound_dir, f"{item}.wav")
        if os.path.isfile(sound_file):
            if sys.platform == 'win32':
                import winsound
                winsound.PlaySound(sound_file, winsound.SND_FILENAME)
            else:
                if sys.platform == 'darwin':
                    os.system(f'afplay "{sound_file}" 2> /dev/null')
                else:
                    os.system(f'aplay "{sound_file}" 2> /dev/null')
        else:
            print(f"Sound file '{sound_file}' not found.")

if __name__ == "__main__":
    main()