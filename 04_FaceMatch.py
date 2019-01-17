from aip import AipFace
import base64

""" 你的 APPID AK SK """
APP_ID='15436600'
API_KEY='Nc90b82tqFd18u6di7zpdCXk'
SECRET_KEY='HrniyZl9GEpjWL9jZbFquvwej4evyf1c'

'''创建应用'''
client=AipFace(APP_ID,API_KEY,SECRET_KEY)

'''
def base64_data(filepath):
    with open(filepath, 'rb') as f:
        return base64.b64encode(f.read())
images=[{'image':base64_data('qiwei.jpg'),'image_type':'BASE64',},{'image':base64_data('yuwenwen.jpg'),'image_type':'BASE64'},]
'''
""" 调用人脸对比 """
result = client.match([
    {
        'image': str(base64.b64encode(open('yuwenwen.jpg', 'rb').read()),'utf-8'),
        'image_type': 'BASE64',
    },
    {
        'image': str(base64.b64encode(open('qiwei_3.jpg', 'rb').read()),'utf-8'),
        'image_type': 'BASE64',
    }
])

#print(result)

"""判断是否为一个人"""
result_score=result['result']['score']

if result_score >= 80:
    print('相似度为%s,完全一个人' % result_score)
elif (result_score >= 60 and result_score < 80):
    print('相似度为%s，可能是同一个人' % result_score)
else:
    print('相似度仅为%s，不是同一个人' % result_score)
