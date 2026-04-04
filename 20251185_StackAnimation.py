import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. CSV 데이터 로드 (과제 조건 b 반영)
try:
    # 실제 파일 경로에서 로드
    df = pd.read_csv("team_data.csv")
    all_words = []
    # 모든 팀원의 단어를 리스트 하나로 결합 (과제 조건 d-1)
    for i in range(1, 4):
        all_words.extend(df[f'단어{i}'].tolist())
except FileNotFoundError:
    print("Error: 'team_data.csv' 파일이 없습니다. 파일명을 확인해주세요!")
    exit()

# 2. 애니메이션 시나리오 구성 (d-3: 선언 단계 강조)
# "스택 선언" 문구 추가
actions = [("init", "stack = []  # 스택 선언", [])]
current_stack = []

for word in all_words:
    # Push 연산
    current_stack.append(word)
    actions.append(("push", f'stack.push("{word}")', list(current_stack)))
    
    # d-4: 스택 크기 조절 (5개 이상이면 Top 확인 후 Pop)
    if len(current_stack) >= 5:
        actions.append(("top", f'stack.top() -> "{current_stack[-1]}"', list(current_stack)))
        popped = current_stack.pop()
        actions.append(("pop", f'stack.pop() -> "{popped}"', list(current_stack)))

# 3. 시각화 및 애니메이션 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 7))

def update(frame):
    ax.clear()
    action_type, command, stack_state = actions[frame]
    
    # 이미지 예시와 유사한 전체 외곽 테두리 (파란색)
    rect_outline = plt.Rectangle((0.02, 0.02), 0.96, 0.96, fill=False, 
                                 edgecolor='#3498db', lw=3, transform=ax.transAxes)
    ax.add_patch(rect_outline)

    # --- 왼쪽 영역: 코드 및 상태 메시지 ---
    if action_type == "init":
        # 스택 선언을 아주 명확하게 표시 (fontsize=... 등호 사용)
        ax.text(0.1, 0.6, "★ SYSTEM CHECK ★", fontsize=16, color='red', weight='bold')
        ax.text(0.1, 0.5, command, fontsize=32, color='darkblue', weight='bold', va='center')
        ax.text(0.1, 0.4, "비어있는 스택이 성공적으로 생성되었습니다.", fontsize=14, color='gray')
    else:
        # 일반 연산 (Push, Pop, Top)
        ax.text(0.05, 0.85, "Current Operation:", fontsize=14, color='gray')
        ax.text(0.08, 0.5, command, fontsize=26, weight='bold', va='center', color='black')

    # --- 오른쪽 영역: 스택 데이터 구조 (표 형태) ---
    box_x, box_width, cell_h = 0.6, 0.3, 0.07
    # 스택 바닥선
    ax.plot([box_x, box_x + box_width], [0.1, 0.1], color='black', lw=3)
    
    # 데이터 셀 그리기
    for i, item in enumerate(stack_state):
        y_pos = 0.1 + (i * cell_h)
        # 사각형 격자 (표 형태)
        rect = plt.Rectangle((box_x, y_pos), box_width, cell_h, fill=False, edgecolor='black', lw=1.5)
        ax.add_patch(rect)
        # 데이터 텍스트 표시
        ax.text(box_x + (box_width/2), y_pos + cell_h/2, item, 
                ha='center', va='center', fontsize=13, weight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

# 애니메이션 실행 (1초 간격)
ani = FuncAnimation(fig, update, frames=len(actions), interval=1000, repeat=False)

print("시뮬레이션을 시작합니다. 첫 화면의 스택 선언을 확인하세요!")
plt.show()
