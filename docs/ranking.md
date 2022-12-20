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

Last Update {{site.data.update_time[-1].update_time}}
{: .text-right }

{% assign last_data = site.data.update_time[-1].filename | remove: ".csv" %}
{% assign members_data = site.data.chart[last_data] %}

| {::nomarkdown}<p>닉네임</p><p>클래스</p>{:/} | 아이템 | 원정대 | 각인 | 특성 | 카드 | 보석 | 무기 | 공격력 | 체력 |
|:-|:-:|:-:|:-:|:-|:-|:-|:-:|:-:|:-:|
{% for member in members_data -%}
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
|{%- assign weapon = member.equipment | split: '/' -%}
{::nomarkdown}<p>{{weapon[1]-}}</p><div class="detail">
{%- assign equip = member.equipment | split: ',' -%}
{%- assign equipName = member.equipment_name | split: ',' -%}
{%- for i in (0..5) -%}
{%- assign equipDetail = equip[i] | split: '/' -%}
<p>{{equipDetail[1]}} {{equipName[i]}} {{equipDetail[3]}}</p>
{%- endfor -%}</div>{:/}{{-raw-}}
|{{member.power-}}
|{{member.vitality-}}|
{% endfor %}
