def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def pow(num, p):
    if p == 1:
        return num
    else:
        return num * pow(num, p-1)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def reverse(q):
    if q.size() == 0:
        return None
    if q.size() == 1:
        return q
    else:
        value = q.dequeue()
        q = reverse(q)
        q.enqueue(value)
        return q

def hanoiTowers(discNum, fromPole, withPole, toPole):
	if discNum >= 1:
		hanoiTowers(discNum-1, fromPole, toPole, withPole)
		print("move from " + fromPole + " to " + toPole)
		hanoiTowers(discNum-1, withPole, fromPole, toPole)

def palindrome(st):
    st = ''.join(st.split())
    if st == "":
        return True
    elif st[0] != st[-1]:
        return False
    else:
        return palindrome(st[1:-1])