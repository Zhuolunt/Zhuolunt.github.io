#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复所有HTML页面的导航栏，将button改为a标签
"""

import os
import re
from pathlib import Path

# 正确的导航栏代码（从index.html复制）
CORRECT_NAV = '''                <nav class="hidden md:flex space-x-8 items-center">
                    
                    <div class="relative group">
                        <a href="what-we-offer.html" class="text-white hover:text-secondary transition-colors duration-300 font-medium flex items-center">
                            What We Offer
                            <i class="fa fa-chevron-down ml-2 text-xs transition-transform duration-300 group-hover:rotate-180"></i>
                        </a>
                        <div class="absolute left-0 mt-2 w-[600px] bg-white rounded-lg shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 transform origin-top scale-95 group-hover:scale-100 mega-menu border border-gray-100">
                            <div class="p-6">
                                <div class="mb-4 pb-4 border-b border-gray-200">
                                    <a href="what-we-offer.html" class="block text-primary hover:text-secondary font-semibold text-base mb-1 transition-colors duration-200">View All Services →</a>
                                    <p class="text-dark/60 text-xs">Complete overview of our travel experiences</p>
                                </div>
                                <div class="grid grid-cols-3 gap-6">
                                    <div>
                                        <h4 class="font-semibold text-dark mb-3 text-sm uppercase tracking-wide">By Type</h4>
                                        <ul class="space-y-2">
                                            <li><a href="all-journeys.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">All Journeys</a></li>
                                            <li><a href="custom-journeys.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Custom Journeys</a></li>
                                            <li><a href="small-group-journeys.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Small Group Journeys</a></li>
                                        </ul>
                                    </div>
                                    <div>
                                        <h4 class="font-semibold text-dark mb-3 text-sm uppercase tracking-wide">By Experience</h4>
                                        <ul class="space-y-2">
                                            <li><a href="cultural-experiences.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Cultural Experiences</a></li>
                                            <li><a href="adventure-travel.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Adventure Travel</a></li>
                                            <li><a href="sustainable-tourism.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Sustainable Tourism</a></li>
                                        </ul>
                                    </div>
                                    <div>
                                        <h4 class="font-semibold text-dark mb-3 text-sm uppercase tracking-wide">By Interest</h4>
                                        <ul class="space-y-2">
                                            <li><a href="all-journeys.html?interest=culinary" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Culinary</a></li>
                                            <li><a href="all-journeys.html?interest=hiking" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Hiking (GUDAO)</a></li>
                                            <li><a href="all-journeys.html?interest=archaeology" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Archaeology</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="relative group">
                        <a href="get-inspired.html" class="text-white hover:text-secondary transition-colors duration-300 font-medium flex items-center">
                            Get Inspired
                            <i class="fa fa-chevron-down ml-2 text-xs transition-transform duration-300 group-hover:rotate-180"></i>
                        </a>
                        <div class="absolute left-0 mt-2 w-[400px] bg-white rounded-lg shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 transform origin-top scale-95 group-hover:scale-100 mega-menu border border-gray-100">
                            <div class="p-6">
                                <div class="mb-4 pb-4 border-b border-gray-200">
                                    <a href="get-inspired.html" class="block text-primary hover:text-secondary font-semibold text-base mb-1 transition-colors duration-200">View All Inspiration →</a>
                                    <p class="text-dark/60 text-xs">Stories, blogs, and travel experiences</p>
                                </div>
                                <div class="space-y-4">
                                    <div>
                                        <h4 class="font-semibold text-dark mb-3 text-sm uppercase tracking-wide">Stories & Inspiration</h4>
                                        <ul class="space-y-2">
                                            <li><a href="travelogue.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Travelogue (Blog)</a></li>
                                            <li><a href="travel-stories.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Travel Stories</a></li>
                                            <li><a href="testimonials.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Testimonials</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="relative group">
                        <a href="travel-resources.html" class="text-white hover:text-secondary transition-colors duration-300 font-medium flex items-center">
                            Travel Resources
                            <i class="fa fa-chevron-down ml-2 text-xs transition-transform duration-300 group-hover:rotate-180"></i>
                        </a>
                        <div class="absolute left-0 mt-2 w-[400px] bg-white rounded-lg shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 transform origin-top scale-95 group-hover:scale-100 mega-menu border border-gray-100">
                            <div class="p-6">
                                <div class="mb-4 pb-4 border-b border-gray-200">
                                    <a href="travel-resources.html" class="block text-primary hover:text-secondary font-semibold text-base mb-1 transition-colors duration-200">View All Resources →</a>
                                    <p class="text-dark/60 text-xs">Guides, tips, and planning information</p>
                                </div>
                                <div class="space-y-4">
                                    <div>
                                        <h4 class="font-semibold text-dark mb-3 text-sm uppercase tracking-wide">Planning Resources</h4>
                                        <ul class="space-y-2">
                                            <li><a href="travel-guides.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Travel Guides</a></li>
                                            <li><a href="travel-tips.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Travel Tips</a></li>
                                            <li><a href="visa-info.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Visa Info</a></li>
                                            <li><a href="faq.html" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">FAQ</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="relative group">
                        <a href="why-us.html" class="text-white hover:text-secondary transition-colors duration-300 font-medium flex items-center">
                            Why Us
                            <i class="fa fa-chevron-down ml-2 text-xs transition-transform duration-300 group-hover:rotate-180"></i>
                        </a>
                        <div class="absolute left-0 mt-2 w-[400px] bg-white rounded-lg shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 transform origin-top scale-95 group-hover:scale-100 mega-menu border border-gray-100">
                            <div class="p-6">
                                <div class="mb-4 pb-4 border-b border-gray-200">
                                    <a href="why-us.html" class="block text-primary hover:text-secondary font-semibold text-base mb-1 transition-colors duration-200">View All →</a>
                                    <p class="text-dark/60 text-xs">Learn more about our company</p>
                                </div>
                                <div class="space-y-4">
                                    <div>
                                        <h4 class="font-semibold text-dark mb-3 text-sm uppercase tracking-wide">About Us</h4>
                                        <ul class="space-y-2">
                                            <li><a href="why-us.html#awards" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Awards and Press</a></li>
                                            <li><a href="why-us.html#people" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Our People</a></li>
                                            <li><a href="why-us.html#sustainability" class="block text-dark/70 hover:text-secondary transition-colors duration-200 text-sm">Sustainability</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <a href="faq.html" class="text-white hover:text-secondary transition-colors duration-300 font-medium">FAQ</a>
                    <a href="contact.html" class="text-white hover:text-secondary transition-colors duration-300 font-medium">Contact</a>
                </nav>'''

# 需要修复的HTML文件列表（排除index.html和why-us.html，因为它们已经是正确的）
html_files = [
    "what-we-offer.html",
    "get-inspired.html",
    "travel-resources.html",
    "all-journeys.html",
    "custom-journeys.html",
    "small-group-journeys.html",
    "cultural-experiences.html",
    "adventure-travel.html",
    "sustainable-tourism.html",
    "travelogue.html",
    "travel-stories.html",
    "testimonials.html",
    "travel-guides.html",
    "travel-tips.html",
    "visa-info.html",
    "faq.html",
    "contact.html",
    "blog-tea-horse-road.html",
    "blog-sustainable-travel.html",
    "blog-silk-road.html",
    "blog-sichuan-cuisine.html",
    "blog-guizhou-culture.html",
    "blog-tibetan-plateau.html",
    "privacy-policy.html",
    "terms-of-service.html",
    "cookie-policy.html",
]

def fix_navigation(file_path):
    """修复单个文件的导航栏"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 匹配导航栏区域（使用更宽松的正则表达式）
        # 匹配从 <nav class="hidden md:flex 开始到 </nav> 结束的整个导航栏
        nav_pattern = r'<nav\s+class="hidden\s+md:flex[^"]*"[^>]*>.*?</nav>'
        
        # 使用 DOTALL 标志使 . 匹配换行符
        match = re.search(nav_pattern, content, re.DOTALL | re.IGNORECASE)
        
        if match:
            # 替换整个导航栏
            content = re.sub(nav_pattern, CORRECT_NAV, content, flags=re.DOTALL | re.IGNORECASE)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ 已修复: {file_path}")
                return True
            else:
                print(f"- 无需修复: {file_path}")
                return False
        else:
            print(f"⚠ 未找到导航栏: {file_path}")
            return False
            
    except Exception as e:
        print(f"✗ 错误 {file_path}: {e}")
        return False

def main():
    base_dir = Path(__file__).parent
    fixed_count = 0
    
    for html_file in html_files:
        file_path = base_dir / html_file
        if file_path.exists():
            if fix_navigation(file_path):
                fixed_count += 1
        else:
            print(f"⚠ 文件不存在: {html_file}")
    
    print(f"\n完成！共修复 {fixed_count} 个文件。")

if __name__ == "__main__":
    main()
