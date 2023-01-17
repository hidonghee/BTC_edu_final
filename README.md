# ABCbit 코인 거래소 및 자동매매 서비스 구축

# 목차
[1. 개요](#개요) <br/>
[2. 인프라](#인프라) <br/>
[3. 코인거래소 ABCbit 웹페이지](#코인거래소-ABCbit-웹페이지)

<br/>

## 개요
- CSP : AWS
- 개발 및 인프라 운영, CI/CD(지속적 통합/배포)를 구현한 DvOps 프로젝트 
- EKS(Elastic Kubernetes Service)사용한 MSA(Micro Service Architecture)구축, 기능별 Pod 분리 운영

### 요구사항
![image](https://user-images.githubusercontent.com/84059211/212466540-9981747e-95fa-4e86-89f2-0c607060f703.png)

### 구축 인원 및 기간
- <b> 기간 : 2022-11-14 ~ 2022-12-01 </b> 
- <b> 인원 : 5명(프론트엔드 개발 1명, 백엔드 개발 2명, 인프라 구축 2명) </b>
- <b> 담당 : 프론트엔드 개발 </b>

### 구축환경
```
Upbit api를 활용한 웹 서비스 구축
```
![image](https://user-images.githubusercontent.com/84059211/212466367-1720147a-9b6b-4d1d-a322-02c099b323d9.png)

### Slack을 활용한 생산성 향상
![image](https://user-images.githubusercontent.com/84059211/212466480-f8bffe1d-833f-443b-9917-1df81cf8078a.png)

<br/>

## 인프라
### Solution Architecture
### <b><a href="https://github.com/bbyu2/BTC_edu_final_terraform"> 코인거래소 웹 사이트 ABCbit 3Tier Architecture 구축 Code </a></b>
```
Terraform을 이용한 인프라 자동화 
```
![image](https://user-images.githubusercontent.com/84059211/212466595-97a4bbe5-d361-4e38-ad72-0f0f5cc3e9ec.png)

### Kubernetes
```
namespace를 통한 Kubernetes환경 분리
```
![image](https://user-images.githubusercontent.com/84059211/212466655-d20a7099-78ea-4139-be11-0ce9950462c3.png)

### CI/CD
### <b><a href="https://github.com/bbyu2/BTC_edu_final_CICD"> 코인거래소 웹 사이트 ABCbit CI/CD Code </a></b>
```
Github, Jenkins, ArgoCD를 활용한 Test, Production 파이프라인으로 분리 운영
```
#### TEST 파이프라인
![image](https://user-images.githubusercontent.com/84059211/212466737-475f9f3f-ab44-4284-98a9-7e23d2c7a803.png)

#### Production 파이프라인
![image](https://user-images.githubusercontent.com/84059211/212467001-9bc9fdd6-3215-4fa1-a8a6-b265b46a951e.png)

### 모니터링
```
프로메테우스와 그라파나를 사용한 EKS의 Node 및 Pod 모니터링
```
![image](https://user-images.githubusercontent.com/84059211/212467121-db4aa420-dafa-47c7-9528-c567451be119.png)
```
AWS 리소스 모니터링
```
![image](https://user-images.githubusercontent.com/84059211/212467184-1bd1d661-7365-4478-b80f-ad8f3f4edbfc.png)
```
모니터링 이중화를 위한 쉘 스크립트 작성
```
![image](https://user-images.githubusercontent.com/84059211/212467216-f6e2c7ff-d5fd-4dbe-b769-5091ab08400e.png)

### 로그관리
![image](https://user-images.githubusercontent.com/84059211/212467232-c9a98e2b-a5d7-4760-b8e1-ab8cc45e792f.png)

<br/>

## 코인거래소 ABCbit 웹페이지
### 메인 페이지
```
로그인 및 로그아웃, 거래소, 자동매매 페이지 이동 가능
```
![image](https://user-images.githubusercontent.com/84059211/212468504-1c9226eb-90d3-4d5e-9ca2-ac05900952bb.png)

### 거래소 페이지
```
Upbit API를 활용한 코인 시세 및 리스트 , 변동 차트, 보유 자산, 매수매도 기능
```
![image](https://user-images.githubusercontent.com/84059211/212468665-7e1648ec-e969-4d17-bd20-c537ee22b80d.png)

### 자동 매매
```
비트 코인 자동 매매 서비스 신청 및 중지, 자산 조회, 자동 매매 거래 내역 확인 
매수된 코인은 다음날 오전 9시에 일괄 매도
```
![image](https://user-images.githubusercontent.com/84059211/212468706-bc5e5434-7f51-4b6d-b436-9f3f33e9cc1c.png)
