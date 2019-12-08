2019-2-OSS-L8
=================

# HOMEPAGE
https://19-2-skku-oss.github.io/2019-2-OSS-L8-page/

## 1. 팀원 소개
- **정상우** (미디어커뮤니케이션학과, 4학년, 팀장, sangwoojung)
- **박민주** (수학과, 4학년, 팀원, wyuinche)
- **방선웅** (소프트웨어학과, 1학년, 팀원, sunwoongskku) 
- **안상현** (소프트웨어학과, 1학년, 팀원, Ahnsanghyun-hi)
- **홍민기** (시스템경영학과, 3학년, 팀원, tenlif)

## 2. 프로젝트 소개 & 실행 예시 
- **Hangul.js** (https://github.com/e-/Hangul.js)

> Hangul.js는 한글로 이루어진 문장의 자음과 모음을 분리하는 자바스크립트 라이브러리입니다. 자모 분리 또는 초성 검색에 사용할 수 있습니다.
> Hangul.assemble (alias `Hangul.a`)

`Hangul.assemble(arr:string[])`는 한글 자음/모음들의 배열 `arr`을 인자로 받아 이를 조합한 문자열을 돌려줍니다. 이 때 한글이 아닌 문자는 그대로 반환됩니다. `Hangul.a`처럼 짧은 이름으로 사용할 수도 있습니다.

```js
Hangul.assemble(['ㄱ','ㅏ','ㄴ','ㅏ','ㄷ','ㅏ']); // '가나다'

Hangul.assemble(['a','b','ㄱ','ㅏ','c']); // 'ab가c'

Hangul.assemble(['a','b','@','!','2','3','X','.']); // 'ab@123X.'
```

이 경우에도 두벌식 키보드에서 주어진 키들을 누를 때 만들어지는 문자열을 돌려준다고 생각하면 쉽습니다.

```js
Hangul.assemble(['ㅗ','ㅐ']); // 'ㅙ'

Hangul.assemble(['ㄹ','ㅂ','ㅅ']); // 'ㄼㅅ'
```

`Hangul.disassemble` 함수와 역함수 관계가 아님에 주의하세요.

```js
Hangul.a(Hangul.d('옽ㅏ')); // '오타' ('옽ㅏ' 가 아님)
```
- **Free Python Games** (https://github.com/grantjenks/free-python-games)

> Free Python Games는 파이썬 무료 게임 프로젝트입니다. 교육과 재미를 위해 만들어진 단순 게임들이 대부분이며, 고전 게임들로 이루어져있습니다.

*게임 예시*

-**Snake**                   -**Paint** 

<img src="https://camo.githubusercontent.com/b189b47e1146da6f14f72b1d5d16ad5185ad072e/687474703a2f2f7777772e6772616e746a656e6b732e636f6d2f646f63732f6672656567616d65732f5f7374617469632f736e616b652e676966" width="200" height="200"> 
<img src="http://www.grantjenks.com/docs/freegames/_static/paint.gif" width="200" height="200"> 

-**Pacman**                  -**Flappy**

<img src="http://www.grantjenks.com/docs/freegames/_static/pacman.gif" width="200" height="200">
<img src="http://www.grantjenks.com/docs/freegames/_static/flappy.gif" width="200" height="200">


## 3. 프로젝트 기여 방식

- **Hangul.js**
    * 소스코드의 주석을 수정/추가합니다.
    * 테스트 페이지의 디자인을 수정합니다.
- **Free Python Games**
    * Snake 게임의 기능들을 추가합니다.
    * Baseball 게임을 새로 만든 후 추가합니다.
    * Memory 게임의 오류를 수정하고 기능들을 추가합니다.
