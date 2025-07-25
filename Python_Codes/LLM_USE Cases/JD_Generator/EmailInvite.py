from email import message
import win32com.client
import re
from datetime import datetime
from langchain.chains import LLMChain
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
import logging
import pythoncom
from datetime import timedelta
 
# Initialize logging
logging.basicConfig(filename='email_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
 
# Initialize Outlook application
pythoncom.CoInitialize()  # Initialize the COM library
outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
 
# Define the folder to monitor (e.g., Inbox)
inbox = namespace.GetDefaultFolder(6)  # 6 refers to the inbox
 
# Define the specific subject to look for
specific_subject = "RE: Congratulations! You have Been Shortlisted for the Position"
 
# Initialize Ollama LLM
llm = ChatOllama(
        model="llama3.2:latest",
        temperature=0
    )
 
# Create a PromptTemplate instance
prompt_template = PromptTemplate(input_variables=["mail_body"], template="Extract the latest occurrence of date and time from the following text: {mail_body}")
 
def extract_date_time(mail_body):
    try:
        # Use Langchain and Llama to extract date and time from mail body
        chain = LLMChain(llm=llm, prompt=prompt_template)
        result = chain.run(mail_body=mail_body)
        return result
    except Exception as e:
        logging.error(f"Error extracting date and time: {e}")
        return None
 
def schedule_meeting(date_time_info,recipient):
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
            appointment.Recipients.Add(recipient)
 
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
                        #print(conversation_items)
                    except Exception as e:
                        #print("error getting conversation2")
                        logging.error(f"Error processing conversation items: {e}")
                    # for item in conversation_items:
                    #     print(item)
                    if specific_subject == message.Subject and check_sent_emails(message.Sender.Address):#and item != message:
                        mail_body = message.Body
                        mail_sender = message.SenderEmailAddress
                        #print(mail_sender)
                       
                        date_time_info = extract_date_time(mail_body)
                                   
                        if date_time_info:
                            schedule_meeting(date_time_info,mail_sender)
                            #print("Mission Success")
                            break
                       
    except Exception as e:
        logging.error(f"Error checking emails: {e}")
 
# Check sent item to avoid repeated mail to already sent users
# Define the folder to monitor (e.g., Inbox)
sent = namespace.GetDefaultFolder(5)  # 6 refers to the inbox
 
# Define the specific subject to look for
sent_subject = "Scheduled Meeting"
 
def check_sent_emails(sender):
    var = True
    try:
        # Get today's date and the date 8 days ago
        today = datetime.now() # type: ignore
        eight_days_ago = today - timedelta(days=1)
 
        # Filter emails sent in the last 8 days
        smessages = sent.Items
        smessages.Sort("[SentOn]", True)
        smessages = smessages.Restrict("[SentOn] >= '" + eight_days_ago.strftime("%m/%d/%Y %H:%M %p") + "'")
        #messages.Sort("[SentTime]", True)  # Sort emails by received time in descending order
        count = 0
        for smessage in smessages:
            count += 1
            print(count)
            if sent_subject in smessage.Subject and smessage.Receiver == sender:
               var = False
            break
        return var
    except Exception as e:
        logging.error(f"Error checking Sent emails: {e}")
    

# Monitor emails and check for replies with specific subject
while True:
    check_emails()