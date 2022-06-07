# Job Status Module
This is for Celonis data jobs status checking application. Contains main.ipynb and main.conf files with code and configurations.
App can be used to check if failed jobs are present in data pools, to check the statuses of all jobs in particular data pools and to check statuses of particulars data jobs. In case of presence of any FAIL status, or requests for data pool or data jobs - application send email to user.

## Working principles
App is built on the basis of Python core libraries, only using smtplib to connect to server for sending emails, email.mime objects to create html template of email, configparser to obtain data from conf file and pycelonis to reach celonis object. 

## Configures
In the main.conf file there are multiple fields that can be changed by user. get_jobs_by_pool_name and get_job_status_by_job_name are for invokation of getting data jobs from particular data pools and getting data jobs by name features. Just assign values for this adding it separated by ','. In case of single request - just put the name of data pool/data job. In case of absence of data pool/data job in knowledge model - user will be notified. Leave fields empty if no need for this request. Failed data jobs are checked automatically, and user shouldn't change anything in configures. If failed jobs are present, or user requested features of getting data jobs/data pools - email notification will be sent. If get_jobs_by_pool_name and get_job_status_by_job_name fields are empty and no failed data jobs are present - email won't be sent.
host_server and host_port - fields for hosting information.
sender_email and sender_password - information on email address and password for user, from whom email notifications will be sent. Please check information inside this fields to prevent login failed error.
receiver_email - email address for user, for whom notification will be sent. In case of many - just add it separated by ','.

### Items for email template
subject - the subject of sending email, default value can be changed to any desired.
hello - the introduction string of email, can be changed from default as well.
failed_jobs_string - this is for displaying failed jobs. Can be changed, just two pairs of {} should be left in template to recognize data pools and data jobs.
jobs_by_pool_string - this is for displaying get_jobs_by_pool_name feature. {} should be left in template to recognize data pool name. Please note, this is displayed as unordered list, so <ul> tag should not be left from template as well.
jobs_by_name_string - this is for displaying get_job_status_by_job_name feature. Please note, this is displayed as unordered list, so <ul> tag should not be left from template as well.
