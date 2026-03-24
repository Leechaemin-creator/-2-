import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
from matplotlib.animation import FuncAnimation


def set_korean_font():
    candidates = ['Malgun Gothic', 'AppleGothic', 'NanumGothic', 'NanumBarunGothic']
    available = {f.name for f in fm.fontManager.ttflist}
    for font in candidates:
        if font in available:
            plt.rcParams['font.family'] = font
            plt.rcParams['axes.unicode_minus'] = False
            return
    
    for f in fm.fontManager.ttflist:
        if any(k in f.name for k in ['Gothic', 'Gothic', 'Nanum', 'Malgun']):
            plt.rcParams['font.family'] = f.name
            plt.rcParams['axes.unicode_minus'] = False
            return

set_korean_font()


team_data = [
    {'학번': '20241233', '이름': '원솔은',  '단어': ['꽃잎','정원','목련','소음','파우더','우유']},
    {'학번': '20241261', '이름': '이채민',  '단어': ['소풍','벚꽃','개강','커피','알바','디저트']},
    {'학번': '20241263', '이름': '이채윤',  '단어': ['연인','벚꽃','석촌호수','커피','바리스타','원두']},
    {'학번': '20251177', '이름': '구수진',  '단어': ['벚꽃','잔디','생일','아메리카노','원두','갈색']},
    {'학번': '20251179', '이름': '권지영',  '단어': ['벚꽃','중간고사','봄동','카페라떼','디저트','투썸']},
    {'학번': '20251185', '이름': '김수민',  '단어': ['개나리','식목일','나비','케이크','아메리카노','카페인']},
    {'학번': '20251189', '이름': '김주영',  '단어': ['잔디','꽃가루','개나리','라떼','조명','카페인']},
]

all_words = [w for m in team_data for w in m['단어']]


class Stack:
    def __init__(self, max_size=10):
        self.data = []
        self.max_size = max_size

    def push(self, item):
        if len(self.data) >= self.max_size:
            print('Stack Overflow!')
            return False
        self.data.append(item)
        return True

    def pop(self):
        if not self.data:
            print('Stack Underflow!')
            return None
        return self.data.pop()

    def top(self):
        if not self.data:
            print('Stack이 비어있습니다.')
            return None
        return self.data[-1]


stack = Stack(max_size=10)
history = []

print('사용 가능한 단어:')
for m in team_data:
    print(f"  [{m['이름']}] {' / '.join(m['단어'])}")
print()
print('명령어: push <단어> / pop / top / done(종료)')
print('-' * 40)

while True:
    try:
        cmd = input('>>> ').strip()
    except EOFError:
        break
    if not cmd:
        continue
    if cmd.lower() == 'done':
        break

    parts = cmd.split(maxsplit=1)
    op = parts[0].lower()

    if op == 'push':
        if len(parts) < 2:
            print('단어를 입력하세요. 예: push 벚꽃')
            continue
        word = parts[1].strip()
        if word not in all_words:
            print(f'  "{word}"은(는) 없는 단어입니다.')
            continue
        if stack.push(word):
            history.append(('push', word, list(stack.data)))
            print(f'  push("{word}") -> {stack.data}')
    elif op == 'pop':
        item = stack.pop()
        if item is not None:
            history.append(('pop', item, list(stack.data)))
            print(f'  pop() = "{item}" -> {stack.data}')
    elif op == 'top':
        item = stack.top()
        if item is not None:
            history.append(('top', item, list(stack.data)))
            print(f'  top() = "{item}"')
    else:
        print('알 수 없는 명령어. push / pop / top / done 을 사용하세요.')

print(f'\n총 {len(history)}개 스텝 기록 완료 → 애니메이션 시작!')


MAX_STACK = 10
BOX_H = 0.55
BOX_W = 3.6
X0    = 0.7

BG      = '#1e1e2e'
SURFACE = '#313244'
EMPTY   = '#45475a'
FILLED  = '#585b70'
TEXT    = '#cdd6f4'
IDX     = '#6c7086'
PUSH_C  = '#89dceb'
POP_C   = '#f38ba8'
TOP_C   = '#a6e3a1'
DARK    = '#1e1e2e'

fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(13, 7),
                                  gridspec_kw={'width_ratios': [1.1, 1]})
fig.patch.set_facecolor(BG)
plt.tight_layout(pad=2.5)

def draw(i):
    ax_l.cla(); ax_r.cla()
    op, item, state = history[i]

    
    ax_l.set_facecolor(BG)
    ax_l.set_xlim(0, 10); ax_l.set_ylim(0, 10)
    ax_l.axis('off')

    if op == 'push':
        code, accent, badge = f'stack.push("{item}")', PUSH_C, 'PUSH'
    elif op == 'pop':
        code, accent, badge = f'stack.pop()\n-> "{item}"', POP_C, 'POP'
    else:
        code, accent, badge = f'stack.top()\n-> "{item}"', TOP_C, 'TOP'

    ax_l.text(5, 8.5, badge, fontsize=14, color=DARK, ha='center', va='center',
              fontweight='bold',
              bbox=dict(boxstyle='round,pad=0.5', facecolor=accent, edgecolor='none'))
    ax_l.text(5, 6.2, code, fontsize=20, color=accent, ha='center', va='center',
              bbox=dict(boxstyle='round,pad=0.9', facecolor=SURFACE, edgecolor=accent, linewidth=2.5))
    ax_l.text(5, 4.2, f'Step {i+1} / {len(history)}', fontsize=12, color=TEXT, ha='center')
    ax_l.text(5, 3.2, f'size = {len(state)} / {MAX_STACK}', fontsize=12, color=TEXT, ha='center')

    owner = next((m['이름'] for m in team_data if item in m['단어']), '?')
    ax_l.text(5, 1.8, f'by {owner}', fontsize=11, color=IDX, ha='center', style='italic')

    
    ax_r.set_facecolor(BG)
    ax_r.set_xlim(0, 5)
    ax_r.set_ylim(-0.3, MAX_STACK * BOX_H + 1.0)
    ax_r.axis('off')
    ax_r.text(2.5, MAX_STACK * BOX_H + 0.6, 'STACK',
              fontsize=15, color=TEXT, ha='center', fontweight='bold')

    for j in range(MAX_STACK):
        y = j * BOX_H
        ax_r.add_patch(mpatches.FancyBboxPatch((X0, y), BOX_W, BOX_H - 0.06,
            boxstyle='round,pad=0.03', facecolor=SURFACE, edgecolor=EMPTY, lw=1))
        ax_r.text(0.45, y + BOX_H/2, str(j), fontsize=8, color=IDX, ha='center', va='center')

    pop_ghost_y = len(state) * BOX_H if op == 'pop' else None

    for j, word in enumerate(state):
        y = j * BOX_H
        is_top = (j == len(state) - 1)
        if   op == 'top'  and is_top: fc, ec, tc = TOP_C,  TOP_C,  DARK
        elif op == 'push' and is_top: fc, ec, tc = PUSH_C, PUSH_C, DARK
        else:                          fc, ec, tc = FILLED, '#7f849c', TEXT
        ax_r.add_patch(mpatches.FancyBboxPatch((X0, y), BOX_W, BOX_H - 0.06,
            boxstyle='round,pad=0.03', facecolor=fc, edgecolor=ec, lw=2))
        ax_r.text(2.5, y + BOX_H/2, word, fontsize=13, color=tc,
                  ha='center', va='center', fontweight='bold')

    if pop_ghost_y is not None:
        ax_r.add_patch(mpatches.FancyBboxPatch((X0, pop_ghost_y), BOX_W, BOX_H - 0.06,
            boxstyle='round,pad=0.03', facecolor=POP_C, edgecolor=POP_C, lw=2, alpha=0.45))
        ax_r.text(2.5, pop_ghost_y + BOX_H/2, f'<- "{item}" 제거',
                  fontsize=11, color=DARK, ha='center', va='center', fontweight='bold')

    fig.suptitle('Stack Animation', fontsize=14, color=TEXT, y=0.98)

anim = FuncAnimation(fig, draw, frames=len(history), interval=1800, repeat=True)
plt.show()