class Solution:
    def getLucky(self, s: str, k: int) -> int:
        store = []

        for c in s:
            value = ord(c) - ord('a') + 1
            store.append(str(value))
        
        new_store = "".join(store)
        result = 0

        while k!=0:
            total = 0
            for c in new_store:
                total += int(c)
            new_store = str(total)
            k -= 1    

            if k == 0:
                result = total
        return result
        