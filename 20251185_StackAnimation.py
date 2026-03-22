import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. CSV 데이터 로드 (과제 조건 b, c 반영)
try:
    df = pd.read_csv("team_data.csv")
    all_words = []
    # 모든 팀원의 단어를 리스트 하나로 결합 (과제 조건 d-1 충족)
    for i in range(1, 4):
        all_words.extend(df[f'단어{i}'].tolist())
except FileNotFoundError:
    print("Error: 'team_data.csv' 파일을 찾을 수 없습니다. 파일 위치를 확인해주세요.")
    exit()

# 2. 애니메이션 시나리오 구성 (과제 조건 d 반영)
# d-3: stack 선언([]) 단계부터 기록 시작
actions = [("init", "stack = []", [])]
current_stack = []

# d-1: 모든 단어 순차 처리 / d-2: push, pop, top 연산 활용
for word in all_words:
    # Push 연산: 단어를 스택에 추가
    current_stack.append(word)
    actions.append(("push", f"stack.push(\"{word}\")", list(current_stack)))
    
    # d-4: 스택 크기를 10 이하로 유지하기 위한 로직
    if len(current_stack) >= 5:
        # Top 연산: 최상단 데이터 확인
        actions.append(("top", f"stack.top() -> \"{current_stack[-1]}\"", list(current_stack)))
        # Pop 연산: 최상단 데이터 제거
        popped = current_stack.pop()
        actions.append(("pop", f"stack.pop() -> \"{popped}\"", list(current_stack)))

# 3. 시각화 및 애니메이션 설정 (d-5 반영)
plt.rcParams['font.family'] = 'Malgun Gothic' # 한글 폰트 설정
plt.rcParams['axes.unicode_minus'] = False     # 마이너스 기호 깨짐 방지

fig, ax = plt.subplots(figsize=(10, 7))

def update(frame):
    """프레임마다 스택의 상태를 화면에 그리는 함수"""
    ax.clear()
    action_type, command, stack_state = actions[frame]
    
    # 왼쪽: 현재 실행 중인 Python 스택 코드 표시
    ax.text(0.05, 0.9, "Current Operation:", fontsize=14, color='gray')
    ax.text(0.05, 0.8, command, fontsize=22, color='royalblue', weight='bold')
    
    # 오른쪽: 스택 데이터 구조 시각화
    ax.text(0.7, 0.9, "[ Stack Data Structure ]", fontsize=16, ha='center', weight='bold')
    
    # 리스트의 데이터를 아래에서부터 박스 형태로 쌓아 올림
    for i, item in enumerate(stack_state):
        rect = plt.Rectangle((0.55, 0.1 + i*0.07), 0.3, 0.06, 
                             fill=True, facecolor='lavender', edgecolor='midnightblue', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(0.7, 0.12 + i*0.07, item, ha='center', fontsize=12, weight='semibold')
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off') # 제목과 축을 모두 제거하여 화면을 깔끔하게 유지

# 애니메이션 객체 생성 (interval=800ms)
ani = FuncAnimation(fig, update, frames=len(actions), interval=800, repeat=False)

print("시뮬레이션을 시작합니다.")
plt.show()
