# LDR - ATS-Compliant Resume Generator

A Python-based tool for generating professional, ATS (Applicant Tracking System) compliant resumes in multiple formats.

## Features

- ✅ **ATS-Compliant**: Follows best practices for Applicant Tracking Systems
- 📄 **Multiple Formats**: Generate resumes in TXT and PDF formats
- 🎯 **Professional Layout**: Clean, organized sections with proper formatting
- 🔧 **Customizable**: Easy-to-use data structures for personalization
- 📦 **Zero Config**: Works out of the box with sample data

## What is ATS Compliance?

ATS (Applicant Tracking System) compliance means that your resume is formatted in a way that can be easily parsed by automated recruitment software. Key features include:

- Simple, clean formatting without complex tables or graphics
- Standard section headers (Experience, Education, Skills, etc.)
- Proper use of keywords relevant to the job
- Contact information clearly displayed
- Standard fonts and readable structure

## Installation

1. Clone the repository:
```bash
git clone https://github.com/UGpedia12/LDR.git
cd LDR
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

Run the example script to generate a sample resume:

```bash
python example.py
```

This will generate:
- `resume.txt` - Plain text version (most ATS-friendly)
- `resume.pdf` - PDF version (human-readable)

## Usage

### Using the Sample Resume

```python
from resume_generator import ATSResumeGenerator, create_sample_resume

# Create sample resume data
resume_data = create_sample_resume()

# Generate resume
generator = ATSResumeGenerator(resume_data)
generator.save_txt("my_resume.txt")
generator.generate_pdf("my_resume.pdf")
```

### Creating Your Custom Resume

```python
from resume_generator import (
    ATSResumeGenerator,
    PersonalInfo,
    Experience,
    Education,
    ResumeData
)

# Define your personal information
personal_info = PersonalInfo(
    name="Your Name",
    email="your.email@example.com",
    phone="(123) 456-7890",
    location="Your City, State",
    linkedin="linkedin.com/in/yourprofile",
    github="github.com/yourusername"
)

# Add your work experience
experience = [
    Experience(
        title="Software Engineer",
        company="Tech Company",
        location="San Francisco, CA",
        start_date="Jan 2020",
        end_date="Present",
        responsibilities=[
            "Developed scalable web applications",
            "Led team of 3 developers",
            "Improved system performance by 40%"
        ]
    )
]

# Add your education
education = [
    Education(
        degree="Bachelor of Science in Computer Science",
        institution="University Name",
        location="City, State",
        graduation_date="May 2019",
        gpa="3.8/4.0"
    )
]

# Create complete resume data
resume_data = ResumeData(
    personal_info=personal_info,
    summary="Your professional summary here...",
    skills=["Python", "JavaScript", "SQL", "Docker"],
    experience=experience,
    education=education
)

# Generate resume
generator = ATSResumeGenerator(resume_data)
generator.save_txt("resume.txt")
generator.generate_pdf("resume.pdf")
```

## Resume Sections

The generator supports the following resume sections:

1. **Personal Information** (required)
   - Name, email, phone
   - Optional: location, LinkedIn, GitHub, website

2. **Professional Summary** (optional)
   - Brief overview of your professional background

3. **Skills** (optional)
   - List of your technical and professional skills

4. **Professional Experience** (optional)
   - Job title, company, location, dates
   - List of responsibilities and achievements

5. **Projects** (optional)
   - Project name, description, technologies used
   - Optional: project URL

6. **Education** (optional)
   - Degree, institution, location, graduation date
   - Optional: GPA, honors

7. **Certifications** (optional)
   - List of professional certifications

## ATS Best Practices

When creating your resume, follow these tips for maximum ATS compatibility:

1. **Use Standard Section Headers**: Stick to common headers like "Experience", "Education", "Skills"
2. **Include Keywords**: Use industry-relevant keywords from the job description
3. **Avoid Graphics**: Don't use images, charts, or complex formatting
4. **Use Simple Bullets**: Stick to standard bullet points (•)
5. **Choose Standard Fonts**: Use common fonts like Arial, Calibri, or Times New Roman
6. **Save in Multiple Formats**: Provide both TXT (most compatible) and PDF versions
7. **Be Consistent**: Use consistent date formats and styling throughout

## Output Formats

### TXT Format
- Plain text format
- Maximum ATS compatibility
- Can be opened in any text editor
- Recommended for online job applications

### PDF Format
- Professional appearance
- Good for email submissions and printing
- Requires `reportlab` library
- Human-readable with proper formatting

## Requirements

- Python 3.7+
- reportlab (for PDF generation)

## License

This project is open source and available for educational and commercial use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.