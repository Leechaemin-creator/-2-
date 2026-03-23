#include <iostream>
#include <string>

using namespace std; // std::string을 포함한 표준 라이브러리 사용

const int MAX_STACK_SIZE = 10;

class ArrayStack {
    int top;
    string data[MAX_STACK_SIZE];

public:
    ArrayStack() { top = -1; }

    bool isEmpty() { return top == -1; }
    bool isFull() { return top == MAX_STACK_SIZE - 1; }

    void push(string s) {
        if (isFull()) {
            cout << "스택 포화 에러" << endl;
            return; // 더 이상 진행하지 않도록 종료
        }
        data[++top] = s;
    }

    string pop() {
        if (isEmpty()) {
            cout << "스택 공백 에러" << endl;
            return ""; // 빈 문자열 반환 혹은 예외 처리
        }
        cout << "pop 결과: " << data[top] << endl;
        return data[top--]; // 값을 먼저 리턴하고 top 감소

    }

    string peek() {
        if (isEmpty()) {
            cout << "스택 공백 에러" << endl;
            return "";
        }
        return data[top]; // 현재 맨 위 값만 확인
    }

    void display() {
        printf("[스택 항목의 수=%2d] ==> ", top + 1);
        for (int i = 0; i <= top; i++) {
            // string 객체는 printf에서 %s로 출력할 때 .c_str()이 필요합니다.
            printf("<%s> ", data[i].c_str());
        }
        printf("\n");
    }
};

int main() {
    ArrayStack stack;

    stack.push("벚꽃");
    stack.push("개강");
    stack.push("소풍");

    stack.display();
    stack.pop();

    stack.push("연인");
    stack.push("석촌호수");
    stack.push("커피");

    stack.display();
    stack.pop();

    stack.push("바리스타");
    stack.push("원두");
    stack.push("잔디");

    stack.display();
    stack.pop();

    stack.push("생일");
    stack.push("아메리카노");
    stack.push("갈색");

    stack.display();
    stack.pop();
    stack.display();
    stack.pop();
    stack.display();
    stack.pop();
    stack.display();
    stack.pop();

    stack.push("중간고사");
    stack.push("봄동");
    stack.push("카페라테");

    stack.display();
    stack.pop();
    stack.display();
    stack.pop();

    stack.push("디저트");
    stack.push("투썸");

    stack.display();
    stack.pop();

    stack.push("개나리");
    stack.push("식목일");
    stack.push("나비");
    stack.display();
    stack.pop();
    stack.display();
    stack.pop();

    stack.push("케이크");
    stack.push("카페인");

    stack.display();
    stack.pop();
    stack.display();
    stack.pop();

    stack.push("꽃가루");
    stack.push("조명");


    stack.display();
    stack.pop();



    return 0;
}