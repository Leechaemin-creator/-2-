import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. CSV 데이터 읽기 (과제 조건 b, c 반영)
try:
    df = pd.read_csv("team_data.csv")
    # 모든 단어를 하나의 리스트로 합치기
    all_words = []
    for i in range(1, 4):
        all_words.extend(df[f'단어{i}'].tolist())
except FileNotFoundError:
    print("Error: team_data.csv 파일을 찾을 수 없습니다. 같은 폴더에 있는지 확인하세요.")
    exit()

# 2. 애니메이션 시나리오 구성 (과제 조건 d 반영)
# stack 선언부터 시작 (d-3)
actions = [("init", "stack = []", [])]
current_stack = []

# 모든 단어를 한 번 이상 사용 (d-1)
# push, pop, top 연산을 모두 한 번 이상 사용 (d-2)
for word in all_words:
    # Push 연산
    current_stack.append(word)
    actions.append(("push", f"stack.push(\"{word}\")", list(current_stack)))
    
    # 스택 크기 10 이하 유지 (d-4)를 위해 5개가 쌓이면 pop/top 수행
    if len(current_stack) >= 5:
        # Top 확인
        actions.append(("top", f"stack.top() -> \"{current_stack[-1]}\"", list(current_stack)))
        # Pop 수행
        popped = current_stack.pop()
        actions.append(("pop", f"stack.pop() -> \"{popped}\"", list(current_stack)))

# 3. 시각화 설정 (과제 조건 d-5 반영)
plt.rcParams['font.family'] = 'Malgun Gothic' # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 7))

def update(frame):
    ax.clear()
    action_type, command, stack_state = actions[frame]
    
    # 왼쪽: 스택 명령어 표시
    ax.text(0.05, 0.9, "Python Stack Operations:", fontsize=15, color='gray')
    ax.text(0.05, 0.8, command, fontsize=22, color='blue', weight='bold')
    
    # 오른쪽: 스택 구조 시각화 (테이블 형태)
    ax.text(0.65, 0.9, "[ Stack Structure ]", fontsize=15, ha='center')
    
    # 바닥부터 쌓아 올리기
    for i, item in enumerate(stack_state):
        # 사각형 그리기
        rect = plt.Rectangle((0.5, 0.1 + i*0.07), 0.3, 0.06, fill=True, color='lavender', edgecolor='black')
        ax.add_patch(rect)
        # 단어 쓰기
        ax.text(0.65, 0.12 + i*0.07, item, ha='center', fontsize=12)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

# 애니메이션 실행 (interval 800ms)
ani = FuncAnimation(fig, update, frames=len(actions), interval=800, repeat=False)
plt.show()