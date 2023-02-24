import os
import asyncio
import math

def solve_question(words):
    if "prime?" in words: return answer_is_prime(words)
    elif "square?" in words: return answer_is_square(words)
    elif "divisible" in words: return answer_is_divisible(words)
    else: pass
#IS PRIME
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def answer_is_prime(words):
    nums = [word for word in words if word.isnumeric()]
    if isprime(int(nums[-1])): return "Y"
    return "N"

#IS SQUARE
def issquare(num):
    root = math.sqrt(num)
    if int(root + 0.5) ** 2 == num:
        return True
    else:
        return False

def answer_is_square(words):
    nums = [word for word in words if word.isnumeric()]
    if issquare(int(nums[-1])): return "Y"
    return "N"

#IS DIVISIBLE
def isdivisible(num, divisor):
    if num % divisor == 0:
        return True
    return False

def answer_is_divisible(words):
    divisor = words[-2][:-1]
    print(words, divisor)
    nums = [word for word in words if word.isnumeric()]
    if isdivisible(int(nums[-1]), int(divisor)): return "Y"
    return "N"

#async def connect():
#    reader, writer = await asyncio.open_connection("192.46.238.159", 1337)
#    for i in range(50):
#        data = await reader.read(10000)
#        words = data.decode().split()
#        print(words)
#        answer = solve_question(words)
#        print(f'Send: {answer!r}')
#        writer.write(answer.encode())
#        print("Done, first loop")
#    await writer.drain()


async def handler(reader, writer):
    def send(msg):
        print("send to device: {}".format(msg))
        writer.write((msg + '\n').encode())

    print("device connected")
    while True:
        msg = await reader.readline()
        if not msg:
            print("device disconnected")
            break
        msg = msg.decode().strip()
        print("got from device: {}".format(msg))

        words = msg.split(" ")
        result = solve_question(words)
        if result: send(solve_question(words))

async def start_server():
    reader, writer = await asyncio.open_connection('192.46.238.159', 1337)
    try:
        asyncio.run(await handler(reader, writer))
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server())

#is_prime()
#is_perfect_square()
#is_divisible?()%
