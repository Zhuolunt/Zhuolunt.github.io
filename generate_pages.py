#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量生成所有剩余页面的脚本
"""

# 通用头部HTML（简化版，用于子页面）
HEADER_HTML = '''    <header id="header" class="fixed w-full top-0 z-50 transition-all duration-300 bg-dark/95 shadow-lg">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center py-4">
                <a href="index.html" class="flex items-center space-x-2">
                    <img src="图片1.png" alt="Company Logo" class="h-14 w-auto object-contain rounded-lg" style="max-height: 72px; background-color: rgba(255,255,255,1); padding: 4px;">
                    <span class="text-xl md:text-2xl font-serif font-bold text-white ml-2 hidden md:inline">Journey<span class="text-secondary">Weaver</span></span>
                </a>
                <nav class="hidden md:flex space-x-8 items-center">
                    <div class="relative group">
                        <button class="text-white hover:text-secondary transition-colors duration-300 font-medium flex items-center">What We Offer <i class="fa fa-chevron-down ml-2 text-xs"></i></button>
                        <div class="absolute left-0 mt-2 w-56 bg-white rounded-lg shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50">
                            <div class="py-2">
                                <a href="all-journeys.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">All Journeys</a>
                                <a href="custom-journeys.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">Custom Journeys</a>
                                <a href="small-group-journeys.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">Small Group Journeys</a>
                                <a href="cultural-experiences.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">Cultural Experiences</a>
                                <a href="adventure-travel.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">Adventure Travel</a>
                                <a href="sustainable-tourism.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">Sustainable Tourism</a>
                            </div>
                        </div>
                    </div>
                    <div class="relative group">
                        <button class="text-white hover:text-secondary transition-colors duration-300 font-medium flex items-center">Get Inspired <i class="fa fa-chevron-down ml-2 text-xs"></i></button>
                        <div class="absolute left-0 mt-2 w-56 bg-white rounded-lg shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50">
                            <div class="py-2">
                                <a href="travelogue.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">Travelogue (Blog)</a>
                                <a href="travel-stories.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">Travel Stories</a>
                                <a href="testimonials.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">Testimonials</a>
                            </div>
                        </div>
                    </div>
                    <div class="relative group">
                        <button class="text-white hover:text-secondary transition-colors duration-300 font-medium flex items-center">Travel Resources <i class="fa fa-chevron-down ml-2 text-xs"></i></button>
                        <div class="absolute left-0 mt-2 w-56 bg-white rounded-lg shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50">
                            <div class="py-2">
                                <a href="travel-guides.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">Travel Guides</a>
                                <a href="travel-tips.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">Travel Tips</a>
                                <a href="visa-info.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">Visa Info</a>
                                <a href="faq.html" class="block px-4 py-2 text-dark hover:bg-secondary hover:text-white transition-colors duration-200">FAQ</a>
                            </div>
                        </div>
                    </div>
                    <a href="why-us.html" class="text-white hover:text-secondary transition-colors duration-300 font-medium">Why Us</a>
                    <a href="faq.html" class="text-white hover:text-secondary transition-colors duration-300 font-medium">FAQ</a>
                    <a href="contact.html" class="text-white hover:text-secondary transition-colors duration-300 font-medium">Contact</a>
                </nav>
                <a href="contact.html" class="hidden md:block bg-secondary hover:bg-secondary/90 text-white font-semibold py-2 px-6 rounded-full transition-all duration-300 transform hover:scale-105">PLAN YOUR JOURNEY</a>
                <button id="mobile-menu-button" class="md:hidden text-white text-2xl focus:outline-none p-2"><i class="fa fa-bars"></i></button>
            </div>
        </div>
    </header>'''

# 通用页脚HTML
FOOTER_HTML = '''    <footer class="bg-dark text-white pt-16 pb-12">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-12">
                <div class="md:col-span-2">
                    <div class="flex items-center mb-6">
                        <img src="图片1.png" alt="Journey Weaver Logo" class="h-12 w-auto object-contain bg-white p-2 rounded-lg">
                        <span class="ml-3 text-xl font-bold text-white">Journey Weaver</span>
                    </div>
                    <p class="text-gray-400 mb-6">Weave Journeys, Cherish Memories. Specializing in emotionally-driven, sustainable travel experiences across China.</p>
                </div>
                <div>
                    <h4 class="text-lg font-semibold mb-6">Quick Links</h4>
                    <ul class="space-y-3">
                        <li><a href="index.html" class="text-gray-400 hover:text-secondary transition-colors">Home</a></li>
                        <li><a href="all-journeys.html" class="text-gray-400 hover:text-secondary transition-colors">All Journeys</a></li>
                        <li><a href="why-us.html" class="text-gray-400 hover:text-secondary transition-colors">Why Us</a></li>
                        <li><a href="contact.html" class="text-gray-400 hover:text-secondary transition-colors">Contact</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-lg font-semibold mb-6">Contact</h4>
                    <ul class="space-y-3 text-gray-400">
                        <li>+86 021-64227654</li>
                        <li>service@journeyweaver-sh.com</li>
                        <li>Shanghai, China</li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-white/10 mt-10 pt-8 text-center text-gray-400 text-sm">
                © 2025 Journey Weaver. All rights reserved.
            </div>
        </div>
    </footer>'''

# 通用脚本
SCRIPT_HTML = '''    <script>
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, { threshold: 0.1 });
        document.querySelectorAll('.animate-slide-up').forEach(el => observer.observe(el));
    </script>'''

# 页面配置
PAGES = [
    {
        'filename': 'small-group-journeys.html',
        'title': 'Small Group Journeys - Journey Weaver | Intimate Group Travel Experiences',
        'description': 'Intimate group experiences with like-minded travelers, limited to small groups for authentic connections.',
        'hero_title': 'Small Group Journeys',
        'hero_subtitle': 'Intimate group experiences with like-minded travelers, limited to small groups for authentic connections',
        'breadcrumb': ['Home', 'All Journeys', 'Small Group Journeys'],
        'content': '''            <div class="text-center mb-16 animate-slide-up">
                <h2 class="text-4xl font-serif font-bold text-dark mb-4">Intimate Group Experiences</h2>
                <div class="w-24 h-1 bg-secondary mx-auto mb-6"></div>
                <p class="text-dark/70 max-w-2xl mx-auto text-lg">
                    Connect with like-minded travelers in small, intimate groups designed for authentic experiences and meaningful connections.
                </p>
            </div>

            <div class="grid md:grid-cols-2 gap-12 mb-16">
                <div class="animate-slide-up">
                    <h3 class="text-2xl font-serif font-semibold text-dark mb-6">Why Small Groups?</h3>
                    <ul class="space-y-4">
                        <li class="flex items-start gap-4">
                            <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                                <i class="fa fa-check text-primary"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-dark mb-1">Intimate Connections</h4>
                                <p class="text-dark/70">Small groups foster deeper connections between travelers and with local communities.</p>
                            </div>
                        </li>
                        <li class="flex items-start gap-4">
                            <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                                <i class="fa fa-check text-primary"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-dark mb-1">Flexible Itineraries</h4>
                                <p class="text-dark/70">Smaller groups allow for more spontaneous experiences and personalized attention.</p>
                            </div>
                        </li>
                        <li class="flex items-start gap-4">
                            <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                                <i class="fa fa-check text-primary"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-dark mb-1">Expert Guides</h4>
                                <p class="text-dark/70">Our professional guides can provide more personalized attention to each traveler.</p>
                            </div>
                        </li>
                        <li class="flex items-start gap-4">
                            <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                                <i class="fa fa-check text-primary"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-dark mb-1">Shared Experiences</h4>
                                <p class="text-dark/70">Create lasting memories with a small group of fellow adventurers.</p>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="animate-slide-up" style="animation-delay: 100ms;">
                    <div class="rounded-2xl overflow-hidden shadow-xl">
                        <img src="https://picsum.photos/id/10/800/600" alt="Small Group Journey" class="w-full h-full object-cover" loading="lazy">
                    </div>
                </div>
            </div>

            <div class="text-center animate-slide-up">
                <a href="contact.html" class="inline-block bg-secondary hover:bg-secondary/90 text-white font-semibold py-3 px-8 rounded-full text-lg transition-all duration-300 transform hover:scale-105 hover:shadow-lg">
                    Join a Small Group Journey
                </a>
            </div>'''
    },
    {
        'filename': 'cultural-experiences.html',
        'title': 'Cultural Experiences - Journey Weaver | Immersive Cultural Travel',
        'description': 'Deep cultural immersion through traditional workshops, local interactions, and heritage sites.',
        'hero_title': 'Cultural Experiences',
        'hero_subtitle': 'Deep cultural immersion through traditional workshops, local interactions, and heritage sites',
        'breadcrumb': ['Home', 'All Journeys', 'Cultural Experiences'],
        'content': '''            <div class="text-center mb-16 animate-slide-up">
                <h2 class="text-4xl font-serif font-bold text-dark mb-4">Immerse Yourself in Chinese Culture</h2>
                <div class="w-24 h-1 bg-secondary mx-auto mb-6"></div>
                <p class="text-dark/70 max-w-2xl mx-auto text-lg">
                    Experience authentic Chinese culture through hands-on workshops, local interactions, and visits to heritage sites.
                </p>
            </div>

            <div class="grid md:grid-cols-3 gap-8 mb-16">
                <div class="bg-light rounded-2xl p-8 animate-slide-up">
                    <div class="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-6">
                        <i class="fa fa-university text-primary text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-serif font-semibold text-dark mb-4">Traditional Workshops</h3>
                    <p class="text-dark/70 mb-6">Learn traditional crafts like pottery, calligraphy, and silk weaving from master artisans.</p>
                </div>
                <div class="bg-light rounded-2xl p-8 animate-slide-up" style="animation-delay: 100ms;">
                    <div class="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-6">
                        <i class="fa fa-users text-primary text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-serif font-semibold text-dark mb-4">Local Interactions</h3>
                    <p class="text-dark/70 mb-6">Meet local families, participate in daily life, and share meals with community members.</p>
                </div>
                <div class="bg-light rounded-2xl p-8 animate-slide-up" style="animation-delay: 200ms;">
                    <div class="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-6">
                        <i class="fa fa-building text-primary text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-serif font-semibold text-dark mb-4">Heritage Sites</h3>
                    <p class="text-dark/70 mb-6">Visit UNESCO World Heritage sites and learn about China's rich historical legacy.</p>
                </div>
            </div>

            <div class="text-center animate-slide-up">
                <a href="contact.html" class="inline-block bg-secondary hover:bg-secondary/90 text-white font-semibold py-3 px-8 rounded-full text-lg transition-all duration-300 transform hover:scale-105 hover:shadow-lg">
                    Explore Cultural Experiences
                </a>
            </div>'''
    },
    {
        'filename': 'adventure-travel.html',
        'title': 'Adventure Travel - Journey Weaver | Thrilling Expeditions in China',
        'description': 'Thrilling expeditions and challenging routes for adventure enthusiasts seeking extraordinary experiences.',
        'hero_title': 'Adventure Travel',
        'hero_subtitle': 'Thrilling expeditions and challenging routes for adventure enthusiasts',
        'breadcrumb': ['Home', 'All Journeys', 'Adventure Travel'],
        'content': '''            <div class="text-center mb-16 animate-slide-up">
                <h2 class="text-4xl font-serif font-bold text-dark mb-4">Thrilling Expeditions</h2>
                <div class="w-24 h-1 bg-secondary mx-auto mb-6"></div>
                <p class="text-dark/70 max-w-2xl mx-auto text-lg">
                    Challenge yourself with our carefully designed adventure routes across China's most spectacular landscapes.
                </p>
            </div>

            <div class="grid md:grid-cols-2 gap-12 mb-16">
                <div class="animate-slide-up">
                    <h3 class="text-2xl font-serif font-semibold text-dark mb-6">Adventure Options</h3>
                    <ul class="space-y-4">
                        <li class="flex items-start gap-4">
                            <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                                <i class="fa fa-mountain text-primary"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-dark mb-1">Mountain Expeditions</h4>
                                <p class="text-dark/70">Trek through the Himalayas, explore Tibetan plateaus, and conquer challenging peaks.</p>
                            </div>
                        </li>
                        <li class="flex items-start gap-4">
                            <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                                <i class="fa fa-bicycle text-primary"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-dark mb-1">Cycling Adventures</h4>
                                <p class="text-dark/70">Cycle through scenic routes, from ancient trade routes to modern highways.</p>
                            </div>
                        </li>
                        <li class="flex items-start gap-4">
                            <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                                <i class="fa fa-ship text-primary"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-dark mb-1">Water Sports</h4>
                                <p class="text-dark/70">Rafting, kayaking, and other water-based adventures in pristine rivers and lakes.</p>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="animate-slide-up" style="animation-delay: 100ms;">
                    <div class="rounded-2xl overflow-hidden shadow-xl">
                        <img src="https://picsum.photos/id/1043/800/600" alt="Adventure Travel" class="w-full h-full object-cover" loading="lazy">
                    </div>
                </div>
            </div>

            <div class="text-center animate-slide-up">
                <a href="contact.html" class="inline-block bg-secondary hover:bg-secondary/90 text-white font-semibold py-3 px-8 rounded-full text-lg transition-all duration-300 transform hover:scale-105 hover:shadow-lg">
                    Plan Your Adventure
                </a>
            </div>'''
    },
    {
        'filename': 'sustainable-tourism.html',
        'title': 'Sustainable Tourism - Journey Weaver | Eco-Friendly Travel',
        'description': 'Eco-friendly journeys with carbon-neutral routes and support for local conservation efforts.',
        'hero_title': 'Sustainable Tourism',
        'hero_subtitle': 'Eco-friendly journeys with carbon-neutral routes and support for local conservation',
        'breadcrumb': ['Home', 'All Journeys', 'Sustainable Tourism'],
        'content': '''            <div class="text-center mb-16 animate-slide-up">
                <h2 class="text-4xl font-serif font-bold text-dark mb-4">Travel Responsibly</h2>
                <div class="w-24 h-1 bg-secondary mx-auto mb-6"></div>
                <p class="text-dark/70 max-w-2xl mx-auto text-lg">
                    Our commitment to sustainable tourism ensures your travels contribute positively to the destinations you visit.
                </p>
            </div>

            <div class="grid md:grid-cols-2 gap-12 mb-16">
                <div class="animate-slide-up">
                    <h3 class="text-2xl font-serif font-semibold text-dark mb-6">Our Sustainability Practices</h3>
                    <ul class="space-y-4">
                        <li class="flex items-start gap-4">
                            <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                                <i class="fa fa-leaf text-primary"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-dark mb-1">Carbon-Neutral Routes</h4>
                                <p class="text-dark/70">All western routes follow our "Dual Carbon Plan" with carbon offset programs.</p>
                            </div>
                        </li>
                        <li class="flex items-start gap-4">
                            <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                                <i class="fa fa-heart text-primary"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-dark mb-1">Local Community Support</h4>
                                <p class="text-dark/70">10% of fees from western routes are donated to local ecological funds.</p>
                            </div>
                        </li>
                        <li class="flex items-start gap-4">
                            <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center flex-shrink-0 mt-1">
                                <i class="fa fa-recycle text-primary"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-dark mb-1">Eco-Friendly Accommodations</h4>
                                <p class="text-dark/70">We partner with sustainable hotels and lodges that prioritize environmental responsibility.</p>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="animate-slide-up" style="animation-delay: 100ms;">
                    <div class="rounded-2xl overflow-hidden shadow-xl">
                        <img src="https://picsum.photos/id/1044/800/600" alt="Sustainable Tourism" class="w-full h-full object-cover" loading="lazy">
                    </div>
                </div>
            </div>

            <div class="text-center animate-slide-up">
                <a href="contact.html" class="inline-block bg-secondary hover:bg-secondary/90 text-white font-semibold py-3 px-8 rounded-full text-lg transition-all duration-300 transform hover:scale-105 hover:shadow-lg">
                    Choose Sustainable Travel
                </a>
            </div>'''
    },
]

# HTML模板
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://www.journeyweaver-sh.com/{filename}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha256-eZrrJcwDc/3uDhsdt61sL2oOBY362qM3lon1gyExkL0=" crossorigin="anonymous" />
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        primary: '#2A6496',
                        secondary: '#F4A261',
                        accent: '#E9C46A',
                        dark: '#0F172A',
                        light: '#F8FAFC',
                        muted: '#64748B',
                    }},
                    fontFamily: {{
                        serif: ['Playfair Display', 'serif'],
                        sans: ['Montserrat', 'sans-serif'],
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ font-family: 'Montserrat', sans-serif; }}
        h1, h2, h3, h4, h5, h6 {{ font-family: 'Playfair Display', 'serif'; }}
        html {{ scroll-behavior: smooth; }}
        .animate-slide-up {{
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.8s ease-out;
        }}
        .animate-slide-up.animate-in {{
            opacity: 1;
            transform: translateY(0);
        }}
    </style>
</head>
<body class="bg-light text-dark">
{header}

    <section class="pt-32 pb-20 bg-gradient-to-br from-primary to-primary/80 text-white">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
            <div class="max-w-3xl mx-auto text-center animate-slide-up">
                <h1 class="text-5xl md:text-6xl font-serif font-bold mb-6">{hero_title}</h1>
                <p class="text-xl text-white/90 mb-8">{hero_subtitle}</p>
                <nav class="flex justify-center items-center gap-2 text-sm">
                    {breadcrumb_html}
                </nav>
            </div>
        </div>
    </section>

    <section class="py-20 bg-white">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
{content}
        </div>
    </section>

{footer}
{script}
</body>
</html>'''

def generate_breadcrumb(breadcrumb_items):
    """生成面包屑导航HTML"""
    items = []
    for i, item in enumerate(breadcrumb_items):
        if i == len(breadcrumb_items) - 1:
            items.append(f'<span class="text-white">{item}</span>')
        else:
            href = 'index.html' if item == 'Home' else f'{item.lower().replace(" ", "-")}.html'
            items.append(f'<a href="{href}" class="text-white/70 hover:text-white">{item}</a>')
        if i < len(breadcrumb_items) - 1:
            items.append('<i class="fa fa-chevron-right text-white/50 text-xs"></i>')
    return '\n                    '.join(items)

def generate_page(page_config):
    """生成单个页面"""
    breadcrumb_html = generate_breadcrumb(page_config['breadcrumb'])
    
    html = HTML_TEMPLATE.format(
        title=page_config['title'],
        description=page_config['description'],
        filename=page_config['filename'],
        header=HEADER_HTML,
        hero_title=page_config['hero_title'],
        hero_subtitle=page_config['hero_subtitle'],
        breadcrumb_html=breadcrumb_html,
        content=page_config['content'],
        footer=FOOTER_HTML,
        script=SCRIPT_HTML
    )
    
    return html

if __name__ == '__main__':
    for page in PAGES:
        html_content = generate_page(page)
        with open(page['filename'], 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Generated: {page['filename']}")

