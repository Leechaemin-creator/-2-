from manim import *

class StackAnimation(Scene):
    def construct(self):

        font_name = "Malgun Gothic" 

       
        code_title = Text("실행 중인 코드:", font=font_name, font_size=30, color=GRAY).to_corner(UL).shift(DOWN*0.5 + RIGHT*0.5)
        code_anchor = Dot(code_title.get_left() + DOWN*0.8).fade(1) 
        self.add(code_title, code_anchor)

        
        code_line = Text("stack = []", font=font_name, font_size=36).next_to(code_anchor, RIGHT)
        self.play(Write(code_line), run_time=1)
        self.wait(0.5)

       
        stack_start_pos = RIGHT * 3.5 + DOWN * 2.5
        BOX_WIDTH = 2.5
        BOX_HEIGHT = 0.6
        stack_mobjects = [] 

        def create_box(word):
            """박스와 글자를 묶어주는 함수"""
            box = Rectangle(width=BOX_WIDTH, height=BOX_HEIGHT, color=WHITE, fill_color=BLACK, fill_opacity=1)
            text = Text(word, font=font_name, font_size=24).move_to(box.get_center())
            return VGroup(box, text)

        
        words = [
            "개나리", "식목일", "나비", "케이크", "아메리카노", "카페인", "중간고사", 
            "봄동", "카페라떼", "디저트", "투썸", "벚꽃", "잔디", "생일", "갈색", 
            "원두", "정원", "목련", "소음", "연인", "석촌호수", "파우더", "우유", 
            "커피", "바리스타", "개나리", "꽃가루", "라떼", "조명", "소풍", "개강", "알바"
        ]

        
        actions = []
        current_stack = []
        for word in words:
            if len(current_stack) >= 8: 
                actions.append(("top", current_stack[-1]))
                actions.append(("pop", current_stack.pop()))
                actions.append(("pop", current_stack.pop()))
                actions.append(("pop", current_stack.pop()))
            actions.append(("push", word))
            current_stack.append(word)

        
        if current_stack:
            actions.append(("top", current_stack[-1]))
            actions.append(("pop", current_stack.pop()))

       
        for action, arg in actions:
            if action == "push":
                
                new_code = Text(f'stack.push("{arg}")', font=font_name, font_size=36, color=YELLOW).next_to(code_anchor, RIGHT)
                self.play(Transform(code_line, new_code), run_time=0.3)
                
              
                box = create_box(arg)
                box.move_to(stack_start_pos + UP * (len(stack_mobjects) * BOX_HEIGHT))
                self.play(FadeIn(box, shift=DOWN*0.3), run_time=0.7)
                stack_mobjects.append(box)

            elif action == "pop":
                new_code = Text(f'stack.pop() -> "{arg}"', font=font_name, font_size=36, color=RED).next_to(code_anchor, RIGHT)
                self.play(Transform(code_line, new_code), run_time=0.3)
                
                popped_box = stack_mobjects.pop()
                self.play(FadeOut(popped_box, shift=UP*0.3), run_time=0.7)

            elif action == "top":
                new_code = Text(f'stack.top() -> "{arg}"', font=font_name, font_size=36, color=BLUE).next_to(code_anchor, RIGHT)
                self.play(Transform(code_line, new_code), run_time=0.3)
                
                top_box = stack_mobjects[-1]
                self.play(Indicate(top_box, color=YELLOW_C, scale_factor=1.1), run_time=0.7)

        self.wait(2) 
