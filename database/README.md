## Database QnA

### Q. 데이터베이스 키(database key)

A. 데이터베이스(database)에서 키(key)란 검색 정렬(sort) 시 튜플(tuple)을 구분할 수 있는 기준이 되는 속성(attribute)이다.

- 후보 키(candidate key): 튜플을 유일하게 식별할 수 있는 속성들의 부분집합이다. 즉 기본 키(primary key)로 사용할 수 있는 속성들이며, 테이블(table) 내부에 있는 모든 튜플들에 대해 유일성과 최소성을 만족 해야한다.

- 기본 키(primary key): 후보 키 중 선택된 메인 키(main key)이다. 널(null) 값을 가져서는 안되며 동일한 값을 가질 수 없다.
- 대체 키(surrogate key): 후보 키 중 기본 키를 제외한 나머지 키이다. 보조 키라고도 불린다.
- 슈퍼 키(super key): 슈퍼 키는 한 테이블 내에 있는 속성들의 집합으로 구성된 키로써 테이블을 구성하는 모든 튜플 중 슈퍼 키로 구성된 속성의 집합과 동일한 값을 나타나지 않는다. 테이블을 구성하는 모든 튜플에 대해 유일성을 만족시키지만 최소성은 만족시키지 못한다.
- 외래 키(foreign key): 관계를 맺고 있는 테이블 키다.

### Q. 조인(join)

A. 관계형 데이터베이스에서는 중복 데이터를 피하기 위해서 데이터를 쪼개 여러 테이블로 나누어서 저장한다. 이렇게 분리되어 저장된 데이터에서 원하는 결과를 다시 도출하기 위해서는 여러 테이블을 조합할 필요가 있다. 관계형 데이터베이스에서는 조인 연산자를 사용해 관련 있는 칼럼을 기준으로 행을 합쳐주는 연산이다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/163299111-00e9d290-9504-4ece-ae16-0f074bb2b6b5.png" alt="join image" width="800" height="450"><br/>
  <a href="https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=chsmanager&logNo=140202016634">사진 출처</a>
</p>

### Q. sql(structured query language) injection

A. sql injection은 해커에 의해 조작된 sql 쿼리문이 데이터베이스에 그대로 전달되어 비정상정 명령을 실행시키는 공격기법이다. 대표적으로 논리적 에러(error-based)와, 유니온(union) 키워드(keyword)를 이용한 union-based가 있다.

- 논리적 에러(error-based) sql injection: 논리적 에러를 이용한 것이며 가장 많이 쓰이고 대중적인 공격기법이다.

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/163299313-50132d19-582f-4c6f-b528-3cca7a359d06.png" alt="error based sql injection image" width="800" height="450"><br />
  <a href="https://noirstar.tistory.com/264">사진 출처</a>
</p>

- 유니온 베이스(union-based) sql injection: union 명령어를 이용한 공격기법이다.
  - union: 두 개의 쿼리문에 대한 결과를 통합해서 하나의 테이블로 보여주는 키워드

<p align="center">
  <img src="https://user-images.githubusercontent.com/78870076/163299840-1b4ca910-9093-450c-b010-9f4a0e57523c.png" alt="union based sql injection image" width="800" height="450"><br />
  <a href="https://noirstar.tistory.com/264">사진 출처</a>
</p>

방어 대책으로는 값을 받을 때 검증하고, 또한 에러(error)시 해당하는 에러 메시지(error message)를 감춘다. 그리고 특수 문자를 자동으로 제거해주는 preparestatement 키워드를 사용한다.

### Q. sql 종류

A. sql 종류에는 데이터(data)를 정의하는 ddl, 데이터를 조작하는 dml, 데이터를 제어하는 dcl, 트랜잭션을 제어하는 tcl이 있다.

- ddl(data definition language): 테이블과 같이 데이터 구조를 정의하는 명령어로 대표적으로 create, alter, drop 등이 있다.
- dml(data manipulation language): 데이터 조회, 삽입, 수정 등 데이터에 변형을 가하는 명령어로 대표적으로 select, insert, delete, update 등이 있다.
- dcl(data control language): 데이터베이스에 접근하거나 객체(object) 사용을 위한 권한(permission)을 주거나 회수하는 명령어로 대표적으로 revoke, grant 등이 있다.
- tcl(transaction control language): dml에 의해 조작된 결과가 트랜잭션(transaction) 별로 반영되는 명령어로 대표적으로 commit, rollback이 있다.

### Q. sql vs nosql

A.

- sql: sql은 대표적인 관계형 데이터베이스(relational database)이다. 관계형 데이터베이스의 가장 큰 특징은 명확한 스키마(schema)와, 데이터간의 관계이다. 관계를 맺고 있어 데이터를 중복없이 한 번만 저장할 수 있지만, 스키마를 사전에 계획하고 알려야 하므로 덜 유연하며 관계를 맺고 있기에 많은 조인 연산을 유발할 수 있다.
- nosql: nosql은 말 그대로 sql을 사용하지 않는 것으로 스키마도 없고, 관계도 없다. 다른 구조를 갖는 데이터를 같은 컬렉션(collection)에 추가하는 것이 가능한 이미 모든 것을 갖춘 문서를 작성하는 것이 nosql이다. 스키마가 없기 때문에 유연하며 애플리케이션(application)이 필요로 하는 형태로 문서가 작성되기 때문에 읽어오는 속도 또한 빠르다. 그러나 중복 데이터를 갱신해야 하는 비용이 sql 보다 더 많이 든다는 단점을 갖고있다.

### Q. 수직적 확장(scale up)/수평적 확장(scale out)

A.

- 수직적 확장(scale up): 단순히 데이터베이스의 서버의 성능을 향상시키는 것(sql, nosql)
- 수평적 확장(scale out): 더 많은 서버가 추가되고, 데이터베이스가 전체적으로 분산되는 것(nosql)

### Q. 인덱스(index)

A. 관계형 데이터베이스에서 인덱스란 검색 속도를 높이기 위한 기술이다. 인덱스는 기본적으로 b+ tree 구조를 갖고있다.

- [b+ tree 설명](https://github.com/m1nnh/tech-interview-QnA/tree/master/data-structure#q-%EB%B9%84%ED%94%8C%EB%9F%AC%EC%8A%A4%ED%8A%B8%EB%A6%ACb-tree)

### Q. 정규화(normalization)

A. 관계형 데이터베이스에서 중복을 최소화 하기 위해 데이터를 구조화하는 작업이다. 구체적으로 말하면 하나의 종속성이 하나의 릴레이션(relation)으로 표현될 수 있도록 분해해가는 과정이라고 할 수 있다.

- 1차 정규화: 같은 성격과 내용이 연속적으로 나타내는 컬럼(column)이 있을 때 기본 테이블에 pk를 설정하고, 새로운 테이블에 해당하는 컬럼들을 옮기며 1:n 관계를 맺어주는 것이다.
- 2차 정규화: 주식별자가 아닌 속성 중에서 주식별자 전체가 아닌 일부 속성에 종속된 속성을 제거하는 과정이다.
- 3차 정규화: 주식별자가 아닌 속성 중에서 종속된 속성을 제거하는 과정이다.

### Q. 반정규화(de-normalization)

A. 하나 이상의 테이블에 데이터를 중복 배치하여 최적화하는 것을 의미한다. 효율적인 쿼리를 사용하기 위해 사용하며, 데이터 갱신 비용을 감수해야 한다.

### Q. 트랜잭션(transaction)

A. 트랜잭션은 데이터베이스의 상태를 변화시키는 하나의 논리적인 작업단위다. 쉽게 말해서 한꺼번에 수행되어야할 일련의 연산인데, 주로 데이터 부정합을 방지하기 위해 사용한다. 트랜잭션의 특징은 acid 4가지가 있다.

- 원자성(atomicity): 트랜잭션은 더 이상 분해할 수 없는 최소 단위이기 때문에 all or nothing 전략을 수립해야 한다.
- 일관성(consistency): 트랜잭션 수행 전 후 데이터가 모순되지 않고 일관성이 있어야 한다는 의미이다.
- 고립성, 독립성(isolation): 트랜잭션 수행 중에 다른 트랜잭션이 끼어들면 안된다는 의미이다.
- 영속성(durability): 트랜잭션 정상 종료 후 영구적으로 데이터베이스에 반영되어야 한다는 의미이다.

### Q. 트랜잭션 격리 수준(isolation level)

A. 트랜잭션 격리 수준은 여러 트랜잭션이 동시에 처리될때, 특정 트랜잭션에서 다른 트랜잭션에서 테이블을 조회하거나 변경한 테이블을 볼수 있게 할지 말지 결정하는 문제다. 크게 4단계로 구성되어 있으며 뒤로 갈수록 고립성은 높지만 동시처리 성능이 떨어진다.

- 0단계(read uncommitted): 트랜잭션 commit, rollback 상관없이 다른 트랜잭션에서 데이터를 읽을 수 있다. 그러나 읽어들인 데이터가 변경된 테이블에 없는 dirty read가 발생할 수 있다.
- 1단계(read committed): 커밋된 내용만 읽을 수 있다. 그러나 repeatable read 정합성에 어긋난다.
  - repeatable read: select할 때마다 같은 결과가 나와야 하는 것을 의미한다.
- 2단계(repeatable read): 트랜잭션이 수행하기 전 커밋된 내용에 대해서만 읽어들일 수 있다. 그러나 같은 쿼리를 두 번 실행했을 때 기존에 없었던 레코드(record)가 나타나는 phantom read가 발생한다.
- 3단계(serializable): 가장 간단하고, 고ㅗ립성이 높지만 동시처리 성능이 매우 낮아 거의 사용하지 않는다.

### Q. undo/redo

A. 트랜잭션과 무관하게 버퍼(buffer) 상태에 따라 버퍼 교체가 일어난다.

- undo: 정상적으로 종료되지 않아 복구하는 작업
- redo: 정상 종료된 트랜잭션의 결과를 재반영 하는 것
