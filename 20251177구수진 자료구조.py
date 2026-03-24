import os
import time

def draw(stack, text):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n {text:<25} +------------+")
    for i in range(9, -1, -1):
        if i < len(stack):
            print(f"{' ':27} | {stack[i]:^10} |")
        else:
            print(f"{' ':27} | {' ':^10} |")
        print(f"{' ':27} +------------+")
    time.sleep(1.2)

s = []

s.append("개나리")
draw(s, 'stack.push("개나리")')

s.append("나비")
draw(s, 'stack.push("나비")')

s.append("케이크")
draw(s, 'stack.push("케이크")')

s.append("아메리카노")
draw(s, 'stack.push("아메리카노")')

s.append("벚꽃")
draw(s, 'stack.push("벚꽃")')

s.append("중간고사")
draw(s, 'stack.push("중간고사")')

# top 연산 결과 표시
draw(s, f'stack.top() -> {s[-1]}')

s.pop()
draw(s, 'stack.pop()')

s.append("봄동")
draw(s, 'stack.push("봄동")')

s.append("디저트")
draw(s, 'stack.push("디저트")')

s.append("연인")
draw(s, 'stack.push("연인")')

s.append("생일")
draw(s, 'stack.push("생일")')

s.append("우유")
draw(s, 'stack.push("우유")')

draw(s, f'stack.top() -> {s[-1]}')

s.pop()
draw(s, 'stack.pop()')

s.append("라떼")
draw(s, 'stack.push("라떼")')