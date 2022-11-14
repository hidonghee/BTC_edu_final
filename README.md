# 📣 BTC_edu_final 📣
### 2022 BTC 클라우드 엔지니어 과정 Final Froject
##
## 🚗🚗 구축 환경 🚗🚗 
#### 1. AWS 
#### 2. Terraform 
#### 3. Kubernetes 
#### 4. Docker
##
## 🍟🍟 개발 환경 🍟🍟 
### 1. 파이참+Django
#### 🥨 가상환경 설정 하는 법 🥨
##### (1) pycham에 깃을 받아온다 => 참고 : https://ellun.tistory.com/280 (VCS에서 git 가져오기까지)

##### (2) 본인 작업 브랜치로 변경 : 본인 작업 브랜치로 checkout 
![image](https://user-images.githubusercontent.com/84059211/201602826-363fe3c2-c777-4165-9915-c87f310aece2.png)

##### (3) 깃 브랜치 확인
`````
PS C:\Users\admin\PycharmProjects\BTC_edu_final> git branch
* jihee
  main
`````

##### (4) 인터프린터 설정 : [file] > [Setting] >  [Project: BTC_edu_final] > [Python Interprinter] 에서 인터 프린터 설정
##### !!!! 원래 Django 없음 !!!!
![image](https://user-images.githubusercontent.com/84059211/201604812-7c6144ae-3336-429d-9747-3a2061fd50ab.png)

##### (5) 장고 사용을 위한 가상환경 구성 : ~~~\venv\Scripts\ 폴더로 이동해서 가상환경 .\activate 실행
`````
PS C:\Users\admin\PycharmProjects\BTC_edu_final\venv\Scripts> .\activate
`````
##### 아래와 같이 (venv)가 생긴것을 확인 할 수 있다.
`````
(venv) PS C:\Users\admin\PycharmProjects\BTC_edu_final\venv\Scripts>
`````

##### (6) 장고 설치 : 아래에서 install package
![image](https://user-images.githubusercontent.com/84059211/201607495-b545fd2c-fb00-4ced-a105-7c8b8a9cb9fe.png)

##### (7) 장고 버전 확인
`````
(venv) PS C:\Users\admin\PycharmProjects\BTC_edu_final\venv\Scripts> django-admin --version
4.1.3
`````

##### (8) 장고 실행
`````
(venv) PS C:\Users\admin\PycharmProjects\BTC_edu_final> python .\manage.py runserver
`````
![image](https://user-images.githubusercontent.com/84059211/201606916-3c3bea73-772e-4cde-afec-5724f36ac21b.png)





