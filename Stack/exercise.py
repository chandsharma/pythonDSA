from stack_deque import Stack

def reverse_string(s):
    stack = Stack()
    for l in s:
        stack.push(l)
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

def is_match(first,second):
    match = {'(':')',
             '[':']',
             '{':'}'}
    return match[second] == first

def is_balanced(s):
    stack = Stack()
    for l in s:
        if l in ['(','[','{']:
            stack.push(l)
        elif l in [')',"]",'}']:
            if stack.is_empty():
                return False
            if not is_match(l,stack.pop()):
                return False
    return stack.is_empty()

print(reverse_string("We will conquere COVID-19"))
print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))