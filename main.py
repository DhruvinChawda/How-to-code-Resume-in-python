from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.styles import ParagraphStyle

# Create a PDF document
doc = SimpleDocTemplate("resume.pdf", pagesize=letter)

# Set up the document
width, height = letter
styles = getSampleStyleSheet()
title_style = styles["Title"]
normal_style = styles["Normal"]
subheading_style = subheading_style = ParagraphStyle(
    "Subheading",  
    parent=normal_style,  
    fontName="Helvetica-Bold",  
    fontSize=14,  
    textColor="blue", 
    spaceBefore=12,  
    spaceAfter=6, 
)
subheading_style2 = subheading_style2 = ParagraphStyle(
    "Subheading",  
    parent=normal_style,  
    fontName="Helvetica-Bold",  
    fontSize=14,  
    textColor="brown", 
    spaceBefore=12,  
    spaceAfter=6, 
)

# resume content
name = "Name : Radhe Shyam"

about = "As a dedicated and results-driven Club Treasurer, I bring a passion for financial management and a proven track record of ensuring fiscal responsibility within club environments. With a keen eye for detail, I excel in creating and managing budgets, tracking expenses, and providing transparent financial reporting."

Skills = "SKILLS : <br/><br/>1) Financial management <br/> 2)Attention to Detail <br/> 3) Budgeting and Forecasting <br/> 4)Tableau and powerBi <br/> 5) C Python <br/> 6) HTML CSS JAVASCRIPT REACT.JS"

Education = "EDUCATION : <br/><br/>CSE DATA SCIENCE 3RD YEAR<br/>CGPA : 8<br/><br/>HONORS<br/>(WEB DEVELOPMENT)"

Experience = "EXPERIENCE : <br/><br/>Worked for ITUS Club<br/>(Marketing and interviews)<br/><br/>Student Exchange Program<br/>Coding Platforms : Codechef and codeforces"

Objective = "OBJECTIVE"
Objective1 = "To leverage my financial expertise and meticulous attention to detail as a Club Treasurer, contributing to the effective management of club finances, budget optimization, and strategic financial planning. I am committed to ensuring the club's financial stability and fostering its growth through responsible financial management and creative fundraising initiatives."
#content for the resume
content = []

content.append(Paragraph(name, title_style))
content.append(Spacer(1, 12))
content.append(Paragraph(about, normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph(Skills, subheading_style))
#content.append(Line(width - 100, 0, width - 100, 0.1))  
content.append(Spacer(1, 24))
content.append(Paragraph(Education, subheading_style2))
content.append(Spacer(1, 24))
content.append(Paragraph(Experience,subheading_style))
content.append(Spacer(1,24))
content.append(Paragraph(Objective,title_style))
content.append(Spacer(1, 15))
content.append(Paragraph(Objective1,subheading_style2))


# the PDF document
doc.build(content)

print("Resume generated successfully as 'resume.pdf'")
