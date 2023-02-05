---
layout: default
title: Home
nav_order: 1
description: "Day guild information."
permalink: /
---

<div class="index-wrapper" markdown="1">
![](./assets/images/2023 HAPPY NEW YEAR.jpg)


![](./assets/images/Day_logo.png)
</div>

<div markdown="1" style="overflow: auto;">
<div class="index-left" markdown="1">

### 템레벨 랭킹
{% assign member_data = site.data.member_chart %}

| # | 닉네임 | 아이템 레벨 |
|:-:|:-|:-|
{% assign ranking = 1 -%}
{% for i in (0..4) -%}
{%- assign member = member_data[i] -%}
|{{ranking}}{%- assign ranking = ranking | plus: 1 -%}
|{{member.name-}}
|{{member.itemLV-}}|
{% endfor %}


<a href="{{ '/docs/ranking/' | relative_url }}" class="more">랭킹 더보기 ></a>
{: .text-right .fs-2 }


### 주간 템레벨 변화
{% assign member_list = site.data.guild_members.main_character | concat: site.data.guild_members.sub_character %}
{% assign before_data = site.data.update_time[-8].filename | remove: ".csv" %}
{% assign after_data = site.data.update_time[-1].filename | remove: ".csv" %}
{% assign before_data = site.data.chart[before_data] %}
{% assign after_data = site.data.chart[after_data] %}

| # | 닉네임 | 아이템 레벨 변화 |
|:-:|:-|:-:|
{% assign ranking = 1 -%}
{% for member in member_list %}
  {%- assign before = before_data | where:"name", member | first -%}
  {%- assign after = after_data | where:"name", member | first -%}
  {%- unless before and after -%}{%- continue -%}{%- endunless -%}
  {%- if before.itemLV == after.itemLV -%}{%- continue -%}{%- else -%}{%- assign empty_check = 1 -%}{%- endif -%}
  |{{ranking}}{%- assign ranking = ranking | plus: 1 -%}
  |{{after.name-}}
  |{{before.itemLV}} > {{after.itemLV-}}|
{% endfor %}


<a href="{{ '/docs/chart/weekly_chart/' | relative_url }}" class="more">주간 템레벨 변화 더보기 ></a>
{: .text-right .fs-2 }


### 캐릭터 가치 환산
{% assign capitalization_data = site.data.capitalization %}

| # | 닉네임 | 가치 |
|:-:|:-|:-:|
{% assign ranking = 1 -%}
{% for i in (0..4) -%}
{%- assign capitalization = capitalization_data[i] -%}
|{{ranking}}{%- assign ranking = ranking | plus: 1 -%}
|{{capitalization.name-}}
|{%- assign total_gold = capitalization.equipTotal | plus: capitalization.accTotal | plus: capitalization.gemTotal -%}
{% include numberWithCommas.html number=total_gold %}|
{% endfor %}


<a href="{{ '/docs/capitalization/' | relative_url }}" class="more">캐릭터 가치 환산 더보기 ></a>
{: .text-right .fs-2 }

</div>


<div class="index-right" markdown="1">

### 강화 재료 가격
{% assign material = site.data.material_price | last %}

| 재료 | 가격 |
|:-:|:-:|
|정제된 파괴강석|{{material["정제된 파괴강석"]}}|
|정제된 수호강석|{{material["정제된 수호강석"]}}|
|찬란한 명예의 돌파석|{{material["찬란한 명예의 돌파석"]}}|
|최상급 오레하 융화 재료|{{material["최상급 오레하 융화 재료"]}}|
|명예의 파편 주머니(소)|{{material["명예의 파편 주머니(소)"]}}|
|명예의 파편 주머니(중)|{{material["명예의 파편 주머니(중)"]}}|
|명예의 파편 주머니(대)|{{material["명예의 파편 주머니(대)"]}}|
|7멸|{{material["7멸"]}}|
|7홍|{{material["7홍"]}}|
|9멸|{{material["9멸"]}}|
|9홍|{{material["9홍"]}}|
|10멸|{{material["10멸"]}}|
|10홍|{{material["10홍"]}}|


</div>


</div>


