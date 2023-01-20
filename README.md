# ABCbit 코인 거래소 및 자동매매 서비스 구축

## Repository
```
프로젝트 관리를 위한 개발(현 레포지토리) 및 인프라, CI/CD 레포지토리 분리 사용
```
### Terraform을 이용한 인프라 자동화
### <b><a href="https://github.com/bbyu2/BTC_edu_final_terraform"> - 코인거래소 웹 사이트 ABCbit 3Tier Architecture 구축 </a></b>
### Jenkins, ArgoCD를 활용한 CI/CD 자동화
### <b><a href="https://github.com/bbyu2/BTC_edu_final_CICD"> - 코인거래소 웹 사이트 ABCbit CI/CD </a></b>

<br/><br/>

## 개요
#### AWS 서비스를 바탕으로 CI/CD(지속적 통합/배포)를 구현한 DevOps 프로젝트
#### Terraform 코드를 통한 인프라 구축 및 python을 기반으로 Django 프레임워크로 개발 진행
#### EKS(Elastic Kubernetes Service)사용한 MSA(Micro Service Architecture)구축, 기능별 Pod 분리 운영

<br/>

### 요구사항
```
코인 거래 서비스 개발, 무중단 서비스 운영 및 모니터링, 로그 관리를 바탕으로 프로젝트 진행 
```
![image](https://user-images.githubusercontent.com/84059211/212466540-9981747e-95fa-4e86-89f2-0c607060f703.png)

<br/>

### 구축 인원 및 기간
#### - 기간 : 2022-11-14 ~ 2022-12-14 (총 4주) </b> 
#### - 인원 : 5명 (프론트엔드 개발 1명, 백엔드 개발 2명, 인프라 구축 2명) </b>

<br/>

### 구축환경
```
1. Git, Slack Notion 등을 이용한 협업 
2. Django 프레임워크를 바탕으로 python, javascript, html, css를 사용하여 웹 페이지 구축
3. AWS 서비스를 바탕으로 Terraform, Docker, K8S를 이용한 MSA구축
4. 코인거래 서비스를 위한 Upbit api 및 그래프CanvasJS를 활용한  개발 및 반응형 웹페이지를 위한 Bootstrap이용
```
![image](https://user-images.githubusercontent.com/84059211/212466367-1720147a-9b6b-4d1d-a322-02c099b323d9.png)

<br/>

### Slack을 활용한 생산성 향상
```
python을 통한 슬랙 챗봇을 개발하여, 프로젝트시 관련 자료를 편하게 찾을 수 있도록 함
```
![image](https://user-images.githubusercontent.com/84059211/212466480-f8bffe1d-833f-443b-9917-1df81cf8078a.png)

<br/>

### 담당 역할
- FrontEnd 개발과 발표 자료 생성, 최종 발표 진행을 메인으로 담당 
- Backend 및 Infra팀에서 참고할 코드 및 자료를 함께 찾아 테스트하는 등 보조 역할 진행

<br/><br/>

## 코인거래소 ABCbit 웹페이지
### 메인 페이지
```
로그인 및 로그아웃, 거래소, 자동매매 페이지 이동 가능
```
![image](https://user-images.githubusercontent.com/84059211/212468504-1c9226eb-90d3-4d5e-9ca2-ac05900952bb.png)

<br/>

### 반응형 디자인
```
프로젝트 발표 시 홈페이지 접속 QR코드를 제공함으로써, 모바일 접속자를 위한 반응형 웹 페이지 구현
```
![image](https://user-images.githubusercontent.com/84059211/212819414-2216ee05-7dd4-4275-8240-9dff18d6bfcb.png)

<br/>

### 거래소 페이지
```
Upbit API를 활용한 코인 시세 및 리스트 , 변동 차트, 보유 자산, 매수매도 기능
```
![image](https://user-images.githubusercontent.com/84059211/212468665-7e1648ec-e969-4d17-bd20-c537ee22b80d.png)

<br/>

### 자동 매매  페이지
```
비트 코인 자동 매매 서비스 신청 및 중지, 자산 조회, 자동 매매 거래 내역 확인 
매수된 코인은 다음날 오전 9시에 일괄 매도
```
![image](https://user-images.githubusercontent.com/84059211/212468706-bc5e5434-7f51-4b6d-b436-9f3f33e9cc1c.png)

<br/><br/><br/>
***

<div align=center>
<h4> 👈 back to main 👈 </h4>
<a href="https://github.com/bbyu2"> 
<img src="https://img.shields.io/endpoint?label=bbyu2&logo=github&style=for-the-badge&url=https%3A%2F%2Fgithub.com%2Fbbyu2%2F"/>
</a>
</div>
