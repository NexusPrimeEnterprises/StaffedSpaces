import re

with open('/Users/' + __import__('os').path.expanduser('~').split('/')[-1] + '/Desktop/StaffedSpaces/index.html', 'r') as f:
    content = f.read()

# Fix Trust Bar - replace placeholders based on following text
content = re.sub(r'TRUST_ICON_PLACEHOLDER(\s*<span>Premium MacBooks)', r'<div class="trust-icon"><i data-lucide="laptop"></i></div>\1', content)
content = re.sub(r'TRUST_ICON_PLACEHOLDER(\s*<span>ChatGPT)', r'<div class="trust-icon"><i data-lucide="bot"></i></div>\1', content)
content = re.sub(r'TRUST_ICON_PLACEHOLDER(\s*<span>Fiber)', r'<div class="trust-icon"><i data-lucide="wifi"></i></div>\1', content)
content = re.sub(r'TRUST_ICON_PLACEHOLDER(\s*<span>Unlimited)', r'<div class="trust-icon"><i data-lucide="refresh-cw"></i></div>\1', content)

# Any remaining placeholders back to laptop
content = content.replace('TRUST_ICON_PLACEHOLDER', '<div class="trust-icon"><i data-lucide="laptop"></i></div>')

with open('/Users/' + __import__('os').path.expanduser('~').split('/')[-1] + '/Desktop/StaffedSpaces/index.html', 'w') as f:
    f.write(content)

print('Done!')
