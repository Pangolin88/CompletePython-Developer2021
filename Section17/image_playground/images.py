from PIL import Image, ImageFilter

img = Image.open('./images/img_04.jpg')


print(img)
print(f'Image format: {img.format}')
print(f'Image size: {img.size}')
print(f'Image mode: {img.mode}')


# filter image
img.filter(ImageFilter.BLUR).save('./output_images/blur_img_04.png', 'png')
img.filter(ImageFilter.SHARPEN).save('./output_images/sharpen_img_04.png', 'png')
img.filter(ImageFilter.SMOOTH).save('./output_images/smooth_img_04.png', 'png')


# convert image
img.convert('L').save('./output_images/grey_img_04.png', 'png')


# show image
# img.show()


# rotate image
img.rotate(90).save('./output_images/rotate_img_04.png', 'png')


# resize
img.resize((200, 200)).save('./output_images/resize_img_04.png', 'png')


# crop image
img.crop((100, 100, 300, 300)).save('./output_images/crop_img_04.png', 'png')


# resize with thumbnail (respect the ratio)
# thumbnail does not return an image, it change the current image
img.thumbnail((200, 200))

