## Refs:
## - https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/

import os, sys, pprint

from flask import Flask, request, flash, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from config import *
from img_proc import *

# TODO: Separate static and template files.
app = Flask(__name__, static_url_path='', static_folder='static_files', template_folder='static_files')
app.config['MAX_CONTENT_LENGTH'] = 512 * 1024 * 1024

# TODO: Better put this in a "config file", and feed it to here and also to index.html
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['SECRET_KEY'] = os.urandom(16)

def is_extension_allowed(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		app.logger.debug("Returning index.html.")
		return render_template("index.html")
	elif request.method == 'POST':
		if 'image_file' not in request.files:
			app.logger.debug("No file")
			# TODO: Flash user
			return redirect(request.url)
		f = request.files['image_file']

		if f is None or f.filename == '':
			app.logger.debug("Empty file.")
			# TODO: Flash user
			return redirect(request.url)

		if not is_extension_allowed(f.filename):
			app.logger.debug("File extension not allowed")
			# TODO: Flash user
			return redirect(request.url)

		filename = secure_filename(f.filename)
		app.logger.debug("filename= %s", filename)
		# TODO: Don't really need to save the file
		f.save(os.path.join(UPLOAD_FOLDER, filename))
		# TODO: Get from the user the width and height to sample rectangles.
		return redirect(url_for('result', filename=filename))

@app.route('/result/<filename>')
def result(filename):
	app.logger.debug("result: started;")

	# resize_img_in_place(filename, width=500, height=500)

	width, height = 200, 200
	xy_pos1, rect1, xy_pos2, rect2 = get_two_random_rects_from_img(filename, width, height)
	app.logger.debug("rect1.shape= {}, rect2.shape= {}".format(rect1.shape, rect2.shape))
	app.logger.debug("xy_pos1= {}, xy_pos2= {}".format(xy_pos1, xy_pos2))

	confusion_matrix = get_confusion_matrix_in_dict(truth_narray=rect1, test_narray=rect2)
	app.logger.debug("confusion_matrix= \n{}".format(pprint.pformat(confusion_matrix)))

	# TODO: Print the random rectangles on the page.

	perc_overlap = get_perc_overlap_between_two_rects(width, height, xy_pos1, xy_pos2)
	app.logger.debug("perc_overlap= \n{}".format(perc_overlap))

	img1_path = save_narray_as_img(rect1, "rect1_from_{}".format(filename))
	app.logger.debug("img1_path= {}".format(img1_path))
	img2_path = save_narray_as_img(rect2, "rect2_from_{}".format(filename))
	app.logger.debug("img2_path= {}".format(img2_path))

	app.logger.debug("result: done.")
	return render_template("index.html",
												 img1_path=img1_path,
												 img2_path=img2_path,
												 confusion_matrix=pprint.pformat(confusion_matrix),
												 perc_overlap=perc_overlap)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
