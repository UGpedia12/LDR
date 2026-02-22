"""
Tests for the ATS Resume Generator.

Run with: python -m pytest test_resume_generator.py
or simply: python test_resume_generator.py
"""

import os
import tempfile
from resume_generator import (
    ATSResumeGenerator,
    PersonalInfo,
    Experience,
    Education,
    Project,
    ResumeData,
    create_sample_resume
)


def test_personal_info_creation():
    """Test PersonalInfo data class creation."""
    pi = PersonalInfo(
        name="Test User",
        email="test@example.com",
        phone="123-456-7890"
    )
    assert pi.name == "Test User"
    assert pi.email == "test@example.com"
    assert pi.phone == "123-456-7890"
    assert pi.location is None


def test_experience_creation():
    """Test Experience data class creation."""
    exp = Experience(
        title="Engineer",
        company="Test Corp",
        location="NYC",
        start_date="Jan 2020",
        end_date="Dec 2020",
        responsibilities=["Task 1", "Task 2"]
    )
    assert exp.title == "Engineer"
    assert len(exp.responsibilities) == 2


def test_education_creation():
    """Test Education data class creation."""
    edu = Education(
        degree="BS Computer Science",
        institution="Test University",
        location="Boston",
        graduation_date="May 2019"
    )
    assert edu.degree == "BS Computer Science"
    assert edu.institution == "Test University"


def test_project_creation():
    """Test Project data class creation."""
    proj = Project(
        name="Test Project",
        description="A test project",
        technologies=["Python", "JavaScript"]
    )
    assert proj.name == "Test Project"
    assert len(proj.technologies) == 2


def test_resume_data_creation():
    """Test ResumeData creation with default values."""
    pi = PersonalInfo(
        name="Test",
        email="test@test.com",
        phone="123"
    )
    resume = ResumeData(personal_info=pi)
    assert resume.personal_info.name == "Test"
    assert resume.experience == []
    assert resume.skills == []


def test_sample_resume_creation():
    """Test that sample resume is created successfully."""
    resume = create_sample_resume()
    assert resume.personal_info.name == "John Doe"
    assert len(resume.experience) > 0
    assert len(resume.skills) > 0
    assert resume.summary is not None


def test_txt_generation():
    """Test text resume generation."""
    resume = create_sample_resume()
    generator = ATSResumeGenerator(resume)
    txt = generator.generate_txt()
    
    # Check that key sections are present
    assert "JOHN DOE" in txt
    assert "PROFESSIONAL SUMMARY" in txt
    assert "SKILLS" in txt
    assert "PROFESSIONAL EXPERIENCE" in txt
    assert "EDUCATION" in txt
    assert "john.doe@email.com" in txt


def test_txt_save():
    """Test saving resume as text file."""
    resume = create_sample_resume()
    generator = ATSResumeGenerator(resume)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "test_resume.txt")
        generator.save_txt(filepath)
        
        assert os.path.exists(filepath)
        
        with open(filepath, 'r') as f:
            content = f.read()
            assert "JOHN DOE" in content
            assert len(content) > 0


def test_minimal_resume():
    """Test resume with only required fields."""
    pi = PersonalInfo(
        name="Minimal User",
        email="min@test.com",
        phone="555-0000"
    )
    resume = ResumeData(personal_info=pi)
    generator = ATSResumeGenerator(resume)
    txt = generator.generate_txt()
    
    assert "MINIMAL USER" in txt
    assert "min@test.com" in txt
    assert "555-0000" in txt


def test_resume_with_all_sections():
    """Test resume with all optional sections filled."""
    resume = create_sample_resume()
    generator = ATSResumeGenerator(resume)
    txt = generator.generate_txt()
    
    # Verify all sections are present
    sections = [
        "PROFESSIONAL SUMMARY",
        "SKILLS",
        "PROFESSIONAL EXPERIENCE",
        "PROJECTS",
        "EDUCATION",
        "CERTIFICATIONS"
    ]
    
    for section in sections:
        assert section in txt, f"Section '{section}' not found in resume"


def test_pdf_generation():
    """Test PDF generation (requires reportlab)."""
    try:
        import reportlab
        resume = create_sample_resume()
        generator = ATSResumeGenerator(resume)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "test_resume.pdf")
            generator.generate_pdf(filepath)
            
            assert os.path.exists(filepath)
            assert os.path.getsize(filepath) > 0
            print("✓ PDF generation test passed")
    except ImportError:
        print("⚠ Skipping PDF test - reportlab not installed")


def test_special_characters_in_text():
    """Test handling of special characters."""
    pi = PersonalInfo(
        name="José García",
        email="jose@example.com",
        phone="555-1234"
    )
    resume = ResumeData(
        personal_info=pi,
        summary="Expert in AI/ML & data science"
    )
    generator = ATSResumeGenerator(resume)
    txt = generator.generate_txt()
    
    # Name is uppercased in the resume, check both possible encodings
    # (UTF-8 with accents or ASCII without)
    assert "JOSÉ GARCÍA" in txt.upper() or "JOSE GARCIA" in txt.upper()
    assert "AI/ML" in txt


def run_all_tests():
    """Run all tests and report results."""
    test_functions = [
        test_personal_info_creation,
        test_experience_creation,
        test_education_creation,
        test_project_creation,
        test_resume_data_creation,
        test_sample_resume_creation,
        test_txt_generation,
        test_txt_save,
        test_minimal_resume,
        test_resume_with_all_sections,
        test_pdf_generation,
        test_special_characters_in_text
    ]
    
    passed = 0
    failed = 0
    
    print("Running tests...\n")
    
    for test_func in test_functions:
        try:
            test_func()
            print(f"✓ {test_func.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"✗ {test_func.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__}: {type(e).__name__}: {e}")
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Tests passed: {passed}/{passed + failed}")
    if failed > 0:
        print(f"Tests failed: {failed}/{passed + failed}")
        return False
    else:
        print("All tests passed!")
        return True


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
