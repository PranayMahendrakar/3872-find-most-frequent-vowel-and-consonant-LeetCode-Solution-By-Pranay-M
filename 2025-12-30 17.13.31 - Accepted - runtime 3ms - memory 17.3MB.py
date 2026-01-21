class Solution:
    def maxFreqSum(self, s: str) -> int:
        from collections import Counter
        vowels = set('aeiou')
        cnt = Counter(s)
        max_vowel = max((cnt[c] for c in cnt if c in vowels), default=0)
        max_consonant = max((cnt[c] for c in cnt if c not in vowels), default=0)
        return max_vowel + max_consonant