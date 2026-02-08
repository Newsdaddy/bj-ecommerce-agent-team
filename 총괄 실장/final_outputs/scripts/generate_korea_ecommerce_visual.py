#!/usr/bin/env python3
"""
Korea eCommerce Market Visual Aid Generator - 2025 Edition
검은 배경 + 네온 컬러 스타일의 데이터 그래프 생성
"""

import matplotlib.pyplot as plt
import numpy as np

# 스타일 설정
plt.style.use('dark_background')

# 2025 데이터 (출처: TMO Group, PCMI, K-Biz Insights)
data = {
    'labels': ['Online Share\nof Retail', 'Mobile\nCommerce', 'Social\nDiscovery', 'Coupang+Naver\nMarket Share'],
    'values': [40, 75, 70, 65],
    'colors': ['#00D4FF', '#4ECDC4', '#FF6B6B', '#FFE66D']
}

# 그래프 생성 - 높이를 늘려서 하단 여백 확보
fig, ax = plt.subplots(figsize=(12, 8), facecolor='#0a0a0a')
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

# 제목
ax.set_title('South Korea eCommerce: Key Metrics 2025',
             fontsize=24, fontweight='bold', color='white', pad=20)

# Y축 설정
ax.set_ylim(0, 100)
ax.set_ylabel('Percentage (%)', fontsize=14, color='#888888')
ax.tick_params(axis='y', colors='#888888', labelsize=12)
ax.tick_params(axis='x', colors='white', labelsize=12, pad=8)

# 그리드
ax.yaxis.grid(True, linestyle='--', alpha=0.3, color='#444444')
ax.set_axisbelow(True)

# 스파인 제거
for spine in ax.spines.values():
    spine.set_visible(False)

# 하단 여백 충분히 확보
plt.subplots_adjust(bottom=0.18)

# 출처 및 마켓 사이즈 - figure 좌표계 사용, 오버랩 방지
fig.text(0.5, 0.03, 'Market Size: $160B+ | Rocket WOW: 14M+ subscribers',
         ha='center', va='bottom', fontsize=11, color='#888888')
fig.text(0.5, 0.008, 'Source: TMO Group, PCMI, K-Biz Insights (2025)',
         ha='center', va='bottom', fontsize=9, color='#555555')

# 저장
import os
output_path = '/Users/bj/Documents/ASC/에이전트 트랙/BJ 이커머스 사단/총괄 실장/final_outputs/visuals/visual_20260129_korea_ecommerce_bar.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, dpi=150, facecolor='#0a0a0a', edgecolor='none',
            bbox_inches='tight', pad_inches=0.2)
plt.close()

print(f"✅ Visual saved to: {output_path}")
