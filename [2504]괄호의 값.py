from collections import deque
k = input().rstrip()
point = {')': 2, ']': 3}  # 괄호의 점수
pair = {')': '(', ']': '['}  # 닫는 괄호의 짝꿍


def operate():
    st = deque()
    for x in k:
        if x in ['(', '[']:  # 여는 괄호는 무조건 집어넣는다
            st.append(x)
        else:
            tmp = 0  # 괄호열 계산 결과
            while st and st[-1] not in ['(', '[']:  # 스택 안에 숫자가 들어있는 동안 계속 뽑아내서 tmp에 더한다
                tmp += st.pop()
            if st and st[-1] == pair[x]:  # 스택 top의 괄호와 x가 짝꿍이 맞을 때
                st.pop()  # 여는 괄호 꺼낸다
                if tmp == 0:  # ()와 같이 괄호로만 이뤄져 있는 경우
                    st.append(point[x])
                else:  # [()]과 같이 괄호열이 내부에 있던 경우
                    st.append(point[x] * tmp)  # tmp는 내부 괄호열 계산 결과
            else:
                print(0)
                return
    try:
        print(sum(st))
    except TypeError:  # 안 닫힌 괄호가 존재하는 에러 핸들링
        print(0)


operate()
