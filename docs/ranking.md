---
layout: default
title: Ranking
nav_order: 2
---

# Ranking
{: .fs-9 }

Day guild members ranking
{: .fs-6 .fw-300 }

---

| {::nomarkdown}<p>닉네임</p><p>클래스</p>{:/} | 아이템 | 원정대 | 각인 | 특성 | 카드 | 보석 | 무기 | 공격력 | 체력 |
|:-|:-:|:-:|:-:|:-|:-|:-|:-:|:-:|:-:|
{% for member in site.data.member_chart -%}
|{::nomarkdown}<p>{{member.name-}}</p><p>{{member.class-}}</p>{:/}{{-raw-}}
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
|{% assign card_data = member.card | split: ',' -%}
{%- for card in card_data -%}
{::nomarkdown}<p>{{-card -}}</p>{:/}
{%- endfor -%}{{-raw-}}
|{%- assign gems = member.gem_simple | split: ',' -%}
{%- for gem in gems -%}
{::nomarkdown}<p>{{-gem-}}</p>{:/}
{%- endfor -%}{{-raw-}}
|{::nomarkdown}<p>{{member.equipmentLV | split: ' ' | first-}}</p><div class="detail">
{%- assign equipmentLV = member.equipmentLV | split: ',' -%}
{%- for equipment in equipmentLV -%}
<p>{{-equipment-}}</p>
{%- endfor -%}</div>{:/}{{-raw-}}
|{{member.power-}}
|{{member.vitality-}}|
{% endfor %}