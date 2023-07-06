from source.before_after_image import CompareImage
import sys

process = CompareImage()

before_image = sys.argv[1]
after_image = sys.argv[2]

process.start(before_image, after_image)