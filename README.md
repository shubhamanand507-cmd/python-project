# python-project
# VIT Bhopal Student Result Management System

# Overview

A Python-based command-line application that automates student result computation according to VIT Bhopal's academic rules. The system calculates pass/fail status, determines supplementary exam eligibility, and generates comprehensive reports for individual students or batches.

# Features

Student Data Management - Name, roll number, and marks storage

Automated Result Calculation - Implements VIT Bhopal's passing rules
Supplementary Exam Detection - Identifies students needing re-exams
Multiple Processing Modes - Single student & batch processing
Comprehensive Reporting - Individual reports + class statistics
Input Validation - Robust error handling and data validation
Rule-based Logic -
Pass individual subject: ≥40 marks

Pass overall: ≥40% total percentage

Special case: Pass with supplementary if failing only one subject with ≥40% overall

# Technologies/Tools Used
Programming Language: Python 3.x

Libraries: Standard Python libraries (os, sys)

Platform: Cross-platform (Windows/macOS/Linux)

Interface: Command-line interface (CLI)

# Steps to Install & Run
Prerequisites
Python 3.6 or higher installed
Command-line terminal access
# Installation Steps
Download the Code
Save the provided Python code as 'result_system.py'
Run the Application : python result_system.py
No Additional Dependencies Required
Uses only Python standard libraries
No external packages to install


# Instructions for Testing
Test Scenario 1: Single Student Processing
Launch the application

Choose Option 1: "Check one student"

Enter student details:

Name: John Doe

Roll Number: VIT001

Input marks for all 5 subjects:

Calculus: 85

Physics: 78

Programming: 92

English: 88

Electronics: 95

Expected Result: Full PASS with high percentage

Test Scenario 2: Supplementary Case
Choose Option 1 again

Enter: Jane Smith, VIT002

Input marks:

Calculus: 65

Physics: 72

Programming: 38 # One subject failed

English: 68

Electronics: 71

Expected Result: PASS with supplementary in Programming

Test Scenario 3: Fail Case
Choose Option 1

Enter: Bob Wilson, VIT003

Input marks:

Calculus: 35 # Failed

Physics: 32 # Failed

Programming: 78

English: 65

Electronics: 70

Expected Result: FAIL (multiple failed subjects)

Test Scenario 4: Batch Processing
Choose Option 2: "Check multiple students"

Process 2-3 students with varying marks

Expected Result: Comprehensive summary report showing statistics

Test Scenario 5: Input Validation
Try entering non-numeric marks

Try marks outside 0-100 range

Expected Result: System should prompt for valid input

Test Scenario 6: Rule Reference
Choose Option 3: "See the rules again"

Expected Result: Clear display of all academic rules

# Expected Outcomes
Accurate result computation based on institutional rules

Clear identification of supplementary requirements

Professional report formatting

Proper error handling for invalid inputs

Useful statistical summaries for batch processing

The system is ready for immediate use after downloading the Python file! 🚀
