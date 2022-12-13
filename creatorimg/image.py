from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import shuffle
def createimg(kasbnomi,kasbnarxi,kompaniya):
    imgList = ['creatorimg/img/img1.jpg', 'creatorimg/img/img2.jpg', 'creatorimg/img/img3.jpg', 'creatorimg/img/img4.jpg']
    shuffle(imgList)

    img1 = Image.open('creatorimg/template.jpg')
    img2 = Image.open(imgList[0])


    mask = Image.new('L', img2.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((20,1,280,270), fill=255)

    img1.paste(img2, (210, 250), mask)
    # Call draw Method to add 2D graphics in an image


    I1 = ImageDraw.Draw(img1)

    jobName = kasbnomi
    jobPrice = kasbnarxi
    companyName = kompaniya

    jobNameFont = ImageFont.truetype('creatorimg/Poppins-Bold.ttf', 80)
    jobPriceFont = ImageFont.truetype('creatorimg/Poppins-Bold.ttf', 120)
    companyNameFont = ImageFont.truetype('creatorimg/Poppins-Bold.ttf', 50)

    # Add Text to an image
    I1.text((220, 610), jobName, font=jobNameFont, fill =('white'))
    I1.text((220, 730), f"{jobPrice}", font=jobPriceFont, fill =('springgreen'))
    I1.text((300, 932), companyName, font=companyNameFont, fill =('white'))

    # Display edited image
    # img1.show()

    # Save the edited image
    img1.save("creatorimg/result.png", format='png')
    return True
createimg(str('full stack dev').title(),'500$','idealproject.uz')