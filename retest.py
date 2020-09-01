from PIL import Image

image = Image.open('data/images/%s.jpg' % (0), 'r')
w = int(image.size[0])
h = int(image.size[1])

print(w)
print(h)