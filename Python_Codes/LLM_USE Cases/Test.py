import win32com.client as win32
import re
from datetime import datetime
from langchain.chains import LLMChain
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
import pandas as pd
import logging
import pythoncom
 
# Initialize logging
logging.basicConfig(filename='email_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def rank_resumes_ollama(job_desc, resumes):
        llm = ChatOllama(
            model="llama3.2:latest",
            temperature=0,
            num_gpu = 0
        )
        prompt_template = PromptTemplate(
            input_variables = ["job_desc", "resume"],
            template = """Match the following job description with the resume and provide a score between 1-100 and also provide the matching reason:
            Job Description:{job_desc}
            Resume:{resume}
            Score:
            Match Reason:"""
        )
        chain = LLMChain(llm=llm, prompt=prompt_template)
 
        scores = []
        match_reason = []
        for resume in resumes:
            response = chain.run({"job_desc": job_desc, "resume": resume})
            score_match = re.search(r'Score:\s*(\d+)', response)
            match_reason_match = re.search(r'Match Reason:\s*(.*)', response)
            if score_match:
                score1 = int(score_match.group(1))
                scores.append(float(score1))  # Convert score to float
            else:
                scores.append(0)  # Assign a default score if no match is found
            if match_reason_match:
                match = score_match.group(1) # type: ignore
                match_reason.append(match)  # Convert score to float
            else:
                match_reason.append(0)  # Assign a default score if no match is found
        return scores, match_reason
df_results_out=pd.DataFrame() 

def send_emails(df):
    try:
        pythoncom.CoInitialize()  # Initialize the COM library
        outlook = win32.Dispatch('outlook.application')
        
        for _, row in df.iterrows():
            mail = outlook.CreateItem(0)
            mail.To = "suman.saha2@wipro.com"  # str(row['Email'])
            mail.Subject = 'Job Opportunity'
            mail.Body = f"Dear Candidate,\n\nWe have reviewed your resume and found it suitable for the following job role:\n\nYour resume score is: {row['Score']}\nMatching Reason: {row['Match Reason']}\n\nBest regards,\nRecruitment Team"
            mail.Send()
            print("Emails sent successfully.")
    except Exception as e:
        logging.error(f"Error sending emails{e}")
        print(f"An error occurred: {e}")

job_description = """Full Stack Java Developer
As a Full Stack Java Developer, you will be responsible for developing and maintaining full-stack applications using Java, Node JS, and other related technologies. You will work on creating and integrating RESTful web services, implementing DevOps practices, and building user interfaces using React JS and Angular 10.
 
Key Responsibilities:
Utilize expertise in Java-J2EE and Full Stack Java Developer to develop and maintain full-stack applications.
Apply advanced knowledge of Node JS to build scalable server-side applications and integrate them with front-end components.
Demonstrate proficiency in JAX-RS - Java API- RESTful Web Services to design and implement RESTful APIs.
Utilize DevOps practices to automate the software development process and improve deployment frequency.
Apply Spring Boot and React JS to build user interfaces and enhance the overall user experience.
 
Qualifications and Skills:
Proficiency in Java-J2EE is essential for this role, with a strong focus on developing scalable and maintainable backend applications.
Advanced knowledge of Node JS is highly desirable, with the ability to build efficient server-side applications and integrate with front-end technologies.
Familiarity with JAX-RS - Java API- RESTful Web Services is beneficial, with the capacity to design and implement RESTful APIs effectively.
Experience in DevOps is advantageous, with the ability to automate software development and deployment processes.
Proficiency in Spring Boot and React JS is preferred, with the capability to build responsive and user-friendly interfaces."""

resumes = """WORK EXPERIENCE
Senior Engineer
Wipro Limited
03/2022 - Present,
Contributing to the Development and enhancement
of new product for client. Strong knowledge of JavaScript with object oriented
programming. Design and development user interfaces using
Angular 8 best practices
Senior Software Engineer
Bytes and Bits Information Technology
05/2019 - 02/2022, https://www.bytesandbits.in/
Involved in Development of multiple Web
applications for various Clients. Created Website Template to be used across various
web applications in the Organization.
Senior Software Engineer
Spring and River Pvt. Ltd. 06/2018 - 05/2019, https://springandriver.com/
Enhancements and maintenance of Client's Business
Web Portal. Created Website Template to be used across various
web applications in the Organization. Member of Technical Staff (Software
Engineer)
Interra Information Technologies (India)
Pvt. Ltd. 07/2014 - 07/2017, https://www.interrait.com/
Responsible for entire scripting workload for Browser
Compatibility Project and resolving large scale
tickets. Responsible for Complete
Development/Testing/Deployment/Support of
Damage Parts Image Upload Project.
SKILLS
ASP.NET MVC ASP.NET Core Angular 8
SQL Server Javascript Jquery GIT
PROJECTS
ICICI Consolidation Application (06/2023 - Present)
Development of application using ASP.NET Core, Angular 8, SQL
Server, GIT, GitHub Copilot
Holmes Third Party Risk Management (TPRM)
(03/2022 - 05/2023)
Development of new product for client and enhancement of existing
functionalities using ASP.NET Core, Angular 8, SQL Server, GIT
Sales Audit Application (04/2021 - 02/2022)
Develop application using ASP.NET Core with Entity Core DB First, SQL server, AngularJS
Truno - Contract Management (03/2021 - 04/2021)
Develop application using ASP.NET Core with Entity Core Code First, SQL server, AngularJS
Vendor Delivery App (01/2020 - 03/2021)
Develop application using ASP.NET Core with Entity Core DB First , SQL server, AngularJS
Lawson Interface and Cross Ref App (05/2019 - 01/2020)
Development and enhancements to the existing web portal using in ASP.NET MVC with ADO.NET, SQL server.
Lucky’s Portal (06/2018 - 05/2019)
Maintenance and enhancements to the existing web portal of Retail stores chain web portal. Worked in ASP.NET MVC with ADO.NET, SQL
server. Mazda - Damaged Parts Img Upload (06/2017 - 07/2017)
Enabling user to upload multiple images of defective goods and
storing the same at a predefined location. Worked in ASP.NET MVC 5, HTML,CSS, JavaScript ,jQuery, AJAX, JSON, MySQL, Deque - Web Accessibility Dev (08/2016 - 06/2017)
Associated in generation of webpage overlays. Worked in Amaze development server, Git, Atom editor, JIRA, NVDA, VoiceOver, JavaScript, jQuery
Mazda - WAS 8.5.5 and Browser Compatibility
(05/2016 - 08/2016)
Associated with delivering critical change requests relating to browser compatibility issues. Worked extensively in JavaScript, jQuery
Loyalty Kiosk (07/2014 - 05/2016)
Associate in development, enhancements and maintenance. Worked"""

scores, match_reasons = rank_resumes_ollama(job_description, resumes)
df = pd.DataFrame({'Resume': resumes, 'Score': scores, 'Match Reason': match_reasons})
df_results_out = pd.concat([df_results_out, df], ignore_index=True)

send_emails(df_results_out)