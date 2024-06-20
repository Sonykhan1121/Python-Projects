import qrcode as qr
from PIL import Image
#simple qr_generator
img = qr.make("www.github.com/sonykhan1121")
img.save("mygit_profile.png")






#customize qr_generator

# q = qr.QRCode(version=1,
#                error_correction  = qr.constants.ERROR_CORRECT_H,
#                box_size = 10,
#                border = 4,)
# q.add_data("www.github.com/sonykhan1121")
# q.make(fit = True)
# img = q.make_image(fill_color= "black",back_color= "white")
# img.save("github.png")