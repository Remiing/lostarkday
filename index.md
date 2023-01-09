---
layout: default
title: Home
nav_order: 1
description: "Day guild information."
permalink: /
---

<div class="index-wrapper" markdown="1">
![](./assets/images/main.png)


![](./assets/images/Day_logo.png)
</div>

<div markdown="1" style="overflow: auto;">
<div markdown="1" style="box-sizing: border-box; width: 60%; float: left; padding-right: 1rem; border-right: 1px solid #eeebee">

### 템레벨 랭킹
{% assign member_data = site.data.member_chart %}
| {::nomarkdown}<p>닉네임</p><p>클래스</p>{:/} | 아이템 |
|:-|:-|
{% for i in (0..4) -%}
{%- assign member = member_data[i] -%}
|{::nomarkdown}<p>{{member.name-}}</p><p>{{member.class-}}</p>{:/}{{-raw-}}
|{{member.itemLV-}}|
{% endfor %}

<a href="https://remiing.github.io/lostarkday/docs/ranking/" class="more">랭킹 더보기 ></a>
{: .text-right .fs-2 }

### 캐릭터 가치 환산
{% assign capitalization_data = site.data.capitalization %}
| 닉네임 | 아이템 | 총합 |
|:-|:-:|:-:|
{% for i in (0..4) -%}
{%- assign capitalization = capitalization_data[i] -%}
|{{capitalization.name-}}
|{{capitalization.itemLV-}}
|{%- assign total_gold = capitalization.equipTotal | plus: capitalization.accTotal | plus: capitalization.gemTotal -%}
{% include numberWithCommas.html number=total_gold %}|
{% endfor %}

<a href="https://remiing.github.io/lostarkday/docs/capitalization/" class="more">캐릭터 가치 환산 더보기 ></a>
{: .text-right .fs-2 }

</div>


<div markdown="1" style="box-sizing: border-box; width: 40%; float: right; padding-left: 1rem;">

### 강화 재료 가격
{% assign material = site.data.material_price %}
| 재료 | 가격 |
|:-:|:-:|
{% assign row = material | where:"itemName", "정제된 파괴강석" | first %}|{{row.itemName-}}|{{row.itemPrice-}}|
{% assign row = material | where:"itemName", "정제된 수호강석" | first %}|{{row.itemName-}}|{{row.itemPrice-}}|
{% assign row = material | where:"itemName", "찬란한 명예의 돌파석" | first %}|{{row.itemName-}}|{{row.itemPrice-}}|
{% assign row = material | where:"itemName", "최상급 오레하 융화 재료" | first %}|{{row.itemName-}}|{{row.itemPrice-}}|
{% assign row = material | where:"itemName", "명예의 파편 주머니(소)" | first %}|{{row.itemName-}}|{{row.itemPrice-}}|
{% assign row = material | where:"itemName", "명예의 파편 주머니(중)" | first %}|{{row.itemName-}}|{{row.itemPrice-}}|
{% assign row = material | where:"itemName", "명예의 파편 주머니(대)" | first %}|{{row.itemName-}}|{{row.itemPrice-}}|
{% assign row = material | where:"itemName", "9멸" | first %}|{{row.itemName-}}|{{row.itemPrice-}}|
{% assign row = material | where:"itemName", "9홍" | first %}|{{row.itemName-}}|{{row.itemPrice-}}|
{% assign row = material | where:"itemName", "10멸" | first %}|{{row.itemName-}}|{{row.itemPrice-}}|
{% assign row = material | where:"itemName", "10홍" | first %}|{{row.itemName-}}|{{row.itemPrice-}}|

</div>


</div>


증가량 Top 5

