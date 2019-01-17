from aip import AipFace
import base64

""" 你的 APPID AK SK """
APP_ID='15436600'
API_KEY='Nc90b82tqFd18u6di7zpdCXk'
SECRET_KEY='HrniyZl9GEpjWL9jZbFquvwej4evyf1c'

'''创建应用'''
client=AipFace(APP_ID,API_KEY,SECRET_KEY)

'''人脸检测图片参数传入'''
filepath='girl_1.jpg'
with open(filepath,'rb') as f:
    base64_data=base64.b64encode(f.read())
image =str(base64_data,'utf-8')
imageType='BASE64'
""" 如果有可选参数 """
options={}
options['face_field']='age,beauty'
options['max_face_num']=1
options['face_type']='LIVE'
""" 带参数调用人脸检测 """
result=client.detect(image,imageType,options)
print(result)
