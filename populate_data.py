import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from core.models import PersonalInfo, AboutCard, Highlight, Statistic, SkillCategory, Skill, ProjectTag, Project

def populate():
    # Personal Info
    PersonalInfo.objects.all().delete()
    PersonalInfo.objects.create(
        name="Sandeep Mishra",
        job_title="Network Engineer",
        typed_text_strings="Network Engineer, Infrastructure Builder",
        description="Networking professional with hands-on experience in LAN/WAN infrastructure, routing & switching, and network troubleshooting. Passionate about building reliable, scalable networks.",
        cv_link="https://drive.google.com/file/d/1-nPnIcGA29diiEJPiFO1zfLGNtCYu9YI/view",
        email="sandeepmishrawork@outlook.com",
        phone="+91-xxxxxxxxxx",
        location="New Delhi, India",
        linkedin_url="https://linkedin.com/in/sandeepmishraofficial",
        github_url="https://github.com/sandeepmishraofficial",
        twitter_url="https://twitter.com/Sandeep_code",
        instagram_url="https://instagram.com/sandeepmishra._",
        status_label="Available for opportunities",
        open_to_work=True,
        experience_summary="6+ months experience",
        education_summary="BCA — Graduating 2025"
    )

    # About Cards
    AboutCard.objects.all().delete()
    AboutCard.objects.create(
        title="Network Engineer",
        icon_class="fas fa-network-wired",
        icon_color_class="text-accent",
        border_color_code="",
        bg_color_class="bg-blue-50 dark:bg-blue-950/50",
        description="Configuring and maintaining routers, switches, and LAN/WAN infrastructure. Skilled in Cisco IOS, VLANs, and STP.",
        order=1
    )
    AboutCard.objects.create(
        title="Routing & Protocols",
        icon_class="fas fa-route",
        icon_color_class="text-indigo-500",
        border_color_code="#6366f1",
        bg_color_class="bg-indigo-50 dark:bg-indigo-950/50",
        description="Hands-on with OSPF, EIGRP, BGP, static routing, and inter-VLAN routing for enterprise topologies.",
        order=2
    )
    AboutCard.objects.create(
        title="Network Monitoring",
        icon_class="fas fa-traffic-light",
        icon_color_class="text-cyan-500",
        border_color_code="#0891b2",
        bg_color_class="bg-cyan-50 dark:bg-cyan-950/50",
        description="Analyzing traffic with Wireshark, identifying anomalies, packet loss, and connectivity issues across endpoints.",
        order=3
    )

    # Highlights
    Highlight.objects.all().delete()
    highlights = [
        "6+ months hands-on experience in network configuration and troubleshooting across 50+ endpoints",
        "Configured OSPF, EIGRP routing and VLANs in enterprise lab environments using GNS3 & Cisco Packet Tracer",
        "Built multi-layer enterprise network topologies simulating real-world infrastructure in home lab",
        "Certified in Networking Fundamentals (Coding Seekho Institute) and Python (HackerRank)",
        "Proficient in IP subnetting, DHCP/DNS configuration, ACLs, NAT/PAT, and VPN setup"
    ]
    for i, h in enumerate(highlights):
        Highlight.objects.create(text=h, order=i+1)

    # Statistics
    Statistic.objects.all().delete()
    Statistic.objects.create(value="50+", label="Endpoints Managed", color_class="text-accent", order=1)
    Statistic.objects.create(value="10+", label="Lab Scenarios Built", color_class="text-indigo-500", order=2)
    Statistic.objects.create(value="6mo", label="Internship Experience", color_class="text-cyan-500", order=3)

    # Skills
    SkillCategory.objects.all().delete()
    Skill.objects.all().delete()
    
    cat1 = SkillCategory.objects.create(name="Routing & Switching", data_cat="routing", is_active_default=True, order=1)
    Skill.objects.create(category=cat1, name="Cisco IOS", icon_class="fas fa-microchip", icon_color_class="text-accent", level="", order=1)
    Skill.objects.create(category=cat1, name="VLANs", icon_class="fas fa-project-diagram", icon_color_class="text-indigo-500", level="Advanced", order=2)
    Skill.objects.create(category=cat1, name="STP", icon_class="fas fa-sitemap", icon_color_class="text-cyan-500", level="Intermediate", order=3)
    Skill.objects.create(category=cat1, name="ACLs", icon_class="fas fa-shield-alt", icon_color_class="text-blue-500", level="Advanced", order=4)
    Skill.objects.create(category=cat1, name="Inter-VLAN Routing", icon_class="fas fa-exchange-alt", icon_color_class="text-green-500", level="Advanced", order=5)
    Skill.objects.create(category=cat1, name="Port Security", icon_class="fas fa-lock", icon_color_class="text-orange-500", level="Intermediate", order=6)
    Skill.objects.create(category=cat1, name="NAT / PAT", icon_class="fas fa-random", icon_color_class="text-purple-500", level="Advanced", order=7)
    Skill.objects.create(category=cat1, name="EtherChannel", icon_class="fas fa-network-wired", icon_color_class="text-red-400", level="Beginner", order=8)

    cat2 = SkillCategory.objects.create(name="Protocols", data_cat="protocols", order=2)
    Skill.objects.create(category=cat2, name="OSPF", icon_class="fas fa-route", icon_color_class="text-accent", level="Advanced", order=1)
    Skill.objects.create(category=cat2, name="EIGRP", icon_class="fas fa-arrows-alt", icon_color_class="text-indigo-500", level="Intermediate", order=2)
    Skill.objects.create(category=cat2, name="BGP", icon_class="fas fa-globe", icon_color_class="text-blue-500", level="Beginner", order=3)
    Skill.objects.create(category=cat2, name="DHCP", icon_class="fas fa-server", icon_color_class="text-cyan-500", level="Advanced", order=4)
    Skill.objects.create(category=cat2, name="DNS", icon_class="fas fa-search", icon_color_class="text-green-500", level="Advanced", order=5)
    Skill.objects.create(category=cat2, name="TCP / IP", icon_class="fas fa-ethernet", icon_color_class="text-orange-500", level="Expert", order=6)
    Skill.objects.create(category=cat2, name="VPN / IPSec", icon_class="fas fa-key", icon_color_class="text-purple-500", level="Intermediate", order=7)
    Skill.objects.create(category=cat2, name="SNMP", icon_class="fas fa-broadcast-tower", icon_color_class="text-red-400", level="Beginner", order=8)

    cat3 = SkillCategory.objects.create(name="Tools & Software", data_cat="tools", order=3)
    Skill.objects.create(category=cat3, name="Cisco Packet Tracer", icon_class="fas fa-desktop", icon_color_class="text-accent", level="Expert", order=1)
    Skill.objects.create(category=cat3, name="GNS3", icon_class="fas fa-cubes", icon_color_class="text-indigo-500", level="Advanced", order=2)
    Skill.objects.create(category=cat3, name="Wireshark", icon_class="fas fa-chart-bar", icon_color_class="text-cyan-500", level="Advanced", order=3)
    Skill.objects.create(category=cat3, name="PuTTY", icon_class="fas fa-terminal", icon_color_class="text-green-500", level="Expert", order=4)
    Skill.objects.create(category=cat3, name="VMware", icon_class="fas fa-hdd", icon_color_class="text-orange-500", level="Intermediate", order=5)
    Skill.objects.create(category=cat3, name="MS Visio", icon_class="fas fa-object-group", icon_color_class="text-purple-500", level="Intermediate", order=6)
    Skill.objects.create(category=cat3, name="ServiceNow", icon_class="fas fa-ticket-alt", icon_color_class="text-blue-500", level="Intermediate", order=7)
    Skill.objects.create(category=cat3, name="Python (Basic)", icon_class="fab fa-python", icon_color_class="text-yellow-500", level="Beginner", order=8)

    cat4 = SkillCategory.objects.create(name="OS & Systems", data_cat="systems", order=4)
    Skill.objects.create(category=cat4, name="Windows 10/11", icon_class="fab fa-windows", icon_color_class="text-accent", level="Expert", order=1)
    Skill.objects.create(category=cat4, name="Windows Server", icon_class="fas fa-server", icon_color_class="text-indigo-500", level="Advanced", order=2)
    Skill.objects.create(category=cat4, name="Ubuntu Linux", icon_class="fab fa-linux", icon_color_class="text-orange-500", level="Intermediate", order=3)
    Skill.objects.create(category=cat4, name="Active Directory", icon_class="fas fa-users-cog", icon_color_class="text-cyan-500", level="Intermediate", order=4)
    Skill.objects.create(category=cat4, name="IP Subnetting", icon_class="fas fa-network-wired", icon_color_class="text-green-500", level="Expert", order=5)
    Skill.objects.create(category=cat4, name="Cable Management", icon_class="fas fa-plug", icon_color_class="text-purple-500", level="Intermediate", order=6)

    # Projects
    ProjectTag.objects.all().delete()
    Project.objects.all().delete()

    t_gns3 = ProjectTag.objects.create(name="GNS3")
    t_ospf = ProjectTag.objects.create(name="OSPF")
    t_vlans = ProjectTag.objects.create(name="VLANs")
    t_vpn = ProjectTag.objects.create(name="VPN")
    t_wireshark = ProjectTag.objects.create(name="Wireshark")
    t_lanwan = ProjectTag.objects.create(name="LAN/WAN")
    t_servicenow = ProjectTag.objects.create(name="ServiceNow")
    t_qos = ProjectTag.objects.create(name="QoS")
    t_ipplanning = ProjectTag.objects.create(name="IP Planning")

    p1 = Project.objects.create(
        title="Enterprise Network Home Lab",
        description="Designed a multi-layer enterprise topology in GNS3 with routers, multilayer switches, DHCP/DNS servers, and client machines. Implemented OSPF, EIGRP, VLAN segmentation, STP loop prevention, and site-to-site VPN. Documented findings in structured lab reports.",
        icon_class="fas fa-network-wired",
        icon_color_class="text-accent/60",
        gradient_from="from-blue-50 dark:from-blue-950/40",
        gradient_to="to-indigo-50 dark:to-indigo-950/40",
        github_link="https://github.com/sandeepmishraofficial/",
        duration_text="",
        order=1
    )
    p1.tags.add(t_gns3, t_ospf, t_vlans, t_vpn, t_wireshark)

    p2 = Project.objects.create(
        title="Internship — Humming Byte Technologies",
        description="Configured and maintained routers and switches across 20+ nodes. Administered VLAN, ACL, and DHCP/DNS setup. Documented network changes and troubleshooting reports in ServiceNow. Implemented QoS policies and assisted in IP planning.",
        icon_class="fas fa-building",
        icon_color_class="text-green-400/70",
        gradient_from="from-green-50 dark:from-green-950/40",
        gradient_to="to-teal-50 dark:to-teal-950/40",
        github_link="",
        duration_text="2024 – 2025 · 6 Months",
        order=2
    )
    p2.tags.add(t_lanwan, t_servicenow, t_qos, t_ipplanning)

    print("Data populated successfully!")

if __name__ == '__main__':
    populate()
