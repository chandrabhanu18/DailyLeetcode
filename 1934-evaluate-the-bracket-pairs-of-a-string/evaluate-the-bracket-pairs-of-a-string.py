class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        # Store final answer
        result = []

        i = 0

        while i < len(s):

            # Normal character
            if s[i] != '(':
                result.append(s[i])
                i += 1

            # Bracket starts
            else:
                j = i + 1

                # Find ')'
                while s[j] != ')':
                    j += 1

                # Get key inside brackets
                key = s[i + 1:j]

                # Replace key with value
                if key in mp:
                    result.append(mp[key])
                else:
                    result.append("?")

                # Move after ')'
                i = j + 1

        return "".join(result)