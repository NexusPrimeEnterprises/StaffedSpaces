import re

with open('index.html', 'r') as f:
    content = f.read()

# Modal CSS
modal_css = '''
/* Modal Styles */
.modal-overlay { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.7); z-index: 10000; align-items: center; justify-content: center; padding: 20px; }
.modal-overlay.active { display: flex; }
.modal-content { background: var(--white); border-radius: 20px; max-width: 800px; max-height: 90vh; overflow-y: auto; padding: 40px; position: relative; }
.modal-close { position: absolute; top: 15px; right: 20px; font-size: 2rem; cursor: pointer; color: var(--gray-400); background: none; border: none; }
.modal-close:hover { color: var(--dark-slate); }
.modal-content h2 { color: var(--dark-slate); margin-bottom: 20px; font-size: 1.8rem; }
.modal-content h3 { color: var(--teal); margin: 25px 0 10px; font-size: 1.2rem; }
.modal-content p, .modal-content li { color: var(--gray-500); line-height: 1.7; margin-bottom: 10px; }
.modal-content ul { margin-left: 20px; margin-bottom: 15px; list-style: disc; }
'''

content = content.replace('</style>', modal_css + '</style>')

with open('index.html', 'w') as f:
    f.write(content)

print('CSS added!')

# Add second script to add modals
with open('index.html', 'r') as f:
    content = f.read()

privacy_modal = '''
<!-- Privacy Policy Modal -->
<div class="modal-overlay" id="privacyModal">
<div class="modal-content">
<button class="modal-close" onclick="closeModal('privacyModal')">&times;</button>
<h2>Privacy Policy</h2>
<p><strong>Nexus Prime Enterprises LLC-FZ</strong> (StaffedSpaces)<br>Dubai, United Arab Emirates<br><em>Last updated: January 2026</em></p>
<h3>1. Data Controller</h3>
<p>Nexus Prime Enterprises LLC-FZ, registered in Dubai, UAE, is responsible for processing your personal data.</p>
<h3>2. Data We Collect</h3>
<ul><li>Contact Information: Name, email, phone, company</li><li>Business Information: Industry, team size, preferences</li><li>Technical Data: IP address, browser, device info</li></ul>
<h3>3. How We Use Your Data</h3>
<ul><li>To provide our staffing services</li><li>To communicate about our services</li><li>To process inquiries</li><li>To comply with legal obligations</li></ul>
<h3>4. Data Storage</h3>
<p>Customer data is stored in Bitrix24 CRM or customer systems. Customers own all data and can export or delete it anytime.</p>
<h3>5. Your Rights</h3>
<p>You can access, correct, delete, or export your data. Contact: privacy@staffedspaces.com</p>
<h3>6. Data Retention</h3>
<p>Data retained during business relationship plus 2 years. Deletion available within 30 days after termination.</p>
</div>
</div>
'''

terms_modal = '''
<!-- Terms of Service Modal -->
<div class="modal-overlay" id="termsModal">
<div class="modal-content">
<button class="modal-close" onclick="closeModal('termsModal')">&times;</button>
<h2>Terms of Service</h2>
<p><strong>Nexus Prime Enterprises LLC-FZ</strong><br>Dubai, UAE<br><em>Version 3.0 - January 2026</em></p>
<h3>1. Service Description</h3>
<p>StaffedSpaces provides managed remote teams with office space, MacBooks, 4K monitors, and live monitoring in Bangladesh.</p>
<h3>2. Packages</h3>
<ul><li><strong>Trial:</strong> 2 workstations, $1,500/mo, 90 days</li><li><strong>Professional:</strong> 4 workstations, $2,600/mo</li><li><strong>Enterprise:</strong> 8+ workstations, $4,000/mo</li></ul>
<h3>3. Payment</h3>
<p>Infrastructure fees invoiced monthly in advance. Due within 7 days. Deposit required at start.</p>
<h3>4. Replacements</h3>
<p>Professional/Enterprise: Unlimited free replacements. Trial: 2 free replacements.</p>
<h3>5. Liability</h3>
<p>Liability limited to intentional misconduct and gross negligence. Maximum: annual contract value.</p>
<h3>6. Termination</h3>
<p>Trial: 14 days notice. Professional/Enterprise: 30 days notice after minimum term.</p>
<h3>7. Governing Law</h3>
<p>UAE law applies. Jurisdiction: Dubai, UAE.</p>
</div>
</div>
'''

modal_script = '''
<script>
function openModal(id) { document.getElementById(id).classList.add('active'); document.body.style.overflow = 'hidden'; }
function closeModal(id) { document.getElementById(id).classList.remove('active'); document.body.style.overflow = 'auto'; }
document.querySelectorAll('.modal-overlay').forEach(m => m.addEventListener('click', e => { if(e.target === m) closeModal(m.id); }));
document.addEventListener('keydown', e => { if(e.key === 'Escape') document.querySelectorAll('.modal-overlay.active').forEach(m => closeModal(m.id)); });
</script>
'''

content = content.replace('</body>', privacy_modal + terms_modal + modal_script + '</body>')

# Fix footer links
content = content.replace('href="#">Privacy Policy', 'href="javascript:openModal(\'privacyModal\')">Privacy Policy')
content = content.replace('href="#">Terms of Service', 'href="javascript:openModal(\'termsModal\')">Terms of Service')

# Make service links non-clickable
for svc in ['Customer Support', 'Data Entry', 'Virtual Assistants', 'Back Office']:
    content = content.replace(f'<a href="#">{svc}</a>', f'<span style="color: var(--gray-400)">{svc}</span>')

with open('index.html', 'w') as f:
    f.write(content)

print('Modals added!')
