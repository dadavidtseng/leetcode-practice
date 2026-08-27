class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26
        result = []

        for c in s:
            freq[ord(c) - ord("a")] += 1

        for i in range(len(target)):
            idx = ord(target[i]) - ord("a")

            if freq[idx] > 0:
                result.append(target[i])
                freq[idx] -= 1
            else:
                while idx < 25 and freq[idx + 1] <= 0:
                    idx += 1

                if idx < 25 and freq[idx + 1] > 0:
                    result.append(chr(idx + 1 + ord("a")))
                    freq[idx + 1] -= 1

                    for j in range(26):
                        result.append(chr(j + ord("a")) * freq[j])

                    return "".join(result)

                # Backtrack
                for j in range(i - 1, -1, -1):
                    prev_idx = ord(target[j]) - ord("a")
                    freq[prev_idx] += 1
                    result.pop()

                    for k in range(prev_idx + 1, 26):
                        if freq[k] > 0:
                            result.append(chr(k + ord("a")))
                            freq[k] -= 1

                            for m in range(26):
                                result.append(chr(m + ord("a")) * freq[m])

                            return "".join(result)

                return ""

        # Backtrack if the entire target was matched
        for j in range(len(target) - 1, -1, -1):
            prev_idx = ord(target[j]) - ord("a")
            freq[prev_idx] += 1
            result.pop()

            for k in range(prev_idx + 1, 26):
                if freq[k] > 0:
                    result.append(chr(k + ord("a")))
                    freq[k] -= 1

                    for m in range(26):
                        result.append(chr(m + ord("a")) * freq[m])

                    return "".join(result)

        return ""
