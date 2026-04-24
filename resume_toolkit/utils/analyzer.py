"""
analyzer.py — Resume structure and quality analyzer.
Scores a resume based on sections, contact info, length, and bullet usage.
No external API required – pure Python rule-based analysis.
"""
import re


# Section detection patterns (section header keywords)
SECTION_PATTERNS = {
    'contact':        [r'contact', r'reach me', r'get in touch'],
    'summary':        [r'\bsummary\b', r'\bobjective\b', r'\bprofile\b', r'about me', r'\boverview\b', r'career goal'],
    'experience':     [r'experience', r'work history', r'employment', r'professional background', r'career history'],
    'education':      [r'education', r'academic', r'qualification', r'\bdegree\b', r'university', r'college', r'school'],
    'skills':         [r'\bskills\b', r'technical skills', r'core competencies', r'expertise', r'technologies', r'proficiencies'],
    'projects':       [r'\bprojects?\b', r'personal projects', r'academic projects', r'portfolio'],
    'certifications': [r'certif', r'certificates?', r'\bawards?\b', r'achievements?', r'accomplishments?', r'honors?'],
    'languages':      [r'languages?', r'spoken languages?', r'linguistic'],
    'volunteer':      [r'volunteer', r'community', r'social work'],
    'publications':   [r'publications?', r'research', r'papers?', r'articles?'],
}

# Contact information regex patterns
CONTACT_PATTERNS = {
    'email':    r'\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b',
    'phone':    r'(\+?\d[\d\s\-()\[\].]{6,}\d)',
    'linkedin': r'linkedin\.com/in/[\w\-]+',
    'github':   r'github\.com/[\w\-]+',
    'website':  r'https?://(?!linkedin|github)[\w.\-/]+',
}

# Keywords that signal strong impact bullet points
IMPACT_WORDS = [
    'achieved', 'built', 'created', 'designed', 'developed', 'delivered', 'drove',
    'engineered', 'improved', 'implemented', 'increased', 'launched', 'led', 'managed',
    'optimized', 'reduced', 'scaled', 'shipped', 'streamlined', 'transformed',
    '%', 'percent', '$', 'million', 'thousand', 'users', 'revenue', 'growth', 'team',
]


def _score_band(value, low, high, low_score=5, mid_score=15, high_score=20):
    if low <= value <= high:
        return high_score
    elif value < low:
        ratio = value / low if low > 0 else 0
        return max(low_score, int(ratio * mid_score))
    else:  # value > high
        overshoot = (value - high) / high if high > 0 else 0
        return max(low_score, int(mid_score - overshoot * mid_score))


def analyze_resume(text: str) -> dict:
    """
    Analyze resume text and return a structured scoring report.
    Returns a dict with score, section breakdown, contact info, suggestions.
    """
    text_lower = text.lower()
    lines = [l for l in text.split('\n') if l.strip()]
    words = text.split()
    word_count = len(words)

    # ── Section detection ────────────────────────────────────────────────────
    sections_found = {}
    for section, patterns in SECTION_PATTERNS.items():
        sections_found[section] = any(re.search(p, text_lower) for p in patterns)

    # ── Contact info detection ───────────────────────────────────────────────
    contact_found = {}
    for ctype, pattern in CONTACT_PATTERNS.items():
        match = re.search(pattern, text, re.IGNORECASE)
        contact_found[ctype] = bool(match)

    # ── Metrics ─────────────────────────────────────────────────────────────
    bullet_lines = [l for l in lines if re.match(r'^\s*[-•*·◦▪▸►✓✔→]\s', l)]
    bullet_count = len(bullet_lines)

    impact_count = sum(
        1 for line in bullet_lines
        if any(kw.lower() in line.lower() for kw in IMPACT_WORDS)
    )

    # Quantified achievements (lines with numbers/%)
    quantified = sum(
        1 for line in bullet_lines
        if re.search(r'\d+\s*(%|percent|\$|k\b|million|users|team|months?|years?)', line, re.IGNORECASE)
    )

    # ── Sub-scores (out of 100 total) ────────────────────────────────────────
    # Sections present (max 35)
    important_sections = ['summary', 'experience', 'education', 'skills']
    nice_sections      = ['projects', 'certifications', 'contact']
    imp_found  = sum(sections_found.get(s, False) for s in important_sections)
    nice_found = sum(sections_found.get(s, False) for s in nice_sections)
    section_score = int((imp_found / len(important_sections)) * 25 + (nice_found / len(nice_sections)) * 10)

    # Contact completeness (max 15)
    contact_score = int((sum(contact_found.values()) / len(contact_found)) * 15)

    # Word count (max 20): ideal 350–700
    word_score = _score_band(word_count, 350, 700, low_score=5, mid_score=15, high_score=20)

    # Bullet points (max 15): ideal 8–25
    bullet_score = _score_band(bullet_count, 8, 25, low_score=3, mid_score=10, high_score=15)

    # Impact/quantified language (max 15): ideal 3+
    impact_score = min(15, int((impact_count / max(bullet_count, 1)) * 15))

    total_score = min(100, section_score + contact_score + word_score + bullet_score + impact_score)

    # ── Suggestions ──────────────────────────────────────────────────────────
    suggestions = []
    if not sections_found.get('summary'):
        suggestions.append({'icon': '📝', 'text': 'Add a concise professional summary at the top (2-3 lines).'})
    if not sections_found.get('skills'):
        suggestions.append({'icon': '⚡', 'text': 'Add a dedicated Skills section listing your core technologies.'})
    if not sections_found.get('projects'):
        suggestions.append({'icon': '🚀', 'text': 'Add a Projects section to showcase real-world work.'})
    if not sections_found.get('certifications'):
        suggestions.append({'icon': '🏆', 'text': 'Include certifications or awards to stand out.'})
    if not contact_found.get('email'):
        suggestions.append({'icon': '📧', 'text': 'Your email address is missing or hard to detect.'})
    if not contact_found.get('linkedin'):
        suggestions.append({'icon': '🔗', 'text': 'Add your LinkedIn profile URL.'})
    if not contact_found.get('github'):
        suggestions.append({'icon': '💻', 'text': 'Add your GitHub URL to demonstrate your coding activity.'})
    if word_count < 300:
        suggestions.append({'icon': '📏', 'text': f'Resume is too short ({word_count} words). Aim for 350–700 words.'})
    if word_count > 900:
        suggestions.append({'icon': '✂️', 'text': f'Resume is too long ({word_count} words). Trim to under 700 for most roles.'})
    if bullet_count < 5:
        suggestions.append({'icon': '🔸', 'text': 'Use more bullet points to list achievements and responsibilities.'})
    if quantified == 0 and bullet_count > 0:
        suggestions.append({'icon': '📊', 'text': 'Add quantified achievements (e.g., "Improved speed by 40%").'})
    if not suggestions:
        suggestions.append({'icon': '🌟', 'text': 'Excellent resume! Well structured and comprehensive.'})

    # ── Score grade ──────────────────────────────────────────────────────────
    if total_score >= 85:
        grade, grade_color = 'A', '#22c55e'
    elif total_score >= 70:
        grade, grade_color = 'B', '#84cc16'
    elif total_score >= 55:
        grade, grade_color = 'C', '#f59e0b'
    elif total_score >= 40:
        grade, grade_color = 'D', '#f97316'
    else:
        grade, grade_color = 'F', '#ef4444'

    return {
        'total_score':    total_score,
        'grade':          grade,
        'grade_color':    grade_color,
        'section_score':  section_score,
        'contact_score':  contact_score,
        'word_score':     word_score,
        'bullet_score':   bullet_score,
        'impact_score':   impact_score,
        'sections_found': sections_found,
        'contact_found':  contact_found,
        'word_count':     word_count,
        'line_count':     len(lines),
        'bullet_count':   bullet_count,
        'impact_count':   impact_count,
        'quantified':     quantified,
        'suggestions':    suggestions,
    }
