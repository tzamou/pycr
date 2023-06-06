#PyCR (python code returner)
This is a small test project, mainly the author wants to learn what to upload to pypi.

You can use the method provided by this project to send program messages back and forth to line notify. Many functions are incomplete and will be updated in the future.

##Quick Start
```python
from line_notify import Code_returner
helper = Code_returner(token='[your line notify token]')
helper.send_message(message='test messenge')
helper.send_image(img_path='your_image_path.png',message='test image')
```