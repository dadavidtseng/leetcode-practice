class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        # Check if a palindrome can be formed
        odd = -1
        for i in range(26):
            if freq[i] % 2:
                if odd != -1:
                    return ""
                odd = i

        # Frequency for the left half
        half_freq = [x // 2 for x in freq]

        half = []
        for i in range(26):
            half.extend([chr(i + ord('a'))] * half_freq[i])

        half = "".join(half)
        target_half = target[:n // 2]

        # Build palindrome from left half
        def make_palindrome(left):
            middle = ""
            if odd != -1:
                middle = chr(odd + ord('a'))

            return left + middle + left[::-1]

        # Find smallest half >= target_half
        candidate_half = self.lex_ge_permutation(
            half,
            target_half
        )

        # Important: "" is a valid half when n <= 1,
        # so use None to represent "no solution".
        if candidate_half is None:
            return ""

        candidate = make_palindrome(candidate_half)

        # The half may equal target_half, but the full
        # palindrome can still be greater than target.
        if candidate > target:
            return candidate

        # Otherwise, we need the next half permutation.
        next_half = self.next_permutation(
            half,
            candidate_half
        )

        if next_half is None:
            return ""

        return make_palindrome(next_half)

    # --------------------------------------------------
    # Smallest permutation of s that is >= target
    # --------------------------------------------------
    def lex_ge_permutation(self, s: str, target: str):
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        result = []

        for i in range(len(target)):
            idx = ord(target[i]) - ord('a')

            # Match target[i]
            if freq[idx] > 0:
                result.append(target[i])
                freq[idx] -= 1
                continue

            # Try the smallest character > target[i]
            for c in range(idx + 1, 26):
                if freq[c] > 0:
                    result.append(chr(c + ord('a')))
                    freq[c] -= 1

                    for j in range(26):
                        result.append(
                            chr(j + ord('a')) * freq[j]
                        )

                    return "".join(result)

            # No larger character here.
            # Backtrack.
            for j in range(i - 1, -1, -1):
                prev = ord(target[j]) - ord('a')

                freq[prev] += 1
                result.pop()

                for c in range(prev + 1, 26):
                    if freq[c] > 0:
                        result.append(chr(c + ord('a')))
                        freq[c] -= 1

                        for k in range(26):
                            result.append(
                                chr(k + ord('a')) * freq[k]
                            )

                        return "".join(result)

            return None

        # target itself is a valid permutation
        return "".join(result)

    # --------------------------------------------------
    # Smallest permutation of s that is STRICTLY > target
    # --------------------------------------------------
    def next_permutation(self, s: str, target: str):
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        result = []

        for i in range(len(target)):
            idx = ord(target[i]) - ord('a')

            if freq[idx] > 0:
                result.append(target[i])
                freq[idx] -= 1
                continue

            # Try a larger character
            for c in range(idx + 1, 26):
                if freq[c] > 0:
                    result.append(chr(c + ord('a')))
                    freq[c] -= 1

                    for j in range(26):
                        result.append(
                            chr(j + ord('a')) * freq[j]
                        )

                    return "".join(result)

            # Backtrack
            for j in range(i - 1, -1, -1):
                prev = ord(target[j]) - ord('a')

                freq[prev] += 1
                result.pop()

                for c in range(prev + 1, 26):
                    if freq[c] > 0:
                        result.append(chr(c + ord('a')))
                        freq[c] -= 1

                        for k in range(26):
                            result.append(
                                chr(k + ord('a')) * freq[k]
                            )

                        return "".join(result)

            return None

        # target itself was matched.
        # Find the next strictly greater permutation.
        for j in range(len(target) - 1, -1, -1):
            prev = ord(target[j]) - ord('a')

            freq[prev] += 1
            result.pop()

            for c in range(prev + 1, 26):
                if freq[c] > 0:
                    result.append(chr(c + ord('a')))
                    freq[c] -= 1

                    for k in range(26):
                        result.append(
                            chr(k + ord('a')) * freq[k]
                        )

                    return "".join(result)

        return None