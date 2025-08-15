# -------------------------------
# 연결 리스트의 각 노드를 나타내는 클래스
# -------------------------------
class Node:
    def __init__(self, data):
        self.data = data   # 해당 노드(요소)가 저장하는 값
        self.next = None   # 다음 노드를 가리키는 포인터(주소)
                          # 처음 생성 시에는 아무것도 가리키지 않음

# -------------------------------
# 연결 리스트를 관리하는 클래스
# (비상 연락망의 "관리자" 역할)
# -------------------------------
class SinglyLinkedList:
    def __init__(self):
        self.head = None   # 연결 리스트의 첫 번째 노드(헤드)
                          # 관리자는 첫 사람만 알면 나머지는 차례로 따라갈 수 있음

    # ---------------------------
    # 1) 맨 앞(헤드)에 새 노드 추가
    # ---------------------------
    def insert_at_head(self, data):
        new_node = Node(data)       # 새 노드 생성
        new_node.next = self.head   # 새 노드의 다음 포인터가 기존 헤드를 가리키도록
        self.head = new_node        # 헤드를 새 노드로 갱신

    # ---------------------------
    # 2) 지정한 위치에 새 노드 추가
    # ---------------------------
    def insert_at_position(self, data, position):
        # 위치가 0이면 맨 앞에 추가
        if position == 0:
            self.insert_at_head(data)
            return

        new_node = Node(data)       # 새 노드 생성
        current = self.head         # 탐색 시작: 첫 번째 노드부터

        # position-1 번째 노드까지 이동
        for _ in range(position - 1):
            if current is None:     # 범위를 벗어난 경우 (리스트 길이보다 큰 위치)
                return
            current = current.next

        if current is None:         # 유효하지 않은 위치면 추가 중단
            return

        # 새 노드의 다음 포인터를 현재 노드의 다음 노드로 연결
        new_node.next = current.next
        # 현재 노드의 다음 포인터를 새 노드로 변경 (새 노드가 연결되도록)
        current.next = new_node

    # ---------------------------
    # 3) 특정 값(key)을 가진 노드 삭제
    # ---------------------------
    def delete(self, key):
        current = self.head   # 첫 번째 노드부터 탐색
        prev = None           # 이전 노드를 저장할 변수

        while current:
            if current.data == key:     # 삭제할 값을 찾은 경우
                if prev:                # 이전 노드가 존재하면 (중간/끝 삭제)
                    prev.next = current.next
                else:                    # 이전 노드가 없으면 (맨 앞 삭제)
                    self.head = current.next
                return                   # 삭제 후 종료

            prev = current              # 이전 노드 갱신
            current = current.next      # 다음 노드로 이동

    # ---------------------------
    # 4) 특정 값 검색
    # ---------------------------
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:  # 값이 일치하면
                return True
            current = current.next   # 다음 노드로 이동
        return False                 # 끝까지 못 찾으면 False

    # ---------------------------
    # 5) 연결 리스트 순회(출력)
    # ---------------------------
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  # 현재 노드의 값 출력
            current = current.next           # 다음 노드로 이동
        print("None")  # 끝에 도달하면 None 출력

# -------------------------------
# 연결 리스트 사용 예시
# -------------------------------
ll = SinglyLinkedList()

# 맨 앞에 차례대로 값 삽입
ll.insert_at_head(17)  # 17
ll.insert_at_head(18)  # 18 -> 17
ll.insert_at_head(19)  # 19 -> 18 -> 17
ll.insert_at_head(76)  # 76 -> 19 -> 18 -> 17
ll.insert_at_head(44)  # 44 -> 76 -> 19 -> 18 -> 17

# 위치 3에 값 34 삽입
# (인덱스 0부터 시작: head=44, 1=76, 2=19, 3 위치에 삽입)
ll.insert_at_position(34, 3)  
# 결과: 44 -> 76 -> 19 -> 34 -> 18 -> 17

# 값 18 삭제
ll.delete(18)  
# 결과: 44 -> 76 -> 19 -> 34 -> 17

# 값 19 검색 (있으므로 True 반환)
print(ll.search(19))  # True

# 전체 리스트 출력
ll.traverse()
# 44 -> 76 -> 19 -> 34 -> 17 -> None
