# CodingTest-Study
<div align="center">
  <h1>🖥Algorithm-Study🖥</h1>
</div>
<br/>

- [Member](#Member)
- [Rule](#Rule)
- [Record](#Record)

---

## Member   
| <img src='https://i.namu.wiki/i/AzBBoyawsmnw6ZS_rUo6a6fgvCRwrd6wuaecq6O3hGTuYdFz6NRB_k32VXgmOseF5ihOQ2xI2LWn43ZTZYQ7lw.webp' width='120px' height='120px' alt='avatar'/><br/><b>[윤영서](https://github.com/sdfjkj)</b> |  <img src='https://i.namu.wiki/i/AzBBoyawsmnw6ZS_rUo6a6fgvCRwrd6wuaecq6O3hGTuYdFz6NRB_k32VXgmOseF5ihOQ2xI2LWn43ZTZYQ7lw.webp' width='120px' height='120px' alt='avatar'/><br/><b>[이주원](https://github.com/duoni-o)</b>  |  <img src='https://github.com/sdfjkj/CodingTest-Study/assets/95211829/330197f6-99ce-429f-8fcf-658343bd8aa5' width='120px' height='120px' alt='avatar'/><br/><b>[김정환](https://github.com/sdfjkj)</b>  | 
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | 

---

## Rule


### 협업방법(Upstream)

- 협업 시작하기   
  - Fork뜨기    
  - (터미널)git clone [복사한 url 붙여넣기(본인계정 url)]   
  - upstream 설정 : git remote add upstream https://github.com/sdfjkj/Python-CodingTest-Study.git
  - (참고*) fork한 본인의 repository([본인계정]/Python-CodingTest-Study)는 origin, 원본 repository(sdfjkjPython-CodingTest-Study)는 upstream이라고 한다.      
<br>

- branch 파서 작업하기   
  - 브랜치 생성 : (터미널) git branch [브랜치 이름]   
  - 프랜치 이동 : git checkout [생성한 브랜치 이름]   
  - (참고*) 브랜치 이름은 아무거나 상관없음(예시. develop, KTY, 등등)   
<br>

- 작업 후 push 하기   
   - 작업 내용 저장 : (터미널)git add .   
   - 작업 commit 이름(위 Naming규칙에 따라 작성할 것) : (터미널)git commit -m "commit이름"   
   - 작업 push : (터미널)git push origin [작업 브랜치 이름]   
   - 레포지토리 들어와서 Compare & pull request 라는 초록색 버튼 클릭 -> Create pull request눌러 등록 완료   
<br>

- 최신상태로 업데이트
   - git pull upstream main   
   (또는)
   - git fetch upstream main   
   - git merge upstream main   
---
