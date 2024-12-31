class Solution:
    def similarPairs(self, words: List[str]) -> int:
        signature_count = {}
        
        # Create a signature for each word and count its occurrences
        for word in words:
            # Create a unique sorted signature for the word
            signature = ''.join(sorted(set(word)))
            if signature in signature_count:
                signature_count[signature] += 1
            else:
                signature_count[signature] = 1
        
        # Calculate the number of pairs using the combination formula
        result = 0
        for count in signature_count.values():
            if count > 1:
                result += (count * (count - 1)) // 2  # nC2 = n(n-1)/2
        
        return result