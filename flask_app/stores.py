from flask.ext.uploads import UploadSet, IMAGES

storefronts = UploadSet('storefronts', IMAGES)
item_images = UploadSet('items', IMAGES)
