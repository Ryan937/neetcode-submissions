class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dupes = [0] * 26
        
        for c in words[0]:
            dupes[ord(c) - ord('a')] += 1

        for word in words[1:]:
            current_freq = [0] * 26

            for c in word:
                current_freq[ord(c) - ord('a')] += 1
            
            for i in range(26):
                dupes[i] = min(dupes[i], current_freq[i])

        result = []

        for i in range(26):
            if dupes[i] > 0:
                c = chr(i + ord('a'))
                result.extend([c] * dupes[i])

        return result