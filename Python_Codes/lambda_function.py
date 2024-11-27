# Import necessary libraries
from __future__ import absolute_import
import base64
import json
import requests
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type,RetryError
import uuid
import pyaes
from datetime import datetime, timedelta

# Global value 
retry_error_msg = None #return error message in response of retry calls
make_api_call_counter = 0 #counter to keep track of retry calls

# -------------------- Function to make the API call with retry logic--------------------------------
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), retry=retry_if_exception_type((requests.exceptions.Timeout, requests.exceptions.HTTPError)))
def make_api_call(url, headers, EncPay,proxies):
    response = None 
    global make_api_call_counter
    make_api_call_counter += 1  # Increment the make_api_call counter
    print(f"Retry count :  {make_api_call_counter}")
    try:
        response = requests.post(url, headers=headers, data=EncPay, timeout=5,proxies=proxies)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Check if the response content is empty
        if not response.content:
            print("Empty response received")
            return None
        
        # Attempt to parse the response as JSON
        try:
            return response    
        except ValueError as json_err:
            print(f"JSON decode error: {json_err}")
            raise
     
    except requests.exceptions.HTTPError as http_err:
        global retry_error_msg
        print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        if response.status_code in [401,403]:   # type: ignore
            print("Authentication error occurred")
            return response
        elif response is not None:
            retry_error_msg = response.text
        raise
      
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")  # Handle other possible errors
        raise
      
# -------------------- Function to make the API call with retry logic--------------------------------   

# Main function that handles the app's logic
def app_handler(event, context):
    # Generate a random UUID
    random_uuid = str(uuid.uuid4())
    encKey =  random_uuid[0:32]
    
    # Retrieve data from EF app setting
    request_data = event.get('request_data')
    app_setting = event.get('app_settings')

    # Extract the required data from the trigger request
    extDemandId = str(request_data.get('extDemandId')) # Wipro SR No
    varSRNo = extDemandId
    mark_to_external_reason = request_data.get('calibrationData').get('customFields').get('mark_to_external_reason') # Reason for MTE
    varNoofMTEPosition = request_data.get('calibrationData').get('customFields').get('number_of_mte_positions') # Number of MTE positions
    mark_to_external = request_data.get('calibrationData').get('customFields').get('mark_to_external') # mark to external type  
    mte_reporting_manager = request_data.get('calibrationData').get('customFields').get('mte_reporting_manager') # Reporting Manager
    
    # App setting from EF
    sosSecrets = app_setting.get('JWT') # JWT token for SOS
    basicAuth = app_setting.get('basicAuth') # SAP auth for SOS - SAP connection
    IV = app_setting.get('IV') # IV for decryption
    SOSServiceUrlQA = app_setting.get('ServiceUrl') # Environment wise Host name 
    Proxy_EF = app_setting.get('proxy_EF') # Environment wise EF Proxy 

    # Read configuration from config.json
    with open('config.json', 'r') as f:
        config = json.load(f)
    # Correlation ID for SOS transaction
    CID = config['appcode'] + "-" + str(uuid.uuid4())   
    # Proxies for SOS connection from app platform
    proxies = {
      'https' : Proxy_EF
    }

    # Join the multiple reason in the array with a semicolon
    varMTEReason = ';'.join(mark_to_external_reason)
     # Decode Unicode escape sequences
    # varMTEReason = varMTEReason.encode('utf-8').decode('unicode_escape')
    
    # Check the mark to external type
    if len(mark_to_external) > 0:
      varMTEType = mark_to_external[0]
    else:
      varMTEType = ""
      
    # Pass the reporting manager if exists       
    if mte_reporting_manager is not None:
      varMTEReportingManager = mte_reporting_manager.get('value')[0]
    else:
      varMTEReportingManager = "" 
      
    #Push EF data to SAP via SOS
    try:
     url = SOSServiceUrlQA + config['createExternalHire']
     payload = json.dumps({
      "d": {
        "Type": "MARK_TO_EXTERNAL",
        "mark_to_ext": [
          {
            "Type": "MARK_TO_EXTERNAL",
            "INDENT_NUMBER": str(varSRNo),
            "REASON_MARK_EXTERNAL": varMTEReason,  # Join the multiple reason in the array with a semicolon
            "NO_OPENING": varNoofMTEPosition,
            # "REMARKS": "",
            # "PANELIST": "",
            "REPORTING_MANAGER": varMTEReportingManager,
            # "BOAT": "",
            # "FRANCHISE": "",
            "RECRUIT": True if varMTEType == 'Recruit only' or varMTEType == 'Both' else False,
            "CONTRACT": True if varMTEType == 'Contract only' or varMTEType == 'Both' else False,
            # "FTE": "",
            # "RETAINER": "",
            # "CBR_RATE": "",
            # "FTE_RETAINER_DROPDOWN": ""
          }
        ]
      }
    })
     print("MTE payload - " + payload)     
     payload = json.loads(payload)


     headdisp ={
       "Authorization" : sosSecrets,
       "BasicAuth" : encrypt(basicAuth,encKey,IV,"b"),
       "AccessToken" : encKey,
       "Content-Type" : "text/plain",
       "CorrelationId" : CID
     }
     response_mtepush = requests.post(url, headers=headdisp, data=encrypt(payload,encKey,IV,"p"),timeout=30,proxies=proxies)
     print("header ",response_mtepush.headers.get('correlationid'))
     print("status_code : ", response_mtepush.status_code , "response : ", response_mtepush.text)
     if(response_mtepush.status_code !=200):
          print("Json check",is_json(response_mtepush.text))
          if(is_json(response_mtepush.text)):
            stack_trace = json.loads(response_mtepush.text).get('description')
          else:
            stack_trace = json.loads(decrypt(response_mtepush.text,encKey,IV)).get('message')
          data ={
             "statusCode" : response_mtepush.status_code,
             "error" : "Error occured in create external hire push call",
             "stacktrace" : stack_trace,
             "AccessToken" : encKey,
             "CID" : response_mtepush.headers.get('correlationid'),
             "TS" : str(datetime.utcnow()+ timedelta(hours=5, minutes=30))
          }
          return {
            "body" : data
      } 
    except requests.exceptions.ProxyError as proxEr:
     print(f'A proxy error occurred: {proxEr}')
     data={
        "statusCode" : 500,
         "error" : "A proxy Error occured in create external hire push call",
         "stacktrace" : str(proxEr),         
         "TS" : str(datetime.utcnow()+ timedelta(hours=5, minutes=30))
     }
     return {
        "body" : data
     }
    except RetryError as retryerror:
      print(f"make_api_call was called {make_api_call_counter} times in total")
      global retry_error_msg
      if(retry_error_msg is None):
        stacktrace = retryerror
      else:  
        stacktrace = json.loads(decrypt(retry_error_msg,encKey,IV))['message']
        data={
        "statusCode" : 500,
        "error" : "RetryError Error occured in create external hire push call",
        "stacktrace" : str(stacktrace),
        "TS" : str(datetime.utcnow()+ timedelta(hours=5, minutes=30))
        }
      return {
        "body" : data
      }
    except requests.Timeout as timeOuterr:
      print(f'The request timed out at MTE submit: {timeOuterr}')
      data={
         "statusCode" : 500,
         "error" : "The request timed out Error occured in create external hire push call",
         "stacktrace" :  str(timeOuterr),
         "TS" : str(datetime.utcnow()+ timedelta(hours=5, minutes=30))
        }
      return {
          "body" : data
      } 
    except requests.HTTPError as http_err:
     print(f'HTTP error occurred at MTE submit: {http_err}')
     data={
         "statusCode" : 500,
         "error" : "http_err Error occured in create external hire push call",
         "stacktrace" :  str(http_err),
         "TS" : str(datetime.utcnow()+ timedelta(hours=5, minutes=30))
       }
     return {
          "body" : data
      }
    except Exception as err:
     print(f'Other error occurred at MTE submit: {err}')
     data={
         "statusCode" : 500,
         "error" : "Other Error occured in create external hire push call",
         "stacktrace" :  str(err),
         "TS" : str(datetime.utcnow()+ timedelta(hours=5, minutes=30))
       }
     return {
          "body" : data
      }
    else:
      print('Success! in profile submit ' + str(response_mtepush.status_code))
      print("response decrypted : ",json.loads(decrypt(response_mtepush.text,encKey,IV)))      
      submitRes = decrypt(response_mtepush.text,encKey,IV)
      print("submitRes :",(json.loads(submitRes)['status']))
      # ----------Error scenario----------  
      if ((json.loads(submitRes)['status']) != "Success"):
        data = (json.loads(submitRes))['message']
        data = {
          "statusCode" : 500,  
          "error" : "Error occured in create external hire push call",
          "stacktrace" :  "Error : "+ data,
          "CID" : response_mtepush.headers.get('correlationid'),
          "TS" : str(datetime.utcnow()+ timedelta(hours=5, minutes=30))
          }
        return {
            "body" : data
        }
      # ----------Error scenario----------
    
      # ----------Success scenario--------
      else:
        data = (json.loads(submitRes)['status'])
        print("submitRes :",data)
        data = {
          "statusCode": 200,
          "message" : data + " : Created External Hire successfully.",
          "CID" : response_mtepush.headers.get('correlationid'),
          "TS" : str(datetime.utcnow()+ timedelta(hours=5, minutes=30))
          }
        return {
          'body': json.dumps(data)
        }
      # ----------Success scenario--------  

# ------------- AES 256 CBC mode Encryption method ------------------
def encrypt(data, key, iv, op):
  
    # Convert key and iv to bytes
    key = bytes(key, 'utf-8')
    iv = bytes(iv, 'utf-8')
  
    # Message to be encrypted
    if(op == 'p'):
        data = (json.dumps(data))
    else:
        data = data
        
    # We need to pad the plaintext to be a multiple of 16 bytes
    padding_length = 16 - len(data) % 16
  
    # Pad the plaintext to make it a multiple of 16 bytes
    plaintext = data + chr(16 - len(data) % 16) * padding_length
 
    # Convert the plaintext to bytes
    plaintext_bytes = plaintext.encode('utf-8') 
 
    # Break the plaintext into 16-byte blocks
    blocks = [plaintext_bytes[i:i+16] for i in range(0, len(plaintext_bytes), 16)]

    # Create a new AES cipher object with CBC mode
    aes = pyaes.AESModeOfOperationCBC(key, iv = iv)

    # Encrypt each block
    ciphertext_blocks = [aes.encrypt(block) for block in blocks]
 
    # Concatenate the ciphertext blocks to get the final ciphertext
    ciphertext = b''.join(ciphertext_blocks) 
    value = base64.b64encode(ciphertext).decode('utf-8')
    return value
# ------------- AES 256 CBC mode Encryption method ------------------  

# ------------- AES 256 CBC mode Decryptiom method ------------------
def decrypt(encrypted_data, key, iv):
 # Convert key and iv to bytes
 key = bytes(key, 'utf-8')
 iv = bytes(iv, 'utf-8')
 # The ciphertext
 ciphertext = base64.b64decode(encrypted_data)  # Replace 'value' with the actual base64-encoded ciphertext

# Create a new AES cipher object with CBC mode
 aes = pyaes.AESModeOfOperationCBC(key, iv=iv)

# Break the ciphertext into 16-byte blocks
 blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]

# Decrypt each block
 decrypted_blocks = [aes.decrypt(block) for block in blocks]

# Concatenate the decrypted blocks to get the final plaintext
 decrypted_bytes = b''.join(decrypted_blocks)


# Remove the padding
#  padding_length = decrypted_bytes[-1] if decrypted_bytes[-1] < 16 else 0 # fixed as part of decryption issue
 padding_length = decrypted_bytes[-1] if decrypted_bytes[-1] <= 16 else 0
 plaintext_bytes = decrypted_bytes[:-padding_length]

# Convert the bytes to a string
 try:
    plaintext = plaintext_bytes.decode('utf-8')
 except UnicodeDecodeError:
    plaintext = "Decryption failed: The decrypted bytes are not valid UTF-8."

 return plaintext

# ------------- AES 256 CBC mode Encryption method ------------------

# ------------- JSON check -------------------
def is_json(value):
    try:
        json.loads(value)
        return True
    except (ValueError, TypeError):
        return False
# ------------- JSON check -------------------

# Test the app handler lambda function in local
# event = {
  # "request_data": {},
  # "app_settings": {},
  # "trigger_name": "candidate_stage_advance"
# }

# response = app_handler(event, {})
