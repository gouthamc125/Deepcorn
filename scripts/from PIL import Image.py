from PIL import Image

# Open the image file
image = Image.open(r'C:\Users\C.GOUTHAM\Desktop\Deepcorn\images\corn\6.png')

# Get the color palette of the image
palette = image.getpalette()

# Print the color palette
print(palette)
