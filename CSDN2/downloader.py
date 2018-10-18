import requests
import uuid
from PIL import Image
import shutil

if __name__ == "__main__":
    for i in range(200):
        url = "http://download.csdn.net/index.php/rest/tools/validcode/source_ip_validate/10.5711163911089325"
        response = requests.get(url)
        filename = './captchas/kind2/'+str(uuid.uuid4())+'.png'
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=2048):
                if chunk:
                    f.write(chunk)
                    f.flush()
            f.close()
        im = Image.open(filename)
        Size = im.size
        im.close()
        if Size == (48, 20):
            shutil.move(filename, './captchas/kind1')
