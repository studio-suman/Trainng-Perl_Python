import win32com.client
import re
from datetime import datetime
from langchain.chains import LLMChain
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
import logging
import pythoncom
 
# Initialize logging
logging.basicConfig(filename='email_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
 
# Initialize Outlook application
pythoncom.CoInitialize()  # Initialize the COM library
outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
 
# Define the folder to monitor (e.g., Inbox)
inbox = namespace.GetDefaultFolder(6)  # 6 refers to the inbox
 
# Define the specific subject to look for
specific_subject = "Congratulations! You have Been Shortlisted for the Position"
 
# Initialize Ollama LLM
llm = ChatOllama(
        model="llama3.2:latest",
        temperature=0
    )

# Create a PromptTemplate instance
prompt_template = PromptTemplate(input_variables=["mail_body"], 
                                 template="Extract the latest occurrence of date and time from the following text: {mail_body}"
                                 ) 

def extract_date_time(mail_body):
    try:
        # Use Langchain and Llama to extract date and time from mail body
        chain = LLMChain(llm=llm, prompt=prompt_template)
        result = chain.run(mail_body=mail_body)
        return result
    except Exception as e:
        logging.error(f"Error extracting date and time: {e}")
        return None
 
def schedule_meeting(date_time_info):
    try:
        # Extract date and time from the result
        date_time_match = re.search(r'([A-Za-z]+, [A-Za-z]+ \d{1,2}, \d{4} \d{1,2}:\d{2} [APM]{2})', date_time_info)
        if date_time_match:
            meeting_date_time = datetime.strptime(date_time_match.group(), '%A, %B %d, %Y %I:%M %p')
 
            # Create a new meeting invite
            appointment = outlook.CreateItem(1)  # 1 refers to the appointment item type
            appointment.Start = meeting_date_time
            appointment.Duration = 60  # Duration in minutes
            appointment.Subject = "Scheduled Meeting"
            appointment.Body = "This is a scheduled meeting based on the email reply."
            appointment.Location = "Online"
            appointment.MeetingStatus = 1  # Set the meeting status to Meeting
 
            # Add required attendees (example email)
            appointment.Recipients.Add("krishnakanth.patil@wipro.com")
 
            # Send the meeting invite
            appointment.Save()
            appointment.Send()
            logging.info(f"Meeting scheduled for {meeting_date_time}")
        else:
            logging.warning("No valid date and time found in the email body.")
    except Exception as e:
        logging.error(f"Error scheduling meeting: {e}")
 
def check_emails():
    try:
        messages = inbox.Items
        messages.Sort("[ReceivedTime]", True)  # Sort emails by received time in descending order
        count = 0
        for message in messages:
            count += 1
            print(count)
            if specific_subject in message.Subject:
                # Check if the message has replies
                if message.ConversationIndex:
                    conversation = message.GetConversation()
                    
                    try:
                            # Get all items in the conversation
                        conversation_items = conversation.GetChildren(message)
                    except Exception as e:
                        print("error getting conversation2")
                        logging.error(f"Error processing conversation items: {e}")
                    # for item in conversation_items:
                    #     print(item)
                    if specific_subject in message.Subject:#and item != message:
                        mail_body = message.Body
                        
                        date_time_info = extract_date_time(mail_body)
                                    
                        if date_time_info:
                            schedule_meeting(date_time_info)
                            print("Mission Success")
                            break
                        
    except Exception as e:
        logging.error(f"Error checking emails: {e}")
 
# Monitor emails and check for replies with specific subject
while True:
    check_emails()