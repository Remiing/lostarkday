---
layout: default
title: chart
nav_order: 2
---

{% for item in site.data %}
{{item[0]}}
{% endfor %}

# Chart

Day guild members chart

| 닉네임 | 클래스 | 아이템 | 원정대 | 각인 | 특성 | 카드 | 보석 | 무기 | 공격력 | 체력 |
|:---|:---|:-:|:-:|:-:|:---|:-|:-|:-:|:-:|:-:|
{% for member in site.data.first[1] -%}
|{{member.name-}}
|{{member.class-}}
|{{member.itemLV-}}
|{{member.expeditionLV-}}
|{::nomarkdown}<p>{{member.engraving_simple-}}</p><div class="detail">
{%- assign engraving_detail = member.engraving_detail | split: ',' -%}
{%- for engraving in engraving_detail -%}
<p>{{-engraving-}}</p>
{%- endfor -%}</div>{:/}{{-raw-}}
|{%- assign stats = member.stat | split: ',' -%}
{%- for stat in stats -%}
{::nomarkdown}<p>{{-stat-}}</p>{:/}
{%- endfor -%}{{-raw-}}
|{{member.card-}}
|{%- assign gems = member.gem_simple | split: ',' -%}
{%- for gem in gems -%}
{::nomarkdown}<p>{{-gem-}}</p>{:/}
{%- endfor -%}{{-raw-}}
|{{member.equipmentLV | split: ' ' | first-}}
|{{member.power-}}
|{{member.vitality-}}|
{% endfor %}
