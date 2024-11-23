'''
Harry got a letter from Hogwarts School to join the wizardry. This letter consists of a magical key (6174) and a 4-digit number n with at least two distinct digits. Harry has to count in how many steps this number n can be converted to magical key invented by professor Dumbledore with this procedure as follows:

1.For number n, create two new numbers x and y consists of the digits in n in ascending and descending order respectively.
2.Subtract the smaller number from the larger number.
Help harry to count the steps to enter in the school.


'''

'''
example:

    N = 1234
    Step 1: x = 4321 y= 1234 => n = x-y => 3087
    Step 2: x = 8730 y= 0378 => n = x-y => 8352
    Step 3: x = 8532 y= 2358 => n = x-y => 6174
    you are done.
    Answer is 3

    Sample Input 0

1235

Sample Output 0

7



'''
steps = 0
n = int(input())
while n != 6174 and n != 0:
    if n < 1000:
        n = int(str(n) + '0')
    digits = sorted(str(n), reverse=True)
    x = int(''.join(digits))
    y = int(''.join(sorted(str(n))))
    if x == y:
        n = int(str(n) + '0')
        continue
    n = x - y
    steps += 1
print(steps)