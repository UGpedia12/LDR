"""
ATS-Compliant Resume Generator

This module provides functionality to generate professional, ATS-compliant resumes
in multiple formats (TXT, PDF) based on structured resume data.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date


@dataclass
class PersonalInfo:
    """Personal information section of the resume."""
    name: str
    email: str
    phone: str
    location: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    website: Optional[str] = None


@dataclass
class Experience:
    """Work experience entry."""
    title: str
    company: str
    location: str
    start_date: str
    end_date: str
    responsibilities: List[str]


@dataclass
class Education:
    """Education entry."""
    degree: str
    institution: str
    location: str
    graduation_date: str
    gpa: Optional[str] = None
    honors: Optional[str] = None


@dataclass
class Project:
    """Project entry."""
    name: str
    description: str
    technologies: List[str]
    url: Optional[str] = None


@dataclass
class ResumeData:
    """Complete resume data structure."""
    personal_info: PersonalInfo
    summary: Optional[str] = None
    experience: List[Experience] = field(default_factory=list)
    education: List[Education] = field(default_factory=list)
    skills: List[str] = field(default_factory=list)
    projects: List[Project] = field(default_factory=list)
    certifications: List[str] = field(default_factory=list)


class ATSResumeGenerator:
    """Generator for ATS-compliant resumes."""
    
    def __init__(self, resume_data: ResumeData):
        """
        Initialize the generator with resume data.
        
        Args:
            resume_data: ResumeData object containing all resume information
        """
        self.data = resume_data
    
    def generate_txt(self) -> str:
        """
        Generate a plain text ATS-compliant resume.
        
        Returns:
            String containing the formatted resume
        """
        lines = []
        
        # Personal Information
        pi = self.data.personal_info
        lines.append(pi.name.upper())
        
        contact_parts = [pi.email, pi.phone]
        if pi.location:
            contact_parts.append(pi.location)
        lines.append(" | ".join(contact_parts))
        
        links = []
        if pi.linkedin:
            links.append(f"LinkedIn: {pi.linkedin}")
        if pi.github:
            links.append(f"GitHub: {pi.github}")
        if pi.website:
            links.append(f"Website: {pi.website}")
        if links:
            lines.append(" | ".join(links))
        
        lines.append("")
        lines.append("=" * 80)
        lines.append("")
        
        # Professional Summary
        if self.data.summary:
            lines.append("PROFESSIONAL SUMMARY")
            lines.append("-" * 80)
            lines.append(self.data.summary)
            lines.append("")
        
        # Skills
        if self.data.skills:
            lines.append("SKILLS")
            lines.append("-" * 80)
            lines.append(", ".join(self.data.skills))
            lines.append("")
        
        # Work Experience
        if self.data.experience:
            lines.append("PROFESSIONAL EXPERIENCE")
            lines.append("-" * 80)
            for exp in self.data.experience:
                lines.append(f"{exp.title} | {exp.company}")
                lines.append(f"{exp.location} | {exp.start_date} - {exp.end_date}")
                for resp in exp.responsibilities:
                    lines.append(f"  • {resp}")
                lines.append("")
        
        # Projects
        if self.data.projects:
            lines.append("PROJECTS")
            lines.append("-" * 80)
            for proj in self.data.projects:
                lines.append(f"{proj.name}")
                lines.append(f"  {proj.description}")
                lines.append(f"  Technologies: {', '.join(proj.technologies)}")
                if proj.url:
                    lines.append(f"  URL: {proj.url}")
                lines.append("")
        
        # Education
        if self.data.education:
            lines.append("EDUCATION")
            lines.append("-" * 80)
            for edu in self.data.education:
                lines.append(f"{edu.degree} | {edu.institution}")
                lines.append(f"{edu.location} | {edu.graduation_date}")
                if edu.gpa:
                    lines.append(f"  GPA: {edu.gpa}")
                if edu.honors:
                    lines.append(f"  {edu.honors}")
                lines.append("")
        
        # Certifications
        if self.data.certifications:
            lines.append("CERTIFICATIONS")
            lines.append("-" * 80)
            for cert in self.data.certifications:
                lines.append(f"  • {cert}")
            lines.append("")
        
        return "\n".join(lines)
    
    def save_txt(self, filename: str):
        """
        Save the resume as a plain text file.
        
        Args:
            filename: Path to save the text file
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.generate_txt())
    
    def generate_pdf(self, filename: str):
        """
        Generate a PDF version of the resume.
        
        Args:
            filename: Path to save the PDF file
        """
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
            from reportlab.lib.enums import TA_LEFT, TA_CENTER
        except ImportError:
            raise ImportError(
                "reportlab is required for PDF generation. "
                "Install it with: pip install reportlab"
            )
        
        doc = SimpleDocTemplate(filename, pagesize=letter,
                                rightMargin=0.75*inch, leftMargin=0.75*inch,
                                topMargin=0.75*inch, bottomMargin=0.75*inch)
        
        story = []
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            textColor='#000000',
            spaceAfter=6,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        contact_style = ParagraphStyle(
            'Contact',
            parent=styles['Normal'],
            fontSize=10,
            alignment=TA_CENTER,
            spaceAfter=12
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=12,
            textColor='#000000',
            spaceAfter=6,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        )
        
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=6
        )
        
        # Personal Information
        pi = self.data.personal_info
        story.append(Paragraph(pi.name.upper(), title_style))
        
        contact_parts = [pi.email, pi.phone]
        if pi.location:
            contact_parts.append(pi.location)
        story.append(Paragraph(" | ".join(contact_parts), contact_style))
        
        links = []
        if pi.linkedin:
            links.append(f"LinkedIn: {pi.linkedin}")
        if pi.github:
            links.append(f"GitHub: {pi.github}")
        if pi.website:
            links.append(f"Website: {pi.website}")
        if links:
            story.append(Paragraph(" | ".join(links), contact_style))
        
        story.append(Spacer(1, 0.2*inch))
        
        # Professional Summary
        if self.data.summary:
            story.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
            story.append(Paragraph(self.data.summary, normal_style))
            story.append(Spacer(1, 0.1*inch))
        
        # Skills
        if self.data.skills:
            story.append(Paragraph("SKILLS", heading_style))
            story.append(Paragraph(", ".join(self.data.skills), normal_style))
            story.append(Spacer(1, 0.1*inch))
        
        # Work Experience
        if self.data.experience:
            story.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))
            for exp in self.data.experience:
                job_title = f"<b>{exp.title}</b> | {exp.company}"
                story.append(Paragraph(job_title, normal_style))
                location_date = f"{exp.location} | {exp.start_date} - {exp.end_date}"
                story.append(Paragraph(location_date, normal_style))
                for resp in exp.responsibilities:
                    story.append(Paragraph(f"• {resp}", normal_style))
                story.append(Spacer(1, 0.1*inch))
        
        # Projects
        if self.data.projects:
            story.append(Paragraph("PROJECTS", heading_style))
            for proj in self.data.projects:
                story.append(Paragraph(f"<b>{proj.name}</b>", normal_style))
                story.append(Paragraph(proj.description, normal_style))
                story.append(Paragraph(f"Technologies: {', '.join(proj.technologies)}", normal_style))
                if proj.url:
                    story.append(Paragraph(f"URL: {proj.url}", normal_style))
                story.append(Spacer(1, 0.1*inch))
        
        # Education
        if self.data.education:
            story.append(Paragraph("EDUCATION", heading_style))
            for edu in self.data.education:
                degree_info = f"<b>{edu.degree}</b> | {edu.institution}"
                story.append(Paragraph(degree_info, normal_style))
                location_date = f"{edu.location} | {edu.graduation_date}"
                story.append(Paragraph(location_date, normal_style))
                if edu.gpa:
                    story.append(Paragraph(f"GPA: {edu.gpa}", normal_style))
                if edu.honors:
                    story.append(Paragraph(edu.honors, normal_style))
                story.append(Spacer(1, 0.1*inch))
        
        # Certifications
        if self.data.certifications:
            story.append(Paragraph("CERTIFICATIONS", heading_style))
            for cert in self.data.certifications:
                story.append(Paragraph(f"• {cert}", normal_style))
        
        doc.build(story)


def create_sample_resume() -> ResumeData:
    """
    Create a sample resume data structure for demonstration.
    
    Returns:
        ResumeData: Sample resume data
    """
    personal_info = PersonalInfo(
        name="John Doe",
        email="john.doe@email.com",
        phone="(555) 123-4567",
        location="San Francisco, CA",
        linkedin="linkedin.com/in/johndoe",
        github="github.com/johndoe"
    )
    
    summary = (
        "Experienced Software Engineer with 5+ years of expertise in full-stack "
        "development, cloud architecture, and agile methodologies. Proven track "
        "record of delivering scalable solutions and leading cross-functional teams "
        "to achieve business objectives."
    )
    
    experience = [
        Experience(
            title="Senior Software Engineer",
            company="Tech Corp",
            location="San Francisco, CA",
            start_date="Jan 2021",
            end_date="Present",
            responsibilities=[
                "Led development of microservices architecture serving 1M+ users",
                "Reduced API response time by 40% through optimization and caching",
                "Mentored team of 5 junior developers in best practices",
                "Implemented CI/CD pipeline reducing deployment time by 60%"
            ]
        ),
        Experience(
            title="Software Engineer",
            company="StartUp Inc",
            location="San Francisco, CA",
            start_date="Jun 2019",
            end_date="Dec 2020",
            responsibilities=[
                "Developed RESTful APIs using Python and FastAPI",
                "Built responsive web applications with React and TypeScript",
                "Collaborated with product team to define technical requirements",
                "Improved test coverage from 60% to 95%"
            ]
        )
    ]
    
    education = [
        Education(
            degree="Bachelor of Science in Computer Science",
            institution="University of Technology",
            location="Boston, MA",
            graduation_date="May 2019",
            gpa="3.8/4.0",
            honors="Summa Cum Laude"
        )
    ]
    
    skills = [
        "Python", "JavaScript", "TypeScript", "React", "Node.js",
        "FastAPI", "Django", "PostgreSQL", "MongoDB", "Docker",
        "Kubernetes", "AWS", "Git", "CI/CD", "Agile/Scrum"
    ]
    
    projects = [
        Project(
            name="Open Source Library",
            description="Created a Python library for data validation with 500+ GitHub stars",
            technologies=["Python", "pytest", "GitHub Actions"],
            url="github.com/johndoe/project"
        )
    ]
    
    certifications = [
        "AWS Certified Solutions Architect - Associate",
        "Certified Scrum Master (CSM)"
    ]
    
    return ResumeData(
        personal_info=personal_info,
        summary=summary,
        experience=experience,
        education=education,
        skills=skills,
        projects=projects,
        certifications=certifications
    )
