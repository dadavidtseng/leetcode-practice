"""
Understand:
k[encoded_string] means that encoded_string is being repeated k times
Return the decoded string

Ex1: 2[a3[b]]c -> 2[abbb]c -> abbbabbbc
Ex2: axb3[z]4[c] -> axbzzzcccc
Ex3: ab2[c]3[d]1[x] -> abccdddx

Note that we have to decode the string from the deepest layer outwards

Match:
Stack, String, Recursion

Plan:
The k before [ and encoded_string after [
Whenever we meet ], that means we have to do the decode, so this might be the base case
of recursive call.

Use a stack to store characters, when there's not a k, we must be reading a string.
When there's a k, we remember it and continue reading the encoded_string until we meet 
the right bracket. Once we read the right bracket, we start popping from the stack and do
the decode

#1  s=2
#2  s=2[
#3  s=2[a
#4  s=2[a3
#5  s=2[a3[
#6  s=2[a3[b
#7  s=2[a3[b], we have to decode now
#8  string_to_decode=b, k=3, decoded_string=bbb
#9  s=2[abbb], we have to decode now
#10 string_to_decode=abbb, k=2, decoded_string=abbbabbb
#11 s=abbbabbbc, return
"""

class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        stack = []  # 1 <= s.length <= 30
        i=0

        # If s[i] is in a-z

        while i<len(s):
            start=i
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    i+=1
                stack.append(s[start:i])
            
            elif s[i].isalpha():
                while i < len(s) and s[i].isalpha():
                    i+=1
                stack.append(s[start:i])            

            elif i < len(s) and s[i]=='[':
                stack.append(s[i])
                i+=1
            
            elif i < len(s) and  s[i]==']':
                token = []
                while stack[-1] != '[':
                    token.append(stack.pop())
                stack.pop()
                k = stack.pop()
                decoded_token = "".join(reversed(token)) * int(k)
                if stack and stack[-1]!='[':
                    stack.append(stack.pop() +decoded_token)
                else:
                    stack.append(decoded_token)
                i+=1
        return "".join(stack)

"""
Review:
Comparing my solution with official one stack solution, my idea about merging tokens
is slightly more efficient because of the operations it'll go through while the code logic
without merging tokens is more clean and understandable.

Evaluate:
I should've thought about or been more familiar with while loop and stack.
When trying to decode, I tried to merge all tokens, but I missed the tokens after it.
For example, 2[a3[b]c], wehre there's a letter after decoded token but before right bracket.
Maybe I should be more comfortable with while loop and stack since other questions also use them frequently.
"""
        

        




        