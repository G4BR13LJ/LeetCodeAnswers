
def calPoints(operations):
        # Input: ops = ["5","2","C","D","+"]
        # 'int x' : add integer x to score
        # 'c' is a pop command
        # 'D' checks if anything on stack, if there is, check the final value and mult it by 2, add val to stack
        # '+' checks if there are there are at least two items on stack, if yes then adds their su, as new item
        stack =[]
        for command in operations:
                print(stack)
                command=command.lower()
                try:
                    # its a number, append
                    command = int(command)
                    stack.append(command)
                except:                   
                    if command != "+":
                        print(command)
                        if command == "c":
                            stack.pop()
                            # print(f"(on c command: {stack}")
                        if command == "d":
                            #1 item on stack? - > double it and add that
                            # print(f"(on d command: {stack}")
                            val = stack[-1] + stack[-1]
                            stack.append(val)                              
                    else:
                        # 2 items on stack? - > add them and add their sum to le stack
                        val = stack[-1] + stack[-2]
                        stack.append(val)
                        # print(f"\n{stack}\n")
        i = 0
        rtrn = 0
        for val in stack:
             rtrn += stack[i]
             i+=1
        return rtrn

# print(calPoints(["5","2","C","D","+"]))