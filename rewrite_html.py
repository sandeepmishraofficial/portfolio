import os

file_path = r'c:\workspace\sandeepmishraofficial.github.io-main\core\templates\core\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Hero Section
content = content.replace('Network Engineer specializing in routing, switching, LAN/WAN infrastructure, and network design. Cisco IOS, GNS3, Wireshark, OSPF/EIGRP.', '{{ personal_info.description }}')
content = content.replace('Available for opportunities', '{{ personal_info.status_label }}')
content = content.replace("Hi, I'm<br>\n            <span class=\"text-accent\">Sandeep</span><br>", "Hi, I'm<br>\n            <span class=\"text-accent\">{{ personal_info.name.split.0 }}</span><br>")
content = content.replace('Networking professional with hands-on experience in LAN/WAN infrastructure, routing & switching, and network troubleshooting. Passionate about building reliable, scalable networks.', '{{ personal_info.description }}')

content = content.replace('href="https://drive.google.com/file/d/1-nPnIcGA29diiEJPiFO1zfLGNtCYu9YI/view"', 'href="{{ personal_info.cv_link }}"')

# Social Links
# The social links are tricky to replace precisely with string replacement, but we can replace the entire block.
social_links_old = """<div class="fade-up fade-up-5 flex items-center gap-4">
            <a href="https://linkedin.com/in/sandeepmishraofficial" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-200 dark:border-slate-700 text-slate-500 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-linkedin"></i></a>
            <a href="https://github.com/sandeepmishraofficial" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-200 dark:border-slate-700 text-slate-500 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-github"></i></a>
            <a href="https://twitter.com/Sandeep_code" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-200 dark:border-slate-700 text-slate-500 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-twitter"></i></a>
            <a href="https://instagram.com/sandeepmishra._" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-200 dark:border-slate-700 text-slate-500 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-instagram"></i></a>
          </div>"""

social_links_new = """<div class="fade-up fade-up-5 flex items-center gap-4">
            {% if personal_info.linkedin_url %}<a href="{{ personal_info.linkedin_url }}" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-200 dark:border-slate-700 text-slate-500 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-linkedin"></i></a>{% endif %}
            {% if personal_info.github_url %}<a href="{{ personal_info.github_url }}" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-200 dark:border-slate-700 text-slate-500 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-github"></i></a>{% endif %}
            {% if personal_info.twitter_url %}<a href="{{ personal_info.twitter_url }}" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-200 dark:border-slate-700 text-slate-500 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-twitter"></i></a>{% endif %}
            {% if personal_info.instagram_url %}<a href="{{ personal_info.instagram_url }}" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-200 dark:border-slate-700 text-slate-500 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-instagram"></i></a>{% endif %}
          </div>"""
content = content.replace(social_links_old, social_links_new)

# Profile Card
profile_card_old = """<!-- Profile -->
              <div class="flex items-center gap-4 mb-6">
                <div class="w-16 h-16 rounded-xl bg-gradient-to-br from-accent to-blue-400 flex items-center justify-center text-white text-2xl font-bold font-display shadow-lg">
                  SM
                </div>
                <div>
                  <div class="font-display font-bold text-lg">Sandeep Mishra</div>
                  <div class="text-sm text-slate-500 dark:text-slate-400">Network Engineer</div>
                  <div class="flex items-center gap-1.5 mt-1">
                    <span class="dot-online" style="width:7px;height:7px;"></span>
                    <span class="text-xs text-green-600 dark:text-green-400 font-medium">Open to work</span>
                  </div>
                </div>
              </div>

              <div class="space-y-3 mb-6">
                <div class="flex items-center gap-3 text-sm text-slate-600 dark:text-slate-400">
                  <i class="fas fa-map-marker-alt text-accent w-4"></i>
                  <span>New Delhi, India</span>
                </div>
                <div class="flex items-center gap-3 text-sm text-slate-600 dark:text-slate-400">
                  <i class="fas fa-graduation-cap text-accent w-4"></i>
                  <span>BCA — Graduating 2025</span>
                </div>
                <div class="flex items-center gap-3 text-sm text-slate-600 dark:text-slate-400">
                  <i class="fas fa-briefcase text-accent w-4"></i>
                  <span>6+ months experience</span>
                </div>
              </div>"""

profile_card_new = """<!-- Profile -->
              <div class="flex items-center gap-4 mb-6">
                <div class="w-16 h-16 rounded-xl bg-gradient-to-br from-accent to-blue-400 flex items-center justify-center text-white text-2xl font-bold font-display shadow-lg uppercase">
                  {{ personal_info.name.0 }}{{ personal_info.name.split.1.0 }}
                </div>
                <div>
                  <div class="font-display font-bold text-lg">{{ personal_info.name }}</div>
                  <div class="text-sm text-slate-500 dark:text-slate-400">{{ personal_info.job_title }}</div>
                  {% if personal_info.open_to_work %}
                  <div class="flex items-center gap-1.5 mt-1">
                    <span class="dot-online" style="width:7px;height:7px;"></span>
                    <span class="text-xs text-green-600 dark:text-green-400 font-medium">Open to work</span>
                  </div>
                  {% endif %}
                </div>
              </div>

              <div class="space-y-3 mb-6">
                <div class="flex items-center gap-3 text-sm text-slate-600 dark:text-slate-400">
                  <i class="fas fa-map-marker-alt text-accent w-4"></i>
                  <span>{{ personal_info.location }}</span>
                </div>
                <div class="flex items-center gap-3 text-sm text-slate-600 dark:text-slate-400">
                  <i class="fas fa-graduation-cap text-accent w-4"></i>
                  <span>{{ personal_info.education_summary }}</span>
                </div>
                <div class="flex items-center gap-3 text-sm text-slate-600 dark:text-slate-400">
                  <i class="fas fa-briefcase text-accent w-4"></i>
                  <span>{{ personal_info.experience_summary }}</span>
                </div>
              </div>"""
content = content.replace(profile_card_old, profile_card_new)

# About Cards
about_cards_old = """<div class="md:col-span-1 space-y-4">
            <div class="about-card">
              <div class="w-10 h-10 bg-blue-50 dark:bg-blue-950/50 rounded-lg flex items-center justify-center mb-4">
                <i class="fas fa-network-wired text-accent"></i>
              </div>
              <h3 class="font-display font-bold text-base mb-2">Network Engineer</h3>
              <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">
                Configuring and maintaining routers, switches, and LAN/WAN infrastructure. Skilled in Cisco IOS, VLANs, and STP.
              </p>
            </div>

            <div class="about-card" style="border-left-color:#6366f1">
              <div class="w-10 h-10 bg-indigo-50 dark:bg-indigo-950/50 rounded-lg flex items-center justify-center mb-4">
                <i class="fas fa-route text-indigo-500"></i>
              </div>
              <h3 class="font-display font-bold text-base mb-2">Routing & Protocols</h3>
              <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">
                Hands-on with OSPF, EIGRP, BGP, static routing, and inter-VLAN routing for enterprise topologies.
              </p>
            </div>

            <div class="about-card" style="border-left-color:#0891b2">
              <div class="w-10 h-10 bg-cyan-50 dark:bg-cyan-950/50 rounded-lg flex items-center justify-center mb-4">
                <i class="fas fa-traffic-light text-cyan-500"></i>
              </div>
              <h3 class="font-display font-bold text-base mb-2">Network Monitoring</h3>
              <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">
                Analyzing traffic with Wireshark, identifying anomalies, packet loss, and connectivity issues across endpoints.
              </p>
            </div>
          </div>"""

about_cards_new = """<div class="md:col-span-1 space-y-4">
            {% for card in about_cards %}
            <div class="about-card" {% if card.border_color_code %}style="border-left-color:{{ card.border_color_code }}"{% endif %}>
              <div class="w-10 h-10 {{ card.bg_color_class }} rounded-lg flex items-center justify-center mb-4">
                <i class="{{ card.icon_class }} {{ card.icon_color_class }}"></i>
              </div>
              <h3 class="font-display font-bold text-base mb-2">{{ card.title }}</h3>
              <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">
                {{ card.description }}
              </p>
            </div>
            {% endfor %}
          </div>"""
content = content.replace(about_cards_old, about_cards_new)

# Highlights
highlights_old = """<ul class="space-y-4">
                <li class="flex items-start gap-3 text-sm">
                  <i class="fas fa-check text-accent mt-0.5 flex-shrink-0"></i>
                  <span class="text-slate-600 dark:text-slate-400">6+ months hands-on experience in network configuration and troubleshooting across 50+ endpoints</span>
                </li>
                <li class="flex items-start gap-3 text-sm">
                  <i class="fas fa-check text-accent mt-0.5 flex-shrink-0"></i>
                  <span class="text-slate-600 dark:text-slate-400">Configured OSPF, EIGRP routing and VLANs in enterprise lab environments using GNS3 & Cisco Packet Tracer</span>
                </li>
                <li class="flex items-start gap-3 text-sm">
                  <i class="fas fa-check text-accent mt-0.5 flex-shrink-0"></i>
                  <span class="text-slate-600 dark:text-slate-400">Built multi-layer enterprise network topologies simulating real-world infrastructure in home lab</span>
                </li>
                <li class="flex items-start gap-3 text-sm">
                  <i class="fas fa-check text-accent mt-0.5 flex-shrink-0"></i>
                  <span class="text-slate-600 dark:text-slate-400">Certified in Networking Fundamentals (Coding Seekho Institute) and Python (HackerRank)</span>
                </li>
                <li class="flex items-start gap-3 text-sm">
                  <i class="fas fa-check text-accent mt-0.5 flex-shrink-0"></i>
                  <span class="text-slate-600 dark:text-slate-400">Proficient in IP subnetting, DHCP/DNS configuration, ACLs, NAT/PAT, and VPN setup</span>
                </li>
              </ul>"""

highlights_new = """<ul class="space-y-4">
                {% for hl in highlights %}
                <li class="flex items-start gap-3 text-sm">
                  <i class="fas fa-check text-accent mt-0.5 flex-shrink-0"></i>
                  <span class="text-slate-600 dark:text-slate-400">{{ hl.text }}</span>
                </li>
                {% endfor %}
              </ul>"""
content = content.replace(highlights_old, highlights_new)

# Statistics
stats_old = """<div class="grid grid-cols-3 gap-4">
              <div class="stat-box">
                <div class="font-display text-3xl font-bold text-accent mb-1">50+</div>
                <div class="text-xs text-slate-500 dark:text-slate-400 font-medium">Endpoints Managed</div>
              </div>
              <div class="stat-box">
                <div class="font-display text-3xl font-bold text-indigo-500 mb-1">10+</div>
                <div class="text-xs text-slate-500 dark:text-slate-400 font-medium">Lab Scenarios Built</div>
              </div>
              <div class="stat-box">
                <div class="font-display text-3xl font-bold text-cyan-500 mb-1">6mo</div>
                <div class="text-xs text-slate-500 dark:text-slate-400 font-medium">Internship Experience</div>
              </div>
            </div>"""

stats_new = """<div class="grid grid-cols-3 gap-4">
              {% for stat in statistics %}
              <div class="stat-box">
                <div class="font-display text-3xl font-bold {{ stat.color_class }} mb-1">{{ stat.value }}</div>
                <div class="text-xs text-slate-500 dark:text-slate-400 font-medium">{{ stat.label }}</div>
              </div>
              {% endfor %}
            </div>"""
content = content.replace(stats_old, stats_new)

email_phone_old = """<div class="flex flex-wrap gap-3 text-sm text-slate-600 dark:text-slate-400">
              <div class="flex items-center gap-2">
                <i class="fas fa-envelope text-accent text-xs"></i>
                sandeepmishrawork@outlook.com
              </div>
              <div class="flex items-center gap-2">
                <i class="fas fa-phone text-accent text-xs"></i>
                +91-xxxxxxxxxx
              </div>
            </div>"""

email_phone_new = """<div class="flex flex-wrap gap-3 text-sm text-slate-600 dark:text-slate-400">
              <div class="flex items-center gap-2">
                <i class="fas fa-envelope text-accent text-xs"></i>
                {{ personal_info.email }}
              </div>
              <div class="flex items-center gap-2">
                <i class="fas fa-phone text-accent text-xs"></i>
                {{ personal_info.phone }}
              </div>
            </div>"""
content = content.replace(email_phone_old, email_phone_new)

# Skills Category Buttons
skills_buttons_old = """<div class="flex flex-wrap justify-center gap-2 mb-10">
          <button class="cat-btn active" data-cat="routing">Routing & Switching</button>
          <button class="cat-btn" data-cat="protocols">Protocols</button>
          <button class="cat-btn" data-cat="tools">Tools & Software</button>
          <button class="cat-btn" data-cat="systems">OS & Systems</button>
        </div>"""

skills_buttons_new = """<div class="flex flex-wrap justify-center gap-2 mb-10">
          {% for cat in skill_categories %}
          <button class="cat-btn {% if cat.is_active_default %}active{% endif %}" data-cat="{{ cat.data_cat }}">{{ cat.name }}</button>
          {% endfor %}
        </div>"""
content = content.replace(skills_buttons_old, skills_buttons_new)

# Skills List
skills_list_old_start = "<!-- Routing & Switching -->"
skills_list_old_end = "<!-- ── PROJECTS ── -->"

# Find boundaries to replace all skills categories
start_idx = content.find(skills_list_old_start)
end_idx = content.find(skills_list_old_end)

skills_list_new = """{% for cat in skill_categories %}
        <div class="skill-cat {% if cat.is_active_default %}active{% endif %}" data-cat="{{ cat.data_cat }}">
          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4">
            {% for skill in cat.skills.all %}
            <div class="skill-card"><i class="{{ skill.icon_class }} text-3xl {{ skill.icon_color_class }} mb-3"></i><h4 class="font-semibold text-sm mb-1">{{ skill.name }}</h4>{% if skill.level %}<p class="text-xs text-slate-400">{{ skill.level }}</p>{% endif %}</div>
            {% endfor %}
          </div>
        </div>
        {% endfor %}

      </div>
    </section>

    """

content = content[:start_idx] + skills_list_new + content[end_idx:]

# Projects
projects_old_start = """<div class="grid md:grid-cols-2 gap-6">"""
projects_old_end = """<!-- ── CONTACT ── -->"""

start_idx = content.find(projects_old_start)
end_idx = content.find(projects_old_end)

projects_new = """<div class="grid md:grid-cols-2 gap-6">
          {% for project in projects %}
          <div class="project-card group">
            <div class="h-44 bg-gradient-to-br {{ project.gradient_from }} {{ project.gradient_to }} flex items-center justify-center border-b border-slate-100 dark:border-slate-800 relative overflow-hidden">
              <div class="absolute inset-0 opacity-10" style="background-image: repeating-linear-gradient(0deg, transparent, transparent 20px, rgba(37,99,235,0.3) 20px, rgba(37,99,235,0.3) 21px), repeating-linear-gradient(90deg, transparent, transparent 20px, rgba(37,99,235,0.3) 20px, rgba(37,99,235,0.3) 21px);"></div>
              <i class="{{ project.icon_class }} text-7xl {{ project.icon_color_class }} relative z-10"></i>
            </div>
            <div class="p-6">
              {% if not project.duration_text %}
              <h3 class="font-display font-bold text-lg mb-2">{{ project.title }}</h3>
              {% else %}
              <div class="flex items-center gap-2 mb-2">
                <h3 class="font-display font-bold text-lg">{{ project.title }}</h3>
              </div>
              {% endif %}
              <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed mb-4">
                {{ project.description }}
              </p>
              <div class="flex flex-wrap gap-2 mb-5">
                {% for tag in project.tags.all %}
                <span class="tag">{{ tag.name }}</span>
                {% endfor %}
              </div>
              {% if project.duration_text %}
              <span class="inline-flex items-center gap-2 text-sm font-semibold text-green-600 dark:text-green-400">
                <i class="fas fa-calendar-alt"></i> {{ project.duration_text }}
              </span>
              {% endif %}
              {% if project.github_link %}
              <a href="{{ project.github_link }}" target="_blank" rel="noopener noreferrer"
                 class="inline-flex items-center gap-2 text-sm font-semibold text-accent hover:underline">
                <i class="fab fa-github"></i> View on GitHub
              </a>
              {% endif %}
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </section>

    """

content = content[:start_idx] + projects_new + content[end_idx:]

# Contact Section
contact_boxes_old = """<div class="grid md:grid-cols-3 gap-6 mb-10">
          <div class="stat-box flex flex-col items-center gap-3">
            <div class="w-11 h-11 bg-blue-50 dark:bg-blue-950/50 rounded-xl flex items-center justify-center">
              <i class="fas fa-envelope text-accent"></i>
            </div>
            <div class="text-center">
              <div class="text-xs text-slate-400 mb-1 font-medium uppercase tracking-wide">Email</div>
              <div class="text-sm font-medium text-slate-700 dark:text-slate-300">sandeepmishrawork@outlook.com</div>
            </div>
          </div>
          <div class="stat-box flex flex-col items-center gap-3">
            <div class="w-11 h-11 bg-indigo-50 dark:bg-indigo-950/50 rounded-xl flex items-center justify-center">
              <i class="fas fa-phone text-indigo-500"></i>
            </div>
            <div class="text-center">
              <div class="text-xs text-slate-400 mb-1 font-medium uppercase tracking-wide">Phone</div>
              <div class="text-sm font-medium text-slate-700 dark:text-slate-300">?</div>
            </div>
          </div>
          <div class="stat-box flex flex-col items-center gap-3">
            <div class="w-11 h-11 bg-cyan-50 dark:bg-cyan-950/50 rounded-xl flex items-center justify-center">
              <i class="fas fa-map-marker-alt text-cyan-500"></i>
            </div>
            <div class="text-center">
              <div class="text-xs text-slate-400 mb-1 font-medium uppercase tracking-wide">Location</div>
              <div class="text-sm font-medium text-slate-700 dark:text-slate-300">New Delhi, India</div>
            </div>
          </div>
        </div>"""

contact_boxes_new = """<div class="grid md:grid-cols-3 gap-6 mb-10">
          <div class="stat-box flex flex-col items-center gap-3">
            <div class="w-11 h-11 bg-blue-50 dark:bg-blue-950/50 rounded-xl flex items-center justify-center">
              <i class="fas fa-envelope text-accent"></i>
            </div>
            <div class="text-center">
              <div class="text-xs text-slate-400 mb-1 font-medium uppercase tracking-wide">Email</div>
              <div class="text-sm font-medium text-slate-700 dark:text-slate-300">{{ personal_info.email }}</div>
            </div>
          </div>
          <div class="stat-box flex flex-col items-center gap-3">
            <div class="w-11 h-11 bg-indigo-50 dark:bg-indigo-950/50 rounded-xl flex items-center justify-center">
              <i class="fas fa-phone text-indigo-500"></i>
            </div>
            <div class="text-center">
              <div class="text-xs text-slate-400 mb-1 font-medium uppercase tracking-wide">Phone</div>
              <div class="text-sm font-medium text-slate-700 dark:text-slate-300">{{ personal_info.phone }}</div>
            </div>
          </div>
          <div class="stat-box flex flex-col items-center gap-3">
            <div class="w-11 h-11 bg-cyan-50 dark:bg-cyan-950/50 rounded-xl flex items-center justify-center">
              <i class="fas fa-map-marker-alt text-cyan-500"></i>
            </div>
            <div class="text-center">
              <div class="text-xs text-slate-400 mb-1 font-medium uppercase tracking-wide">Location</div>
              <div class="text-sm font-medium text-slate-700 dark:text-slate-300">{{ personal_info.location }}</div>
            </div>
          </div>
        </div>"""

content = content.replace(contact_boxes_old, contact_boxes_new)

# Footer info
content = content.replace("Sandeep Mishra · All rights reserved", "{{ personal_info.name }} · All rights reserved")
content = content.replace("Network Engineer · Delhi, India", "{{ personal_info.job_title }} · {{ personal_info.location }}")

# Footer Social Links
footer_social_old = """<div class="flex items-center gap-4">
            <a href="https://linkedin.com/in/sandeepmishraofficial" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-700 text-slate-400 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-linkedin"></i></a>
            <a href="https://github.com/sandeepmishraofficial" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-700 text-slate-400 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-github"></i></a>
            <a href="https://twitter.com/Sandeep_code" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-700 text-slate-400 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-twitter"></i></a>
            <a href="https://instagram.com/sandeepmishra._" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-700 text-slate-400 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-instagram"></i></a>
          </div>"""

footer_social_new = """<div class="flex items-center gap-4">
            {% if personal_info.linkedin_url %}<a href="{{ personal_info.linkedin_url }}" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-700 text-slate-400 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-linkedin"></i></a>{% endif %}
            {% if personal_info.github_url %}<a href="{{ personal_info.github_url }}" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-700 text-slate-400 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-github"></i></a>{% endif %}
            {% if personal_info.twitter_url %}<a href="{{ personal_info.twitter_url }}" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-700 text-slate-400 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-twitter"></i></a>{% endif %}
            {% if personal_info.instagram_url %}<a href="{{ personal_info.instagram_url }}" target="_blank" class="w-9 h-9 flex items-center justify-center rounded-full border border-slate-700 text-slate-400 hover:text-accent hover:border-accent transition-colors text-sm"><i class="fab fa-instagram"></i></a>{% endif %}
          </div>"""
content = content.replace(footer_social_old, footer_social_new)

# Typed.js strings
typed_old = 'strings: ["Network Engineer", "Infrastructure Builder"],'
typed_new = 'strings: "{{ personal_info.typed_text_strings }}".split(",").map(s => s.trim()),'
content = content.replace(typed_old, typed_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
