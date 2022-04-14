## Design Pattern QnA

### Q. 디자인 패턴(design pattern)

A. 디자인 패턴이란 요리 레시피에 비유할 수 있다. 실제 개발 현장에서 만들어진 다양한 해결책 중 best practice를 정리한 것이다.

### Q. 어댑터 패턴(adapter pattern)

A. 어댑터(adapter)는 서로 다른 두 인터페이스(interface)의 통신을 가능하게 해준다. 어댑터 패턴은 호출 당하는 쪽의 메서드(method)를 호출하는 쪽의 메서드에 대응하도록 중간에 어댑터를 두는 패턴이다.

- [함께 보면 좋을 것](https://jusungpark.tistory.com/22)

### Q. 프록시 패턴(proxy pattern)

A. 프록시(proxy)는 다른 누군가를 대신해 그 역할을 수행하는 존재를 말한다. 그래서 제어 흐름을 조정하기 위한 목적으로 중간에 대리자를 두는 패턴이다.

- [함께 보면 좋을 것](https://limkydev.tistory.com/79)

### Q. 데코레이터 패턴(decorator pattern)

A. 원본에 장식을 덧 입히는 패턴이다. 프록시와 비슷핮디만 결과 값이 다르다는 차이를 갖고있다.

- [함께 보면 좋을 것](https://gmlwjd9405.github.io/2018/07/09/decorator-pattern.html)

### Q. 싱글톤 패턴(singleton pattern)

A. 클래스(class)의 객체(object), 즉 인스턴스(instance)를 하나만 만들어 사용하기 위한 패턴이다. 즉 필요할 때마다 인스턴스를 생성하는 것이 아니라 기존의 인스턴스를 재활용하는 것이다. 예를 들어, 로그(log)를 남길 때마다 로거(logger) 객체를 생성해서 사용한다면 힙(heap)에 객체를 계속 할당하니까 자원을 그만큼 소모하는 것이다. 따라서 단 하나의 로거 객체만 만들어서 로그를 남길 때마다 같은 객체를 가져다 사용한다. (private 생성자, 정적 변수로 객체 생성, 정적 메소드로 객체 반환)

### Q. 이터레이터 패턴(iterator pattern)

A. 무언가 많이 모여있는 것을 하나씩 지정해서 순서대로 처리하는 패턴이다. for문에서 변수 i의 역할을 추상화한 것으로 보면 된다. 하나씩 꺼내서 처리하는 과정을 구현과 분리할 수 있다.

- [함께 보면 좋을 것](https://jusungpark.tistory.com/25)

### Q. mvc 패턴(model-view-controller pattern)

A. 하나의 애플리케이션(application)을 만들 때 구성 요소를 model, view, controller 세 가지 역할로 구분하는 패턴이다. 사용자가 컨트롤러에 요청하면 컨트롤러는 모델을 통해 데이터를 가져오고 해당 정보를 뷰를 통해 사용자에게 전달한다. 컨트롤러만 모델이나 뷰에 대해 알고 있고, 나머지는 서로의 구성 요소들을 몰라야 한다.

### Q. 템플릿 메서드 패턴(template method pattern)

A. 추상 클래스(abstract class)/구현 클래스(implement class)로 구분해서 사용하는 패턴이다.

### Q. 팩토리 메소드 패턴(factory method pattern)

A. 객체를 만드는 부분을 sub 클래스에 맡기는 패턴이다. 구체적으로 말하면 객체를 생성하는 부분을 따로 만들고, 넘어오는 객체에 따라서 다른 결과 값을 만들어내는 패턴이다.

### Q. 전략 패턴(strategy pattern)

A. 어떤 동작을 하는 로직을 정의하고, 이것들을 하나로 묶어 관리하는 패턴이다. 새로운 로직을 추가하거나 변경할 때 한번에 효율적으로 변경이 가능하다.
