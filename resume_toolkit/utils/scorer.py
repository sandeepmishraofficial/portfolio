"""
scorer.py — ATS (Applicant Tracking System) keyword scorer.
Compares resume text against a job description using rule-based NLP.
No external API required.
"""
import re
from collections import Counter


# Comprehensive English stop words
STOP_WORDS = {
    'a','an','the','and','or','but','in','on','at','to','for','of','with',
    'by','from','is','are','was','were','be','been','being','have','has',
    'had','do','does','did','will','would','could','should','may','might',
    'shall','can','this','that','these','those','i','we','you','he','she',
    'they','it','its','our','your','their','my','his','her','not','no',
    'all','any','more','most','other','some','such','as','if','then','than',
    'when','where','who','which','what','how','up','out','about','into',
    'through','during','before','after','above','below','between','each',
    'few','both','only','also','just','so','well','very','too','use','used',
    'using','work','working','able','new','good','best','make','made','get',
    'got','take','taken','need','needed','like','same','many','much','own',
    'including','must','strong','etc','per','across','around','over','under',
    'within','without','along','following','across','behind','beyond','plus',
    'except','up','out','around','the','however','therefore','thus','hence',
    'accordingly','consequently','furthermore','moreover','nevertheless',
    'nonetheless','otherwise','rather','instead','indeed','certainly','clearly',
    'obviously','typically','generally','usually','often','sometimes','always',
    'never','ever','already','still','yet','again','once','twice','together',
    'here','there','now','then','today','tomorrow','yesterday','year','month',
    'day','time','way','thing','things','part','parts','point','points','area',
    'areas','level','type','types','kind','kinds','set','sets','group','groups',
    'team','members','key','new','old','high','low','large','small','big',
    'great','long','short','right','left','first','last','next','previous',
    'different','various','several','certain','specific','particular','main',
    'major','minor','full','complete','total','overall','general','special',
    'common','real','sure','true','false','open','close','start','end','keep',
    'help','provide','ensure','support','allow','enable','require','include',
    'develop','create','manage','build','run','write','read','report','review',
    'apply','number','numbers','may','looking','role','position','opportunity',
    'candidate','applicant','qualifications','requirements','responsibilities',
    'join','company','organization','business','industry','field','sector',
}

# Common tech abbreviations that should stay uppercase
TECH_TERMS = {
    'api', 'apis', 'aws', 'gcp', 'sql', 'nosql', 'html', 'css', 'js',
    'ui', 'ux', 'qa', 'ci', 'cd', 'ml', 'ai', 'nlp', 'orm', 'rest',
    'json', 'xml', 'http', 'tcp', 'ip', 'ssh', 'ssl', 'tls', 'jwt',
    'oauth', 'saml', 'sdk', 'ide', 'git', 'svn', 'mvc', 'mvp', 'mvvm',
    'spa', 'pwa', 'ssr', 'csr', 'seo', 'crm', 'erp', 'bi', 'etl', 'elt',
    'crud', 'saas', 'paas', 'iaas', 'devops', 'agile', 'scrum', 'kanban',
}


def _tokenize(text: str):
    """Extract meaningful single-word tokens."""
    text_lower = text.lower()
    # Match: words with optional hyphens, dots, #, + (tech terms like c++, c#, node.js)
    tokens = re.findall(r'\b[a-z][a-z0-9+#.\-]*[a-z0-9]\b|\b[a-z]{2,}\b', text_lower)
    return [t for t in tokens if t not in STOP_WORDS and len(t) > 1]


def _extract_bigrams(tokens):
    """Create bigrams from token list (e.g. 'machine learning', 'project management')."""
    return [f"{tokens[i]} {tokens[i+1]}" for i in range(len(tokens) - 1)]


def _extract_skills_phrases(text: str):
    """Extract multi-word skill phrases (2-3 words) from text."""
    patterns = [
        r'machine learning', r'deep learning', r'natural language processing',
        r'computer vision', r'data science', r'data engineering', r'data analysis',
        r'software development', r'software engineering', r'web development',
        r'mobile development', r'full[- ]?stack', r'front[- ]?end', r'back[- ]?end',
        r'cloud computing', r'version control', r'agile methodology', r'test driven',
        r'object oriented', r'microservices? architecture', r'restful api',
        r'continuous integration', r'continuous deployment', r'infrastructure as code',
        r'problem solving', r'critical thinking', r'team player', r'communication skills',
        r'project management', r'product management', r'stakeholder management',
        r'cross[- ]?functional', r'fast[- ]?paced',
    ]
    found = []
    text_lower = text.lower()
    for pattern in patterns:
        if re.search(pattern, text_lower):
            # Normalize pattern to clean phrase
            found.append(re.sub(r'\[.*?\]|\?|\\', '', pattern).replace('-', ' ').strip())
    return found


def extract_keywords(text: str, top_n: int = 60) -> list:
    """Extract top N keywords from text using frequency analysis."""
    tokens = _tokenize(text)
    bigrams = _extract_bigrams(tokens)
    phrases = _extract_skills_phrases(text)
    all_terms = tokens + bigrams + phrases
    freq = Counter(all_terms)
    # Filter: remove very common single chars and keep relevant terms
    filtered = {k: v for k, v in freq.items() if len(k) > 1}
    return [word for word, _ in Counter(filtered).most_common(top_n)]


def calculate_ats_score(resume_text: str, job_description: str) -> dict:
    """
    Calculate ATS score by comparing resume keywords to job description keywords.
    Returns score, matched/missing keywords, and improvement tips.
    """
    if not job_description.strip():
        return {'error': 'Job description is empty.'}

    jd_keywords  = set(extract_keywords(job_description, top_n=70))
    res_keywords = set(extract_keywords(resume_text,     top_n=120))

    matched = jd_keywords & res_keywords
    missing = jd_keywords - res_keywords

    if not jd_keywords:
        return {'error': 'Could not extract keywords from job description.'}

    raw_score = (len(matched) / len(jd_keywords)) * 100

    # Boost score slightly if resume has strong overall keyword density
    density_bonus = min(10, (len(matched) / max(len(res_keywords), 1)) * 20)
    score = min(100, int(raw_score + density_bonus * 0.3))

    # Sort by frequency in JD (high frequency = more important)
    jd_tokens = _tokenize(job_description)
    jd_freq   = Counter(jd_tokens)

    matched_sorted = sorted(matched, key=lambda k: jd_freq.get(k, 0) + jd_freq.get(k.split()[0], 0), reverse=True)
    missing_sorted = sorted(missing, key=lambda k: jd_freq.get(k, 0) + jd_freq.get(k.split()[0], 0), reverse=True)

    # Score grade
    if score >= 80:
        grade, grade_label = 'A', 'Excellent Match'
        grade_color = '#22c55e'
    elif score >= 65:
        grade, grade_label = 'B', 'Good Match'
        grade_color = '#84cc16'
    elif score >= 50:
        grade, grade_label = 'C', 'Average Match'
        grade_color = '#f59e0b'
    elif score >= 35:
        grade, grade_label = 'D', 'Poor Match'
        grade_color = '#f97316'
    else:
        grade, grade_label = 'F', 'Very Low Match'
        grade_color = '#ef4444'

    # Improvement tips
    tips = []
    top_missing = missing_sorted[:5]
    if top_missing:
        tips.append(f"Add these high-priority keywords: {', '.join(top_missing[:3])}.")
    if score < 50:
        tips.append("Tailor your resume specifically for this job description.")
    if score < 70:
        tips.append("Mirror the exact phrasing from the job description where possible.")
    tips.append("Use keywords naturally in your experience bullet points, not just in a skills list.")

    return {
        'score':            score,
        'grade':            grade,
        'grade_label':      grade_label,
        'grade_color':      grade_color,
        'matched_keywords': matched_sorted[:35],
        'missing_keywords': missing_sorted[:35],
        'matched_count':    len(matched),
        'missing_count':    len(missing),
        'total_jd_kw':      len(jd_keywords),
        'tips':             tips,
    }
