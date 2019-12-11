v.0.1
[본래 GUI 개발 계획]

** PyQt5(GUI) 사용

1) 처음 화면 : 캠퍼스 지도와 출도착지 선택 박스를 보여준다
-> 캠퍼스 지도를 캡쳐함, 캡쳐한 이미지를 화면에 띄움
-> 오른쪽 상단에 PyQt5 QComboBox를 이용하여 출발지와 도착지를 선택할 수 있는 박스를 띄움

2) 출발지와 도착지 선택 : 출발지와 도착지에 마커 표시가 된 지도 이미지와 도착 예정 시간을 보여준다
-> 캠퍼스 지도에 각 도착지와 출발지에 따라 마커 표시한 이미지를 새로 만들고 저장함, 화면에 띄움

3) 지도에 이동경로 표시 : 가장 빠른 경로를 지도에 표시해준다.


[단점]
1. 지도를 확대, 축소 할 수 없다.
-> 캠퍼스 지도를 캡쳐한 것이기 때문에, 길이나 건물정보를 자세하게 보고 싶어도 확대해서 볼 수 없다.

2. 기숙사, 한대앞과 같은 거리가 먼 경로의 경우 마커를 한 화면에 표시할 수 없다.
-> 이미지 크기의 제약으로 마커를 한 화면에 표시하려면 배율을 줄여야한다. 그러면 상세 경로를 볼 수 없다.

3. 막대한 노동 필요
-> 약 200가지 경로에 대한 마커 표시, 경로 표시 이미지를 일일이 수작업 해야 된다.

4. 디자인
-> 지도를 캡쳐한 이미지이기 때문에 조작 했을 때 부자연스러운 느낌이 있으며 안예쁘다.



v.0.2
[1차 바뀐 계획]

** PyQt5(GUI) + folium(MAP)

1) 처음 화면 : 캠퍼스 지도와 출도착지를 보여준다.
-> folium으로 캠퍼스 건물 정보를 알 수 있는 지도를 띄우고 오른쪽에 출도착지를 선택하는 박스를 띄움

2) 출도착지 선택 : 출도착지에 마커 표시를 하고 경로를 보여준다.
-> 한 화면에 출도착지가 모두 보이게 하고, 사용자가 직접 화면 배율을 조절할 수 있다. 이동 경로는 확대, 축소해도 유지된다.

3) 도착예정시간 : 화면에 도착예정시간을 띄운다.

4) 셔틀 시간표 : 셔틀콕 아이콘을 클릭하거나 마우스를 가져다 대면 셔틀 시간표를 보여준다.


[오류] : PyQt5와 html페이지를 연결하는 과정에서 이유를 알 수 없는 오류가 발생함. PyQt5를 대체하여 tkinter 모듈을 gui 구현에 적용




v.0.3
[2차 바뀐 계획]

** tkinter(GUI) + folium(Map)

1) 처음 화면 : tkinter로 장소검색 버튼, 출도착지 선택 버튼, 적용하기 버튼이 나타난다.

2) 장소검색 버튼을 누르면 지도와 search box, gps 기능을 사용할 수 있는 웹페이지로 넘어간다.

3) 출도착지 선택 버튼은 combobox기능으로 선택지를 확인하고 선택할 수 있게한다.

4) 적용하기 버튼을 누르면 도착확인 시간과 함께 경로확인 확인하기 버튼이 나타난다.
-> 경로확인 버튼을 누르면 지도에 경로가 그려져있는 웹페이지로 넘어간다.

