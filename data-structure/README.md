## Data Structure QnA

### 자료구조(data struceture)
A. 자료구조는 전산학에서 자료를 효율적으로 이용할 수 있도록 컴퓨터(computer)에 저장하는 방법이다. 신중히 선택한 자료구조는 보다 효율적인 알고리즘(algorithm)을 사용할 수 있게한다.
- 개인적으로 자료구조가 컴퓨터 사이언스(computer science) 중 가장 중요하다고 생각한다.
- 베이스(base)가 있어야 다른 것도 응용 가능!

### Q. 선형(linear)/비선형(nonlinear)
A.
- 선형 자료구조(linear data structure): 데이터(data) 요소가 순차적으로 저장되어 있는 자료구조로, 배열(array)이나 리스트(list)처럼 단일 레벨(single-level)로 구성된다.
- 비선형 자료구조(nonlinear data structure): 트리(tree)나 그래프(graph)처럼 멀티 레벨(multi-level)로 구성되어 있고, 데이터 요소가 순차적으로 저장되어 있지 않다.
  - 멀티 레벨: 하나의 자료 뒤에 여러 개의 자료가 존재할 수 있는 것
<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/161940602-ff537471-c32a-472c-b28d-bf6a7b193478.png" alt="linear, nonlinear image" width="800" height="450"><br/>
  <a href="https://allg.tistory.com/29">사진 출처</a>
</p>

### Q. 배열(array)
A. 배열은 메모리(memory)에 데이터를 연속적으로 저장한다. 인덱스(index)로 조회할 수 있기 때문에 random access가 가능하다. 그러나 삽입(insert)과 삭제(delete)시 앞에 요소들을 이동해야 하기 때문에 더 많은 비용이 발생한다.
- 조회: O(1)
- 삽입/삭제: O(n)
- 배열과 리스트는 명백히 다른 의미
- 배열의 삽입은 맨 뒤에서부터 발생한다.

### Q. 단순 연결 리스트(singly linked-list)
A. 단순 연결 리스트는 노드(node)에 다음 노드의 주소(address)를 가리키는 정보만 추가되어있는 가장 단순한 형태의 연결리스트다.
- 조회 시 다음 데이터를 계속 확인하며(전체 순회) 가야 하기 때문에 O(n)만큼의 시간이 걸린다.
- 삽입할 때는 헤드(head)의 주소를 변경하고, 삭제 시에는 연결되어 있던 노드의 정보만 바꾸면 되기 때문에 O(1)만큼의 시간이 걸린다.
- 다음 노드를 참조하는 주소 중 하나가 잘못되는 경우에 리스트가 끊어져 뒤쪽 자료를 유실할 수 있는 불안정적인 자료구조다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/161942563-209ec797-4330-468f-97d0-750882d1f540.png" alt="singly linked-list image" width="800" height="450"><br />
  <a href="https://freestrokes.tistory.com/84">사진 출처</a>
</p>
### Q. 이중 연결 리스트(doubly linked-list)
A. 이중 연결 리스트는 다음 노드뿐만 아니라 이전 노드의 주소도 추가되어있는 연결 리스트다.
- 단순 연결리스트와 달리 뒤에서부터 탐색이 가능하고, 특정 노드를 삭제하는데 훨씬 간단하게 구현할 수 있다.
- 첫 노드와 마지막 노드 중 하나를 가지고 있다면 전체 리스트를 순회할 수 있기 때문에 끊어진 리스트를 복구하는 것이 가능하다.
- 관리해야 할 참조 주소가 2개로 삽입이나 정렬(sort)의 경우 작업량이 더 많고 소모되는 메모리 양도 많다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/161953461-9391a141-870b-4ddd-90b2-3723002f677d.png" alt="doubly linked-list image" width="800" height="450"><br />
  <a href="https://opentutorials.org/module/1335/8940">사진 출처</a>
</p>

### Q. 스택(stack)/큐(queue)/덱(deque)
A.
- 스택: 스택은 먼저 삽입된 데이터가 가장 마지막에 제거되는 후입선출(last-in first-out) 형태의 자료구조다. 간단하게는 배열로 구현할 수 있으며, 연결리스트를 이용하여 구현할 수 있다.
- 큐: 큐는 먼저 삽입된 데이터가 가장 먼저 제거되는 선입선출(first-in first-out) 형태의 자료구조다. 보통 연결리스트를 이용하여 구현한다.
- 덱: 큐와 스택의 장점만 살린 자료구조
  - 데이터를 맨 뒤에 넣는 것이 아닌 앞에서 넣는 것도 가능하며, 맨 뒤의 데이터나 맨 앞에 데이터도 꺼낼 수 있다.

### Q. 리스트(list)/셋(set)
A.
- 리스트: 중복 데이터를 허용하고, 순서가 유지되는 선형 자료구조다.
- 셋: 집합의 개념으로 중복된 데이터를 허용하지 않으며 순서도 유지되지 않는다. -> 정렬 불가능

### Q. 해시(hash)
A. 해시는 가변 길이 데이터를 해시 함수를 통해 고정 길이 데이터로 바꾸는 것을 말한다.
- 나눗셈 법: 입력 값을 해시테이블(hash table) 크기로 나누고, 나머지를 테이블의 주소로 사용
  - eg. 입력 값: 5,000/테이블 크기: 18,000 -> 5,000 % 18,000 = 5,000 -> 주소로 사용

### Q. 해시테이블(hash table)
A. 해시테이블은 키(key), 값(value)로 데이터를 저장하는 자료구조다. 해시테이블에서는 내부적으로 배열을 사용하여 저장하고, 키 값에 해시함수(hash function)를 적용해 인덱스를 만들고, 이를 활용하여 값을 조회하거나 저장한다.
- key의 중복을 허용하지 않는다.
- 데이터를 다룰 때 인덱스를 활용(내부적으로 배열이기 때문)하기 때문에 빠른 검색 속도를 갖는다.
- 사진에서 오른쪽 버킷(bucket)을 인덱스로 접근

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/161945053-1b0b2597-bbae-4078-a9cd-5955663b8206.png" alt="hash table image" width="800" height="450"><br />
  <a href="https://ko.wikipedia.org/wiki/%ED%95%B4%EC%8B%9C_%ED%85%8C%EC%9D%B4%EB%B8%94">사진 출처</a>
</p>

### Q. 해시충돌(hash collision)
A. 해시에서 가장 문제가 되는 경우가 바로 해시충돌이다. 해시함수를 통해 반환되는 값을 무한정으로 둘 수 없어 서로 다른 데이터가 동일한 해시코드(hash code)가 될 수 있는 것이다. 이를 해결하기 위해 보통 개별체이닝(seperate chaining)과 오픈어드레싱 방식을 사용한다.
- 해시코드: 키 -> 해시함수 -> 해시코드(인덱스)

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/161945705-02cffd55-2f7e-4e49-b798-bcd5293334a0.png" alt="hash collision image" width="800" height="450"><br />
  <a href="https://yjshin.tistory.com/entry/%EC%95%94%ED%98%B8%ED%95%99-%ED%95%B4%EC%8B%9C-%ED%95%A8%EC%88%98-%EC%9E%91%EC%84%B1-%EC%A4%91">사진 출처</a>
</p>

### 개별체이닝(seperate chaining)
A. 해시테이블 내부에 있는 버킷(bucket)을 유연하게 만들어 모든 데이터를 해시테이블에 담는 방식이다. 충돌이 발생했을 경우 연결리스트로 다음 노드에 데이터를 추가해준다.
- 기본적인 자료구조(연결리스트)와 간단한 알고리즘 사용
- 모든 데이터를 담을 수 있다.
- 메모리 문제를 야기할 수 있다. -> 하나의 해시코드 값에 계속 데이터가 쌓일 경우, 다른 버킷은 비어있을 수 있다.
- 성능 저하를 야기할 수 있다. -> 하나의 해시코드 값에 계속 데이터가 쌓일 경우, 조회할 때 많은 비용이 발생할 수 있다. -> 연결리스트는 조회 시 O(n)만큼의 시간이 소요되기 때문이다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/161946472-d960d2f0-b017-48e7-b97c-994c673a3c35.png" alt="seperate chaining image" width="800" height="450"><br />
  <a href="https://8iggy.tistory.com/102">사진 출처</a>
</p>

### 오픈 어드레싱(open addressing)
A. 버킷 당 들어가는 엔트리(entry) 수를 1개로 제한하고, 충돌이 발생했을 때 빈 버킷에 데이터를 넣어주는 방식이다. 대표적으로 선형탐사(linear-probing)와 제곱탐사(quadratic-probing)가 있다.
- 선형탐사: 충돌이 발생하면 해당 위치부터 순차적으로 하나씩 탐사해 빈 버킷에 엔트리를 넣어주는 방식이다.(아래 사진과 동일 interval = 1)
  - 구현 방법이 간단하면서 의외로 전체적인 성능이 좋은편이다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/161947584-bf6dac25-2bf0-4fbb-87ee-509f8bcabd30.png" alt="open addressing image" width="800" height="450"><br />
  <a href="https://8iggy.tistory.com/102">사진 출처</a>
</p>

- 제곱탐사: 충돌이 발생하면 제곱만큼 뛴 버킷에 넣어줘 선형탐사에 비해 더 폭넓게 탐사하기 때문에 탐색과 삭제에 효율적일 수 있다.
  - 초기 해시 값이 같을 경우에 클러스터링(clustering) 문제가 발생하게 된다.
  - 클러스터링(clustering): 한 곳에 데이터가 집중되는 현상

두 방식의 클러스터링 문제를 해결하는 방법으로는 이중해싱(double-hashing)이 있다.
- 이중해싱(double-hashing): 처음 해시함수로는 해시 값을 찾기 위해 사용하고, 두 번째 해시함수로는 충돌이 발생했을 때 탐사 폭을 계산하기 위해 사용되는 방식이다.

### 개별체이닝 vs 오픈 어드레싱
- 체이닝 방식은 데이터를 무한정 저장할 수 있지만, 오픈 어드레싱 방식은 정해진 버킷의 개수 이상은 저장할 수 없으며, 모든 데이터가 반드시 자신의 해시 값과 일치하는 주소에 저장된다는 보장이 없다.
- 체이닝 방식보다 오픈 어드레싱 방식은 연속된 공간에 데이터를 저장하기 때문에 캐시(cash) 효율이 높다. 따라서 데이터 개수가 충분히 적다면 오픈 어드레싱이 개별 체이닝보다 성능이 더 좋지만, 배열의 크기가 커질수록 L1, L2 캐시 적중률(hit-rate)이 낮아지기 때문에 캐시 효율의 장점은 사라진다.

### Q. 트리(tree)
A. 트리는 대표적인 비선형 자료구조로 방향성이 있는 비순환 그래프의 한 종류이다.
- 이진트리(binary-tree): 각 노드가 최대 두 개의 자식(child) 노드를 갖는 트리 -> 포화 이진트리(perfect binary-tree), 완전 이진트리(complete binary-tree), 정 이진트리(full binary-tree)
- 이진탐색트리(binary-search tree): 왼쪽(left) 서브(sub) 트리에는 부모(parent) 노드보다 작은 값, 오른쪽(right) 서브 트리에는 부모 노드보다 큰 값을 갖는 트리이다.

이진트리는 하나의 부모가 두 개의 자식밖에 갖지 못하고, 자칫 균형이 맞지 않으면 검색 효율이 선형검색(linear-search) 급으로 떨어진다. 이것을 개선한 트리가 비트리(b tree) 비플러스트리(b+ tree)가 있다.

### Q. 비트리(b tree)
A. 기존의 이진트리를 확장하여 더 많은 수의 자식 노드를 가질 수 있게 일반화한 것이며 균형트리다.
- 키 값을 이용해 찾고자 하는 데이터를 트리 구조를 이용해 찾는 것이다.
- 어떤 값에 대해서도 같은 시간의 결과를 얻을 수 있다. -> 균형트리
- 생성 당시에는 균형트리 -> 테이블(table) 갱신을 반복하면 서서히 균형이 깨지고, 성능이 악화된다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/161949628-be4889b2-a870-4bae-add5-6920d4ef46df.png" alt="b tree image" width="800" height="450"><br />
  <a href="https://rebro.kr/169">사진 출처</a>
</p>

### Q. 비플러스트리(b+ tree)
A. 비트리를 개선한 트리가 비플러스트리다.
- 리프(leaf)노드를 제외한 모든 노드는 키만 저장할 수 있으며 데이터는 리프노드에만 저장한다.
- 다른 노드에는 키만 저장하기 때문에 메모리 공간을 효율적으로 사용할 수 있다.
- 데이터를 전체 순회할 때 리프노드끼리는 연결리스트로 연결되어 있기 때문에 한 번의 탐사로 전체 순회를 할 수 있다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/161949963-43d530ae-2b31-4916-94bc-24d5ef70a087.png" alt="b+ tree image" width="800" height="450"><br />
  <a href="https://velog.io/@emplam27/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-B-Plus-Tree">사진 출처</a>
</p>

### Q. 트리의 순회(tree traversal)
A. 
- 전위순회(preorder): 루트(root) -> 왼쪽 -> 오른쪽(A-B-D-G-H-E-C-F-I-J)
- 중위순회(inorder): 왼쪽 -> 루트 -> 오른쪽(G-D-H-B-E-A-C-I-F-J)
- 후위순회(postorder): 왼쪽 -> 오른쪽 -> 루트(G-H-D-E-B-I-J-F-C-A)

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/161950233-30108a4c-354a-497d-a445-57ca49e206a9.png" alt="tree example" width="800" height="450"><br />
  <a href="https://reakwon.tistory.com/36">사진 출처</a>
</p>

### Q. 트라이(trie)
A. 트라이는 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조다. 단순하게 하나씩 비교하면서 탐색하는 것보다 훨씬 효율적이다. 그러나 각 노드에서 자식들에 대한 포인터(pointer)를 배열로 모두 저장하고 있다는 점에서 저장 공간의 크기가 크다는 단점도 있다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/161951484-37f950d3-6daf-4d7e-ab24-b9139f5a29bc.png" alt="trie image" width="800" height="450"><br />
  <a href="https://twpower.github.io/187-trie-concept-and-basic-problem">사진 출처</a>
</p>

### Q. 힙(heap)
A. 힙은 완전 이진트리의 일종으로 우선순위 큐(priority-queue)를 위하여 만들어진 자료구조다.(최소힙, 최대힙)
- 우선순위 큐(priority-queue): 데이터의 넣은 순서에 상관없이 데이터의 값으로 순서가 정해지는 자료구조
- 반정렬 상태
- 중복 허용
- 삽입은 가장 마지막 노드에 연결 -> 부모 노드와 데이터를 확인하여 위치 이동
- 삭제는 루트 노드부터 삭제 -> 마지막 노드에 있는 데이터를 루트로 이동 -> 자식 노드와 비교하며 위치 이동(왼쪽 자식과 오른쪽 자식의 숫자가 같을 경우엔 아무거나 선택하거나 알고리즘 사용)
- 삽입과 삭제시 비교하는 횟수가 절반씩 줄기 때문이 O(logn)
