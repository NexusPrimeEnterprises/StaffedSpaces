import re

with open('/Users/' + __import__('os').environ['USER'] + '/Desktop/StaffedSpaces/index.html', 'r') as f:
    content = f.read()

# Trust Bar Icons
replacements = [
    ('trust-icon"></div>\n *<span>Premium MacBooks', 'trust-icon"><i data-lucide="laptop"></i></div>\n <span>Premium MacBooks'),
    ('trust-icon"></div>\n *<span>ChatGPT', 'trust-icon"><i data-lucide="bot"></i></div>\n <span>ChatGPT'),
    ('trust-icon"></div>\n *<span>Fiber', 'trust-icon"><i data-lucide="wifi"></i></div>\n <span>Fiber'),
    ('trust-icon"></div>\n *<span>Unlimited', 'trust-icon"><i data-lucide="refresh-cw"></i></div>\n <span>Unlimited'),
]

for old, new in replacements:
    content = re.sub(old, new, content)

# Transparency Icons
content = re.sub(r'feature-icon-circle"></div>\n *<div>\n *<h4>Live Screen', 'feature-icon-circle"><i data-lucide="monitor"></i></div>\n <div>\n <h4>Live Screen', content)
content = re.sub(r'feature-icon-circle"></div>\n *<div>\n *<h4>Webcam', 'feature-icon-circle"><i data-lucide="video"></i></div>\n <div>\n <h4>Webcam', content)
content = re.sub(r'feature-icon-circle">[^<]*</div>\n *<div>\n *<h4>Digital Time', 'feature-icon-circle"><i data-lucide="clock"></i></div>\n <div>\n <h4>Digital Time', content)
content = re.sub(r'feature-icon-circle"></div>\n *<div>\n *<h4>Performance', 'feature-icon-circle"><i data-lucide="bar-chart-2"></i></div>\n <div>\n <h4>Performance', content)

# Plan Icons  
content = re.sub(r'<!-- TRIAL -->\n *<div class="pricing-card">\n *<div class="plan-icon"></div>', '<!-- TRIAL -->\n <div class="pricing-card">\n <div class="plan-icon"><i data-lucide="rocket"></i></div>', content)
content = re.sub(r'<div class="plan-icon"></div>\n *<div class="plan-header">\n *<div class="plan-name">Professional', '<div class="plan-icon"><i data-lucide="briefcase"></i></div>\n <div class="plan-header">\n <div class="plan-name">Professional', content)
content = re.sub(r'<div class="plan-icon"></div>\n *<div class="plan-header">\n *<div class="plan-name">Enterprise', '<div class="plan-icon"><i data-lucide="building"></i></div>\n <div class="plan-header">\n <div class="plan-name">Enterprise', content)

# Add CSS for trust-icon svg and feature-icon-circle svg and plan-icon svg
css_additions = '''
 .trust-icon svg {
 width: 24px;
 height: 24px;
 stroke: var(--teal);
 stroke-width: 2;
 }
 
 .feature-icon-circle svg {
 width: 26px;
 height: 26px;
 stroke: var(--gold);
 stroke-width: 2;
 }
 
 .plan-icon svg {
 width: 48px;
 height: 48px;
 stroke: var(--teal);
 stroke-width: 1.5;
 }
 
 .plan-icon {
 display: flex;
 justify-content: center;
 }
'''

# Insert CSS before the closing </style> or after trust-icon definition
content = re.sub(r'(\.trust-icon \{[^}]+\})', r'\1' + css_additions, content, count=1)

with open('/Users/' + __import__('os').environ['USER'] + '/Desktop/StaffedSpaces/index.html', 'w') as f:
    f.write(content)

print('Done!')
