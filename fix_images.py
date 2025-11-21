#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修复所有HTML文件中的图片URL
将 source.unsplash.com 替换为稳定的 images.unsplash.com 图片URL
"""

import re
import os
import glob

# 图片映射：根据关键词映射到具体的Unsplash图片ID
IMAGE_MAPPING = {
    # 中国风景、山脉
    'china,landscape,mountains': 'photo-1508804185872-d7badad00f7d',
    'china,nature,travel': 'photo-1501594907352-04cda38ebc29',
    
    # 西藏、高原
    'tibet,plateau,highland': 'photo-1544966503-7cc5ac882d5f',
    'tibet,plateau,mountains': 'photo-1544966503-7cc5ac882d5f',
    'tibet,potala,palace': 'photo-1544966503-7cc5ac882d5f',
    
    # 云南、茶
    'yunnan,tea,mountains': 'photo-1506905925346-21bda4d32df4',
    'tea,yunnan,ancient,road': 'photo-1556679343-c7306c1976bc',
    'tea,yunnan,china': 'photo-1556679343-c7306c1976bc',
    
    # 团队、旅行
    'travel,team,adventure': 'photo-1529156069898-49953e39b3ac',
    
    # 文化、传统
    'chinese,culture,traditional': 'photo-1508804185872-d7badad00f7d',
    
    # 健康、冥想
    'meditation,wellness,nature': 'photo-1506126613408-eca07ce68773',
    
    # 冒险、户外
    'adventure,outdoor,expedition': 'photo-1464822759023-fed622ff2c3b',
    'adventure,sports,outdoor': 'photo-1464822759023-fed622ff2c3b',
    
    # 自然、森林
    'nature,forest,landscape': 'photo-1506905925346-21bda4d32df4',
    
    # 可持续、环保
    'sustainable,eco,green': 'photo-1441974231531-c6227db76b6e',
    'sustainable,eco,green,nature': 'photo-1441974231531-c6227db76b6e',
    
    # 北京、城市
    'beijing,forbidden,city': 'photo-1508804185872-d7badad00f7d',
    'beijing,shanghai,city': 'photo-1508804185872-d7badad00f7d',
    
    # 旅行、冒险
    'travel,adventure,china': 'photo-1501594907352-04cda38ebc29',
    'travel,group,adventure': 'photo-1529156069898-49953e39b3ac',
    
    # 定制旅行
    'custom,travel,personalized': 'photo-1501594907352-04cda38ebc29',
    
    # 新疆、丝绸之路
    'xinjiang,desert,silk,road': 'photo-1501594907352-04cda38ebc29',
    'silk,road,desert,xinjiang': 'photo-1501594907352-04cda38ebc29',
    
    # 贵州
    'guizhou,ethnic,culture,minority': 'photo-1508804185872-d7badad00f7d',
    'guizhou,terrace,ethnic': 'photo-1508804185872-d7badad00f7d',
    
    # 四川
    'sichuan,food,cuisine,spicy': 'photo-1556679343-c7306c1976bc',
    'sichuan,panda,nature': 'photo-1506905925346-21bda4d32df4',
    
    # 云南指南
    'yunnan,lijiang,dali': 'photo-1506905925346-21bda4d32df4',
}

def fix_image_url(match):
    """修复单个图片URL"""
    full_url = match.group(0)
    
    # 提取尺寸和关键词
    size_match = re.search(r'/(\d+)x(\d+)/\?([^"\')\s]+)', full_url)
    if not size_match:
        # 处理已损坏的URL格式
        if 'source.unsplash.com-' in full_url:
            # 提取尺寸
            size_match2 = re.search(r'w=(\d+)&h=(\d+)', full_url)
            if size_match2:
                width = size_match2.group(1)
                height = size_match2.group(2)
                # 使用默认图片
                photo_id = 'photo-1508804185872-d7badad00f7d'
                return f'https://images.unsplash.com/{photo_id}?w={width}&h={height}&fit=crop'
        return full_url
    
    width = size_match.group(1)
    height = size_match.group(2)
    keywords = size_match.group(3)
    
    # 查找对应的图片ID
    photo_id = IMAGE_MAPPING.get(keywords, 'photo-1508804185872-d7badad00f7d')
    
    return f'https://images.unsplash.com/{photo_id}?w={width}&h={height}&fit=crop'

def fix_file(filepath):
    """修复单个文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 匹配所有 source.unsplash.com URL
        pattern = r'https://source\.unsplash\.com[^"\'\s)]+'
        new_content = re.sub(pattern, fix_image_url, content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'✅ 已修复: {filepath}')
            return True
        else:
            print(f'⏭️  无需修复: {filepath}')
            return False
    except Exception as e:
        print(f'❌ 错误 {filepath}: {e}')
        return False

def main():
    """主函数"""
    html_files = glob.glob('*.html')
    fixed_count = 0
    
    print(f'找到 {len(html_files)} 个HTML文件\n')
    
    for filepath in html_files:
        if fix_file(filepath):
            fixed_count += 1
    
    print(f'\n完成！共修复 {fixed_count} 个文件')

if __name__ == '__main__':
    main()

