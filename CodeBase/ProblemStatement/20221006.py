class Solution:
    def interpret(self, command: str) -> str:

        output = ''
        for i in range(len(command)):
            if command[i] == 'G':
                output += 'G'
            elif command[i] == '(':
                if command[i+1] == ')':
                    output += 'o'
                    i += 1
                else:
                    output += 'al'
                    i += 3

        return output


sol = Solution()
print(sol.interpret('(al)G(al)()()G'))