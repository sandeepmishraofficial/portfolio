"""
views.py — Resume Toolkit views.
Handles: Resume Analysis, ATS Score, Editor, Converter.
"""
import io
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .utils.extractor import extract_text
from .utils.analyzer  import analyze_resume
from .utils.scorer    import calculate_ats_score
from .utils.converter import pdf_to_docx, docx_to_pdf


def index(request):
    """Resume Toolkit landing page."""
    return render(request, 'resume_toolkit/index.html')


# ── Resume Analysis ────────────────────────────────────────────────────────────

def analyze(request):
    """Upload resume → get analysis report."""
    if request.method == 'POST':
        resume_file = request.FILES.get('resume')
        if not resume_file:
            return render(request, 'resume_toolkit/analyze.html',
                          {'error': 'Please upload a PDF or DOCX resume file.'})
        try:
            file_content  = resume_file.read()
            resume_text   = extract_text(file_content, resume_file.name)
            if len(resume_text.strip()) < 50:
                return render(request, 'resume_toolkit/analyze.html',
                              {'error': 'Could not extract enough text from the file. Please try a different file.'})
            analysis = analyze_resume(resume_text)
            return render(request, 'resume_toolkit/analyze.html', {
                'analysis':     analysis,
                'resume_text':  resume_text[:3000],  # preview cap
                'filename':     resume_file.name,
            })
        except Exception as e:
            return render(request, 'resume_toolkit/analyze.html', {'error': str(e)})

    return render(request, 'resume_toolkit/analyze.html')


# ── ATS Score ─────────────────────────────────────────────────────────────────

def ats_score(request):
    """Upload resume + job description → get ATS match score."""
    if request.method == 'POST':
        resume_file     = request.FILES.get('resume')
        job_description = request.POST.get('job_description', '').strip()

        errors = []
        if not resume_file:
            errors.append('Please upload a PDF or DOCX resume file.')
        if not job_description:
            errors.append('Please paste a job description.')
        if errors:
            return render(request, 'resume_toolkit/ats_score.html',
                          {'error': ' '.join(errors), 'job_description': job_description})

        try:
            file_content = resume_file.read()
            resume_text  = extract_text(file_content, resume_file.name)
            result       = calculate_ats_score(resume_text, job_description)
            return render(request, 'resume_toolkit/ats_score.html', {
                'result':          result,
                'job_description': job_description,
                'filename':        resume_file.name,
            })
        except Exception as e:
            return render(request, 'resume_toolkit/ats_score.html',
                          {'error': str(e), 'job_description': job_description})

    return render(request, 'resume_toolkit/ats_score.html')


# ── Resume Editor ─────────────────────────────────────────────────────────────

def editor(request):
    """Upload resume → edit in browser → download."""
    if request.method == 'POST':
        action = request.POST.get('action', 'upload')

        # ---- Step 1: Parse the uploaded file ----
        if action == 'upload':
            resume_file = request.FILES.get('resume')
            if not resume_file:
                return render(request, 'resume_toolkit/editor.html',
                              {'error': 'Please upload a PDF or DOCX resume file.'})
            try:
                file_content = resume_file.read()
                resume_text  = extract_text(file_content, resume_file.name)
                return render(request, 'resume_toolkit/editor.html', {
                    'resume_text': resume_text,
                    'filename':    resume_file.name,
                    'editing':     True,
                })
            except Exception as e:
                return render(request, 'resume_toolkit/editor.html', {'error': str(e)})

        # ---- Step 2: Download edited content ----
        elif action == 'download':
            content     = request.POST.get('content', '')
            fmt         = request.POST.get('format', 'txt')

            if fmt == 'txt':
                response = HttpResponse(content, content_type='text/plain; charset=utf-8')
                response['Content-Disposition'] = 'attachment; filename="resume_edited.txt"'
                return response

            elif fmt == 'docx':
                try:
                    from docx import Document
                    from docx.shared import Pt, Inches
                    doc = Document()
                    for section in doc.sections:
                        section.top_margin    = Inches(1)
                        section.bottom_margin = Inches(1)
                        section.left_margin   = Inches(1.1)
                        section.right_margin  = Inches(1.1)
                    style      = doc.styles['Normal']
                    style.font.name = 'Calibri'
                    style.font.size = Pt(11)
                    for line in content.split('\n'):
                        doc.add_paragraph(line)
                    buf = io.BytesIO()
                    doc.save(buf)
                    buf.seek(0)
                    response = HttpResponse(
                        buf.getvalue(),
                        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                    )
                    response['Content-Disposition'] = 'attachment; filename="resume_edited.docx"'
                    return response
                except Exception as e:
                    return render(request, 'resume_toolkit/editor.html',
                                  {'error': str(e), 'resume_text': content, 'editing': True})

            else:
                return render(request, 'resume_toolkit/editor.html',
                              {'error': 'Unknown download format.', 'resume_text': content, 'editing': True})

    return render(request, 'resume_toolkit/editor.html')


# ── Resume Converter ──────────────────────────────────────────────────────────

def converter(request):
    """Convert PDF → DOCX or DOCX → PDF."""
    if request.method == 'POST':
        resume_file = request.FILES.get('resume')
        if not resume_file:
            return render(request, 'resume_toolkit/converter.html',
                          {'error': 'Please upload a PDF or DOCX file.'})

        filename     = resume_file.name
        file_content = resume_file.read()

        try:
            if filename.lower().endswith('.pdf'):
                result_bytes = pdf_to_docx(file_content)
                out_filename = filename.rsplit('.', 1)[0] + '_converted.docx'
                content_type = (
                    'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                )
            elif filename.lower().endswith('.docx'):
                result_bytes = docx_to_pdf(file_content)
                out_filename = filename.rsplit('.', 1)[0] + '_converted.pdf'
                content_type = 'application/pdf'
            else:
                return render(request, 'resume_toolkit/converter.html',
                              {'error': 'Only PDF and DOCX files are supported.'})

            response = HttpResponse(result_bytes, content_type=content_type)
            response['Content-Disposition'] = f'attachment; filename="{out_filename}"'
            return response

        except Exception as e:
            return render(request, 'resume_toolkit/converter.html', {'error': str(e)})

    return render(request, 'resume_toolkit/converter.html')
