class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        # 2. Sort the hand first (O(N log N))
        hand.sort()
        
        # 3. Use a standard dict to track counts
        counts = {}
        for num in hand:
            counts[num] = counts.get(num, 0) + 1
            
        # 4. Iterate through the sorted hand
        for num in hand:
            # If this card has already been used in a group, skip it
            if counts[num] == 0:
                continue
            
            # Start a group of size groupSize
            for i in range(groupSize):
                current_card = num + i
                # If we need a card that doesn't exist or is used up
                if counts.get(current_card, 0) == 0:
                    return False
                
                # Consume the card
                counts[current_card] -= 1
                
        return True