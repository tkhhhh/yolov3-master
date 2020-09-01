from qiniu import Auth, put_data
import requests,time,base64,cv2,os

def api_post(image):
    url_token = 'https://aip.baidubce.com/oauth/2.0/token'
    url_image = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
    with open(image,'rb') as f:
        data = base64.b64encode(f.read())
    param = {
        'client_id':'Qlya48dNvKeHSxqAiIBvv6G5',
        'client_secret': 'pGAgqYPKn1BROX55j7S9hVNgd0VqmWM7',
        'grant_type':'client_credentials'
    }
    response = requests.post(url=url_token,data=param)
    key = response.json()
    access_token = key.get('access_token')
    url_image += '?access_token=' + access_token
    body = {
        'image': str(data,'utf8'),
        'max_face_num': 10,
        'image_type':'BASE64',
        'face_field': 'mask,location'
    }
    header = {
        'Content-Type':'application/json'
    }
    t0 = time.time()
    response = requests.post(url_image,data=body,headers=header)
    key = response.json()
    face_list = key.get('result').get('face_list')
    face = 0
    face_mask = 0
    for tuple in face_list:
        if tuple['mask']['type'] == 0:
            face += 1
        if tuple['mask']['type'] == 1:
            face_mask += 1
    #cv2.imwrite(image,image_x)
    # 绘制预测框
    return time.time()-t0,face,face_mask

if __name__ == "__main__":
    for i in range(1287):
        api_post(str(i)+'.jpg')





