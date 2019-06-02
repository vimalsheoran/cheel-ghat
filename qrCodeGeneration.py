import qrcode
from uuid import uuid1
from pytz import timezone 
from datetime import datetime,timedelta

def gettimenow(delta = True):
    india = timezone('Asia/Kolkata')
    if delta == True:
        india = datetime.now(india)
        return(india.strftime('%Y-%m-%d %H:%M:%S'))
    
    india = datetime.now(india) - timedelta(hours=delta)
    return(india.strftime('%Y-%m-%d %H:%M:%S'))



# Create qr code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

# The data that you want to store

data = {
    'poleId':str(uuid1()),
    'loc':"sfv sfj s",
    'ccms':"SMR03-0219-0792",
    'phase':"R"
}
# 'poleId' = 'uuid1())'

data = "http://192.168.43.75:4000."
# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save it somewhere, change the extension as needed:
# img.save("image.png")
# img.save("image.bmp")
# img.save("image.jpeg")
img.save("image.jpg")
