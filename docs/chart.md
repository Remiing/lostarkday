---
layout: default
title: chart
nav_order: 2
---

# Chart

Day guild members chart

| 닉네임 | 클래스 | 아이템 | 원정대 |
|:-------|:---|:-----|:------|
{% for member in site.data.memberlist -%}
|{{member.name-}}
|{{member.class-}}
|{{member.itemLV-}}
|{{member.expeditionLV}}|
{% endfor %}

# Chart

Day guild members chart

| 닉네임 | 클래스 | 아이템 | 원정대 | 각인 | 특성 | 카드 | 보석 | 무기 | 공격력 | 체력 |
|:-------|:---|:-----|:------|:------|:------|:------|:------|:------|:------|:------|
{% for member in site.data.memberlist -%}
|{{member.name-}}|{{member.class-}}|{{member.itemLV-}}|{{member.expeditionLV-}}
|{::nomarkdown}<p>{{member.engraving_simple-}}</p><div class="detail">
    {%- assign engraving_detail = member.engraving_detail | split: ',' -%}
    {%- for engraving in engraving_detail -%}
    <p>{{-engraving-}}</p>
    {%- endfor -%}</div>{:/}|
{{-member.stat | split: ','-}}
|{{member.card-}}
|{{member.gem_simple | split: ','-}}
|{{member.equipmentLV | split: ' ' | first-}}
|{{member.power-}}
|{{member.vitality-}}|
{% endfor %}
