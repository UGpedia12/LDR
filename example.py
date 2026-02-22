#!/usr/bin/env python3
"""
Example usage of the ATS Resume Generator.

This script demonstrates how to create professional, ATS-compliant resumes
using the resume_generator module.
"""

from resume_generator import (
    ATSResumeGenerator,
    PersonalInfo,
    Experience,
    Education,
    Project,
    ResumeData,
    create_sample_resume
)


def main():
    """Generate example resumes in multiple formats."""
    
    # Option 1: Use the sample resume data
    print("Generating sample resume...")
    resume_data = create_sample_resume()
    
    # Option 2: Create custom resume data (uncommented to show how)
    # resume_data = ResumeData(
    #     personal_info=PersonalInfo(
    #         name="Your Name",
    #         email="your.email@example.com",
    #         phone="(123) 456-7890",
    #         location="Your City, State",
    #         linkedin="linkedin.com/in/yourprofile",
    #         github="github.com/yourusername"
    #     ),
    #     summary="Your professional summary here...",
    #     skills=["Skill 1", "Skill 2", "Skill 3"],
    #     experience=[
    #         Experience(
    #             title="Your Job Title",
    #             company="Company Name",
    #             location="City, State",
    #             start_date="Month Year",
    #             end_date="Month Year",
    #             responsibilities=[
    #                 "Responsibility 1",
    #                 "Responsibility 2"
    #             ]
    #         )
    #     ],
    #     education=[
    #         Education(
    #             degree="Your Degree",
    #             institution="University Name",
    #             location="City, State",
    #             graduation_date="Month Year",
    #             gpa="X.X/4.0"
    #         )
    #     ]
    # )
    
    # Create the generator
    generator = ATSResumeGenerator(resume_data)
    
    # Generate text version (most ATS-friendly)
    print("Generating TXT resume...")
    generator.save_txt("resume.txt")
    print("✓ Created: resume.txt")
    
    # Generate PDF version (requires reportlab)
    try:
        print("Generating PDF resume...")
        generator.generate_pdf("resume.pdf")
        print("✓ Created: resume.pdf")
    except ImportError as e:
        print(f"⚠ PDF generation skipped: {e}")
        print("  Install reportlab to enable PDF generation: pip install reportlab")
    
    # Display text version to console
    print("\n" + "=" * 80)
    print("GENERATED RESUME (TXT FORMAT):")
    print("=" * 80)
    print(generator.generate_txt())
    print("=" * 80)
    print("\nResume generation complete!")


if __name__ == "__main__":
    main()
