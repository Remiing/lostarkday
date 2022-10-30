---
layout: default
title: chart
nav_order: 2
---

# Chart

Day guild members chart

| 닉네임 | 클래스 | 아이템 | 전투 | 원정대 | 각인 | 특성 | 카드 | 보석 | 무기 | 공격력 | 체력 |
|:-------|:---|:-----|:----|:------|:------|:------|:------|:------|:------|:------|:------|
{%- for member in site.data.memberlist %}
|{{member.name-}}
|{{member.class-}}
|{{member.itemLV-}}
|{{member.battleLV-}}
|{{member.expeditionLV-}}
|{{member.engraving_simple-}}
<div class="detail" markdown="1">
{%- for engraving in member.engraving_detail | split: ',' -%}
{{-engraving-}}
{%- endfor -%}</div>
|{{member.stat | split: ','-}}
|{{member.card-}}
|{{member.gem_simple | split: ','-}}
|{{member.equipmentLV | split: ' ' | first-}}
|{{member.power-}}
|{{member.vitality-}}|
{%- endfor %}
