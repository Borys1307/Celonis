from pycelonis import get_celonis
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser

celonis = get_celonis(threaded=True)
pools_ids = list(celonis.pools.ids.keys())
pools_names = list(celonis.pools.names.keys())


def get_name(dictionary):
    if dictionary['status'] == 'FAIL':
        return dictionary['id']
    return None

def get_jobs_failed():
    data_dict = {}
    for pool in pools_ids:
        a = celonis.pools.find(pool)    
        if not data_dict.get(a.name):
            data_dict[a.name] = []
        failed_list = list(filter(None,list(map(get_name,a.check_data_job_execution_status()))))
        for fail in failed_list:
            data_dict[a.name].append(a.data_jobs.find(fail).name)
    data_dict_1 = {k:v for k,v in data_dict.items() if len(v)>0}
    return data_dict_1
    
    
    
def get_name_status(tuple_dict):    
    return {tuple_dict[0]['name']:tuple_dict[1]['status']}
def get_jobs_status_by_pool_name(pool_name):
    try:
        b = celonis.pools.find(pool_name)         
    except NameError:        
        return pool_name
        
    ac = [{k:v} for k,v in zip(['name','name'],b.data_jobs.names.keys())]    
    aa = list(zip(ac,b.check_data_job_execution_status()))    
    
    res1 = {pool_name : list(map(get_name_status,aa))}
    if res1[pool_name] != []:
        return res1
    else:
        return '666'+pool_name
 
 
 
def get_job_status_by_job_name(name):
    for pool in pools_names:
        b = celonis.pools.find(pool) 
        names = b.data_jobs.names  
        if name in names.keys():
            statuses = b.check_data_job_execution_status()
            idx = names[name].id
            for status in statuses:
                if status['id'] == idx:
                    return {name:status['status']}        
        return name



config = configparser.ConfigParser()
config.read('main.conf')



jobs_by_pool = config['EMAIL']['get_jobs_by_pool_name'].split(',')
jobs_by_pool = list(map(str.strip,jobs_by_pool))
if jobs_by_pool != ['']:
    jobs_by_pool = list(map(get_jobs_status_by_pool_name,jobs_by_pool))
    jobs_by_pool_in = list(filter(lambda x: isinstance(x,dict),jobs_by_pool))
    jobs_by_pool_out = list(filter(lambda x: isinstance(x,str),jobs_by_pool))
length_jobs_by_pool = sum(list(map(len,jobs_by_pool)))*len(jobs_by_pool)
 




jobs_by_name = config['EMAIL']['get_job_status_by_job_name'].split(',')
jobs_by_name = list(map(str.strip,jobs_by_name))
if jobs_by_name != ['']:
    jobs_by_name = list(map(get_job_status_by_job_name,jobs_by_name))
    jobs_by_name_in = list(filter(lambda x: isinstance(x,dict),jobs_by_name))
    jobs_by_name_out = list(filter(lambda x: isinstance(x,str),jobs_by_name))
length_jobs_by_name = sum(list(map(len,jobs_by_name)))*len(jobs_by_name)



failed_jobs = get_jobs_failed()


smtp_server = config['EMAIL']['host_server']
port = int(config['EMAIL']['host_port'])
sender_email = config['EMAIL']['sender_email']
sender_password = config['EMAIL']['sender_password']
receiver_email = config['EMAIL']['receiver_email']
failed_jobs_string = config['EMAIL']['failed_jobs_string']
jobs_by_pool_string = config['EMAIL']['jobs_by_pool_string']
jobs_by_name_string = config['EMAIL']['jobs_by_name_string']
hello = config['EMAIL']['hello']


def create_failed_output(string, dictionary):
    result = ''
    for k, v in dictionary.items():             
        result+= string.format(", ".join(v),k)        
    return result
    
jobs_failed = create_failed_output(failed_jobs_string, failed_jobs)

def jobs_by_name_output(string,list_of_dicts):    
    for job in list_of_dicts:
        key = list(job.keys())[0]
        string+= f'<li>{key} : {job[key]} </li>'
    string+='</ul></p>'
    return string
    
def jobs_by_pool_output(string, list_of_dicts):
    result = ''
    for element in list_of_dicts:
        for k, v in element.items():  
            result+= string.format(k)
            result=jobs_by_name_output(result,v)
            #for dicti in v:
             #   key = list(dicti.keys())[0]
              #  result+=f'<li>{key} : {dicti[key]} </li>'
            #result+='</ul></p>'
    return result    



jobs_in_pools = jobs_by_pool_output(jobs_by_pool_string,jobs_by_pool_in)
jobs_by_names = jobs_by_name_output(jobs_by_name_string,jobs_by_name_in)


def pools_not_in (list_of_strings):
    result = ''
    for string in list_of_strings:
        if string.startswith('666'):
            result1 = '<p>Data Pool <b>{}</b> is not exisitng</p>'
            result+=result1.format(string[3:])
        else:
            result1 = '<p>Data Pool <b>{}</b> does not have exisitng Data Jobs</p>'
            result+=result1.format(string)
    return result



def jobs_not_in (list_of_strings):
    result = ''
    for string in list_of_strings:        
        result1 = '<p>Data Job <b>{}</b> is not exisitng</p>'
        result+=result1.format(string)        
    return result
    
    
    
pools_not = pools_not_in(jobs_by_pool_out)
jobs_not = jobs_not_in(jobs_by_name_out)

hello = 'Hello, please check your status and data jobs requests below'
#failed_jobs_string = f'You have next jobs failed in data pools {failed_jobs}' if len(failed_jobs) > 0 else 'No failed jobs'
#jobs_by_pool_string = f'You have next jobs in data pools {jobs_by_pool}' if jobs_by_pool != [''] else ''
#jobs_by_name_string = f'You have next status of jobs {jobs_by_name}' if jobs_by_name != [''] else ''
mail_content = ('\n').join((hello, jobs_failed, jobs_in_pools, pools_not, jobs_by_names, jobs_not))


message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = hello = config['EMAIL']['subject']   
message.attach(MIMEText(mail_content, 'html'))

def send_email():
    session = smtplib.SMTP(smtp_server, port) 
    session.starttls() 
    session.login(sender_email, sender_password) 
    text = message.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()
    
if result != '' or jobs_by_pool_string != '' or jobs_by_name_string != '':
    send_email()
