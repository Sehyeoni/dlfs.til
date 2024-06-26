# Chapter6 학습 관련 기술들
이번 장에서 다룰 주제 :
* 가중치 매개변수의 최적값을 탐색하는 최적화 방법
* 가중치 매개변수 초깃값 설정 방법
* 하이퍼파라미터 설정방법
* 오버피팅 대응책 - 정규화 (가중치 감소, 드롭아웃 등)
* 배치 정규화

## 6.1 매개변수 갱신
신경망 학습의 목적 : 손실함수의 값을 가능한 낮추는 매개변수를 찾는것  = 최적화. optimization

이미 알고있는 방법 1 : SGD(Stochastic Gradient Descent 확률적 경사 하강법)<br>
SGD의 단점 : anisotropy 비등방성 함수에서는 탐색 경로가 비효율적이다. 기울어진 방향이 본래의 최솟값과 다른 방향을 가리키는 문제.

다른 방법 3가지 : 모멘텀, AdaGrad, Adam

### 6.1.4 Momentum
한 방향으로 일정하게 가속하기 때문에 지그재그의 움직임이 커지지 않고 줄어든다.

### 6.1.5 AdaGrad
학습률 감소(learning rate decay) : 학습을 진행하면서 학습률을 점차 줄여가면서 처음에는 크게 학습하다가 조금씩 작게 학습하게 한다.

간단하게는 매개변수 전체의 학습률 값을 일괄적으로 낮출 수 있겠음.<br>
AdaGrad는 이것을 발전시켜 각각의 매개변수에 맞춤형 값을 만들어준다.

과거의 기울기를 제곱하여 계속 더해가는데, 학습을 진행할수록 갱신 강도가 약해져 결국 0에 가까워진다.<br>
RMSProp 방법으로 '지수이동평균'을 적용시켜 개선이 가능하다.

과거의 모든 기울기를 균일하게 더해가는것이 아니라, 먼 과거의 기울기는 서서히 잊고 새로운 기울기 정보를 크게 반영한다.

### 6.1.6 Adam
Momentum + AdaGrad

### 6.1.7 어느 갱신 방법을 사용할 것인가?
각자의 상황을 고려해 여러가지로 시도해라.
![최적화 기법 비교](fig%206-8.png)

## 6.2 가중치의 초깃값
### 6.2.1 초깃값을 0으로 하면? 가중치를 균일한 값으로 설정하면? => 학습이 올바로 이뤄지지 않는다.
weight decay 가중치 감소 기법 : 가중치 매개변수의 값이 작아지도록 학습하는 방법. 오버피팅을 억제해 범용 성능을 높인다.

가중치를 작게 만들고 싶으면 초깃값도 최대한 작은 값에서 시작하는것이 정공법!

초깃값을 0으로 하면(가중치를 균일한 값으로 설정하면) 오차역전파법에서 모든 가중치의 값이 똑같이 갱신되기 때문에 학습이 잘 안됨.

가중치가 고르게 되어버리는(대칭적인 구조를 갖게 되는) 상황을 무너뜨리려면 초깃값을 무작위로 설정해야 함.

### 6.2.2 은닉층의 활성화값 분포
기울기 소실 문제 gradient vanishing : 역전파 기울기 값이 점저 작아지다가 사라지는 현상(0에 가까워짐)

표현력 제한 문제 : 결과값이 치우쳐 나오는 문제. 활성화 값이 치우치면 표현력을 제한한다는 관점에서 문제가 된다.

Xavier 초깃값 : 일반적인 딥러닝 프레임워크들이 표준적으로 이용하고 있음(활성화 함수가 선형일 때. 시그모이드, tanh)

### 6.2.3 ReLU를 사용할 때의 초깃값
He 초깃값 이용

## 6.3 배치 정규화 Batch Normalization
가중치의 초깃값을 적절히 설정하면 각 층의 활성화값 분포가 적당히 퍼지면서 학습이 원활하게 수행된다.<br>
각 층이 활성화를 적당히 퍼뜨리도록 강제해보자!

### 6.3.1 배치 정규화 알고리즘
배치 정규화가 주목받는 이유
* 학습을 빨리 진행할 수 있다.(학습 속도 개선)
* 초깃값에 크게 의존하지 않는다.(초깃값 선택 골치 해소)
* 오버피팅 억제(드롭아웃 등의 필요성 감소)

신경망에 배치 정규화 계층을 삽입한다.
![배치 정규화를 사용한 신경망의 예](fig%206-16.png)

거의 모든 경우에서 배치 정규화를 사용하면 학습이 빨라지고, 초깃값에 크게 의존하지 않아도 된다.

## 6.4 바른 학습을 위해
오버피팅 : 신경망이 훈련 데이터에만 지나치게 적응되어 그 외의 데이터에는 제대로 대응하지 못하는 상태

범용 성능 지향을 위해서는 오버피팅을 억제하는 기술이 중요하다.

### 6.4.1 오버피팅
오버피팅이 일어나는 경우
* 매개변수가 많고 표현력이 높은 모델
* 훈련 데이터가 적었을 때

### 6.4.2 가중치 감소
weight decay 가중치 감소 : 학습 과정에서 큰 가중치에 대해서는 그에 상응하는 큰 페널티를 부과한다.<br>
람다(정규화의 세기를 조절하는 하이퍼파라미터)값 조절. 크게 설정하면 큰 가중치에 대한 패널티가 커짐

### 6.4.3 드롭아웃
신경망이 복잡해지면 가중치 감소로는 오버피팅 대응이 어려움

Dropout : 뉴런을 임의로 삭제하면서 학습. 훈련때 은닉층의 뉴런을 무작위로 골라 삭제함.<br>
시험때에는 든 뉴런에 신호를 전달하고, 각 뉴런의 출력에 훈련 때 삭제 안한 비율을 곱하여 출력함.

* ensemble learning 앙상블 학습 : 개별적으로 학습시킨 여러개 모델의 출력을 평균내어 추론하는 방식

## 6.5 적절한 하이퍼파라미터 값 찾기
### 6.5.1 검증 데이터 validation data
하이퍼파라미터를 조정하면서도 오버피팅이 발생하므로<br>
하이퍼파라미터 전용 확인 데이터가 필요하다. 하이퍼파라미터의 적절성을 평가하는 데이터.

훈련 데이터, 검증 데이터, 시험 데이터

### 6.5.2 하이퍼파라미터 최적화
무작위로 샘플링해 탐색하는 편이 좋은 결과를 낸다고 알려져있음.

학습에 필요한 에폭을 작게 하여 1회 평가에 걸리는 시간을 단축하는것이 효과적임

[하이퍼파라미터의 최적화]
* 0단계 : 하이퍼파라미터 값의 범위 설정
* 1단계 : 설정된 범위에서 무작위 값 추출
* 2단계 : 1단계에서 샘플링한 값을 사용하여 학습, 검증 데이터로 정확도 평가. 이때 에폭 작게 설정
* 3단계 : 1-2단계 반복하여 정확도의 결과를 보고 하이퍼파라미터의 범위 좁히기

* 참조 : 베이즈 최적화 기법 Bayesian optimization

## 6.6 정리
* 매개변수 갱신 방법 : 확률적 경사 하강법, 모멘텀, AdaGrad, Adam 등이 있다.
* Xavier 초깃값 : 시그모이드, tanh에 효과적
* He 초깃값 : ReLU에 효과적
* 배치 정규화 : 빠른 학습, 초깃값 설정 골치 해소, 오버피팅 억제
* 오버피팅을 억제하는 정규화 기술 : 가중치 감소와 드롭아웃이 있다.
* 하이퍼파라미터 값 탐색은 최적값이 존재할만한 범위를 점차 좁혀가는 방식이 효과적이다.