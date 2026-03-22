import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# 1. CSV 데이터 읽기 (과제 조건 b, c 반영)
# 반드시 같은 폴더에 'team_data.csv'가 있어야 합니다.
try:
    df = pd.read_csv("team_data.csv")
    # 모든 단어를 하나의 리스트로 합치기 (d-1: 모든 단어 사용 조건 충족을 위해)
    all_words = []
    for i in range(1, 4):
        all_words.extend(df[f'단어{i}'].tolist())
except FileNotFoundError:
    print("Error: team_data.csv 파일을 찾을 수 없습니다. 같은 폴더에 있는지 확인하세요.")
    exit()

# 2. 애니메이션 시나리오 구성 (과제 조건 d 반영)
# d-3: stack 선언부터 시작
actions = [("init", "stack = []", [])]
current_stack = []

# d-1: 모든 단어 사용 / d-2: push, pop, top 연산 모두 사용
for word in all_words:
    # Push 연산 수행
    current_stack.append(word)
    actions.append(("push", f"stack.push(\"{word}\")", list(current_stack)))
    
    # d-4: stack의 크기를 10 이하로 유지 (5개 쌓일 때마다 관리)
    if len(current_stack) >= 5:
        # Top 연산 (현재 가장 위 데이터 확인)
        actions.append(("top", f"stack.top() -> \"{current_stack[-1]}\"", list(current_stack)))
        # Pop 연산 (데이터 제거)
        popped = current_stack.pop()
        actions.append(("pop", f"stack.pop() -> \"{popped}\"", list(current_stack)))

# 3. 시각화 설정 (d-5: 스택 변화 확인 가능하도록 제작)
plt.rcParams['font.family'] = 'Malgun Gothic' # 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 7))

def update(frame):
    ax.clear()
    action_type, command, stack_state = actions[frame]
    
    # 왼쪽 영역: 현재 실행 중인 스택 명령어 표시
    ax.text(0.05, 0.9, "Python Stack Operations:", fontsize=13, color='gray')
    ax.text(0.05, 0.8, command, fontsize=20, color='blue', weight='bold')
    
    # 오른쪽 영역: 스택 구조 시각화 (이미지 예시와 유사한 형태)
    ax.text(0.65, 0.9, "[ Stack Structure ]", fontsize=15, ha='center', weight='bold')
    
    # 바닥(index 0)부터 차곡차곡 쌓아 올리기
    for i, item in enumerate(stack_state):
        # 박스 그리기
        rect = plt.Rectangle((0.5, 0.1 + i*0.07), 0.3, 0.06, fill=True, color='lavender', edgecolor='black')
        ax.add_patch(rect)
        # 박스 안에 단어 표시
        ax.text(0.65, 0.12 + i*0.07, item, ha='center', fontsize=12)
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

# 4. 애니메이션 생성 및 저장 설정
# interval=800ms로 설정하여 변화를 충분히 인지할 수 있게 함 (d-5)
ani = FuncAnimation(fig, update, frames=len(actions), interval=800, repeat=False)

# [중요] mp4 파일로 저장하기
# FFmpeg가 설치되어 있지 않으면 오류가 날 수 있습니다. 
# 그럴 경우 '화면 녹화' 방식을 사용하세요!
try:
    print("애니메이션을 mp4 파일로 생성 중입니다...")
    writer = animation.FFMpegWriter(fps=1.25, metadata=dict(artist='KimSumin'), bitrate=1800)
    ani.save('20251185_StackAnimation.mp4', writer=writer)
    print("성공: '20251185_StackAnimation.mp4' 파일이 생성되었습니다.")
except Exception as e:
    print("\n[알림] mp4 자동 저장에 실패했습니다.")
    print("원인:", e)
    print("해결책: 아래 plt.show()로 뜨는 창을 직접 녹화하여 mp4를 만드세요!")

plt.show()
