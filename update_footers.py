#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新所有HTML页面的页脚格式，使其与index.html一致
"""

import os
import re
from pathlib import Path

# 标准页脚模板（与index.html一致）
STANDARD_FOOTER = '''    <footer class="bg-dark text-white pt-16 pb-12">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-12">
                <div class="lg:col-span-2 space-y-6">
                    <div class="flex items-center">
                        <a href="index.html" class="flex items-center">
                            <span class="bg-white p-2 rounded-lg">
                                <img src="图片1.png" alt="Journey Weaver Logo" class="h-10 sm:h-12 w-auto object-contain" loading="lazy">
                            </span>
                            <span class="ml-3 text-xl font-bold text-white">Journey Weaver</span>
                        </a>
                    </div>
                    <p class="text-gray-600 leading-relaxed">
                        Weave Journeys, Cherish Memories. Specializing in emotionally-driven, sustainable travel experiences across China.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-secondary transition-colors duration-300">
                            <i class="fa fa-facebook text-white"></i>
                        </a>
                        <a href="#" class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-secondary transition-colors duration-300">
                            <i class="fa fa-instagram text-white"></i>
                        </a>
                        <a href="#" class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-secondary transition-colors duration-300">
                            <i class="fa fa-twitter text-white"></i>
                        </a>
                        <a href="#" class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-secondary transition-colors duration-300">
                            <i class="fa fa-wechat text-white"></i>
                        </a>
                        <a href="#" class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-secondary transition-colors duration-300">
                            <i class="fa fa-linkedin text-white"></i>
                        </a>
                    </div>
                </div>
                
                <div>
                    <h4 class="text-lg font-semibold text-white mb-6">Quick Links</h4>
                    <ul class="space-y-3">
                        <li><a href="index.html#about" class="text-gray-400 hover:text-secondary transition-colors duration-300">About Us</a></li>
                        <li><a href="all-journeys.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">All Journeys</a></li>
                        <li><a href="why-us.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Why Choose Us</a></li>
                        <li><a href="travelogue.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Travelogue</a></li>
                        <li><a href="index.html#team" class="text-gray-400 hover:text-secondary transition-colors duration-300">Our Team</a></li>
                        <li><a href="faq.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">FAQ</a></li>
                        <li><a href="index.html#partnerships" class="text-gray-400 hover:text-secondary transition-colors duration-300">Partnerships</a></li>
                        <li><a href="contact.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Contact Us</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-lg font-semibold text-white mb-6">Our Services</h4>
                    <ul class="space-y-3">
                        <li><a href="cultural-experiences.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Cultural Immersion</a></li>
                        <li><a href="adventure-travel.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Nature Exploration</a></li>
                        <li><a href="custom-journeys.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Health & Wellness</a></li>
                        <li><a href="adventure-travel.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Adventure Tourism</a></li>
                        <li><a href="adventure-travel.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Western Expeditions</a></li>
                        <li><a href="sustainable-tourism.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Carbon-Neutral Travel</a></li>
                        <li><a href="small-group-journeys.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Small Group Tours</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="text-lg font-semibold text-white mb-6">Contact Us</h4>
                    <ul class="space-y-4">
                        <li class="flex items-start gap-3">
                            <i class="fa fa-map-marker text-secondary mt-1 flex-shrink-0"></i>
                            <span class="text-gray-400">
                                <strong class="text-white">Shanghai (HQ)</strong><br>
                                No. 1234, Huaihai Middle Road, Xuhui District, 200031
                            </span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fa fa-map-marker text-secondary mt-1 flex-shrink-0"></i>
                            <span class="text-gray-400">
                                <strong class="text-white">Beijing</strong><br>
                                10F, Oriental Plaza, Dongcheng District, 100006
                            </span>
                        </li>
                         <li class="flex items-start gap-3">
                            <i class="fa fa-map-marker text-secondary mt-1 flex-shrink-0"></i>
                            <span class="text-gray-400">
                                <strong class="text-white">Chengdu</strong><br>
                                26F, Hangkong Road, Wuhou District, 610041
                            </span>
                        </li>
                        <li class="flex items-center gap-3">
                            <i class="fa fa-phone text-secondary flex-shrink-0"></i>
                            <a href="tel:+8602164227654" class="text-gray-400 hover:text-secondary transition-colors duration-300">+86 021-64227654</a>
                        </li>
                        <li class="flex items-center gap-3">
                            <i class="fa fa-envelope text-secondary flex-shrink-0"></i>
                            <a href="mailto:service@journeyweaver-sh.com" class="text-gray-400 hover:text-secondary transition-colors duration-300">service@journeyweaver-sh.com</a>
                        </li>
                    </ul>
                </div>
            </div>
            
            <div class="border-t border-white/10 my-10"></div>
            
            <div class="flex flex-col md:flex-row justify-between items-center gap-6">
                <p class="text-gray-400 text-center md:text-left text-sm">
                    © 2025 Shanghai Journey Weaving Travel Agency Co., Ltd. All rights reserved.
                </p>
                <div class="flex gap-6 text-sm">
                    <a href="privacy-policy.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Privacy Policy</a>
                    <a href="terms-of-service.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Terms of Service</a>
                    <a href="cookie-policy.html" class="text-gray-400 hover:text-secondary transition-colors duration-300">Cookie Policy</a>
                </div>
            </div>
        </div>
    </footer>'''

def update_footer_in_file(file_path):
    """更新单个文件的页脚"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 使用正则表达式匹配footer标签及其内容（包括结束标签）
        # 匹配从<footer开始到</footer>结束的所有内容
        footer_pattern = r'<footer[^>]*>.*?</footer>'
        
        if re.search(footer_pattern, content, re.DOTALL):
            # 替换页脚
            new_content = re.sub(footer_pattern, STANDARD_FOOTER, content, flags=re.DOTALL)
            
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """主函数"""
    # 获取当前目录
    base_dir = Path(__file__).parent
    
    # 要排除的文件
    exclude_files = {'index.html', 'generate_pages.py', 'update_footers.py'}
    
    # 已更新的文件（手动更新过的）
    already_updated = {
        'what-we-offer.html',
        'get-inspired.html',
        'travel-resources.html',
        'contact.html',
        'privacy-policy.html',
        'faq.html'
    }
    
    # 查找所有HTML文件
    html_files = [f for f in base_dir.glob('*.html') 
                  if f.name not in exclude_files and f.name not in already_updated]
    
    updated_count = 0
    skipped_count = 0
    
    for html_file in html_files:
        if update_footer_in_file(html_file):
            print(f"✓ Updated: {html_file.name}")
            updated_count += 1
        else:
            print(f"✗ Skipped (no footer found): {html_file.name}")
            skipped_count += 1
    
    print(f"\n完成！更新了 {updated_count} 个文件，跳过了 {skipped_count} 个文件。")

if __name__ == '__main__':
    main()

