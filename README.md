# iqsms_py3

API REST interface migrated to python3, original python2 version [here](https://iqsms.ru/api/api_rest-python/)


### Simple usage 

```python
from iqsms import Gate

sender = Gate('your_login', 'your_password')
   
print(sender.credits()) # current credits
print(sender.senders()) # all senders
print(sender.send('71234567890', 'some text here', 'iqsms')) #sending sms
```