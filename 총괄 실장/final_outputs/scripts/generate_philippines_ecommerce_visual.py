#!/usr/bin/env python3
"""
Philippines eCommerce Market Visual Aid Generator - 2025 Edition
검은 배경 + 네온 컬러 스타일의 데이터 그래프 생성
Asia's Fastest Growing eCommerce Market
"""

import matplotlib.pyplot as plt
import numpy as np

# 스타일 설정
plt.style.use('dark_background')

# 2025 데이터 (출처: Mordor Intelligence, k+ collective, Archive Market Research)
data = {
    'labels': ['Growth\nRate', 'Mobile\nCommerce', 'Internet\nPenetration', 'Smartphone\nPenetration'],
    'values': [24.1, 79, 83.8, 73.7],
    'colors': ['#FF6B6B', '#00D4FF', '#4ECDC4', '#FFE66D']
}

# 그래프 생성 - 충분한 높이로 하단 여백 확보
fig, ax = plt.subplots(figsize=(12, 9), facecolor='#0a0a0a')
ax.set_facecolor('#0a0a0a')

# 바 그래프
bars = ax.bar(data['labels'], data['values'], color=data['colors'],
              edgecolor='white', linewidth=0.5, width=0.6)

# 값 레이블 추가
for bar, value in zip(bars, data['values']):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 2,
            f'{value}%',
            ha='center', va='bottom',
            fontsize=20, fontweight='bold', color='white')

# 제목 - Growth Rate 강조
ax.set_title('Philippines: Asia\'s Fastest Growing eCommerce Market 2025',
             fontsize=22, fontweight='bold', color='white', pad=25)

# 부제목 - 달러 기호 대신 USD 표기
ax.text(0.5, 1.02, 'USD 17.65B Market  →  USD 33.65B by 2030',
        ha='center', va='bottom', transform=ax.transAxes,
        fontsize=14, color='#00D4FF', style='italic')

# Y축 설정
ax.set_ylim(0, 100)
ax.set_ylabel('Percentage (%)', fontsize=14, color='#888888')
ax.tick_params(axis='y', colors='#888888', labelsize=12)
ax.tick_params(axis='x', colors='white', labelsize=11, pad=10)

# 그리드
ax.yaxis.grid(True, linestyle='--', alpha=0.3, color='#444444')
ax.set_axisbelow(True)

# 스파인 제거
for spine in ax.spines.values():
    spine.set_visible(False)

# 하단 여백 충분히 확보 (오버랩 방지)
plt.subplots_adjust(bottom=0.20, top=0.88)

# 주요 하이라이트 - figure 좌표계 사용
fig.text(0.5, 0.06, 'Shopee: 70M+ visitors | GCash: 94M users | TikTok Shop: #2 App',
         ha='center', va='bottom', fontsize=11, color='#888888')

# 출처 - 가장 하단에 배치
fig.text(0.5, 0.015, 'Source: Mordor Intelligence, k+ collective, Archive Market Research (2025)',
         ha='center', va='bottom', fontsize=9, color='#555555')

# 저장
import os
output_path = '/Users/bj/Documents/ASC/에이전트 트랙/BJ 이커머스 사단/총괄 실장/final_outputs/visuals/visual_20260129_philippines_ecommerce_bar.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=150, facecolor='#0a0a0a', edgecolor='none',
            bbox_inches='tight', pad_inches=0.3)
plt.close()

print(f"✅ Visual saved to: {output_path}")
