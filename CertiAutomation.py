import cv2
import pandas as pd
# The input file contains names as a comma seperated list of format (Rank, User handle, Name)
path_to_input = "/home/bas/event/cert/input/input.xlsx"
participants = pd.read_excel(path_to_input)

template_file_path = "/home/bas/event/cert/Cert.png"

# Make sure this output directory already exists or else certificates won't actually be generated
output_directory_path = "/home/bas/event/cert/output/"

font_size = 1.4
font_color = (51,51,51)

# Test with different values for your particular Template
# This variables determine the exact position where your text will overlay on the template
# Y adjustment determines the px to position above the horizontal center of the template (may be positive or negative)
coordinate_y_adjustment = -80
# X adjustment determiens the px to position to the right of verticial center of the template (may be positive or negative)
coordinate_x_adjustment = 14



for row in participants["Name"]:

	certiName = row
	print(row)
	img = cv2.imread(template_file_path)
	font = cv2.FONT_HERSHEY_SIMPLEX
	text = certiName

	textsize = cv2.getTextSize(text, font, font_size, 7)[0]
	text_x = (img.shape[1] - textsize[0]) / 2 + coordinate_x_adjustment
	text_y = (img.shape[0] + textsize[1]) / 2 - coordinate_y_adjustment
	text_x = int(text_x)
	text_y = int(text_y)
	
	cv2.putText(img, text, (text_x, text_y ), font, font_size, font_color, 3)
	certi_path = output_directory_path + certiName + '.png'
	cv2.imwrite(certi_path,img)
	certiPath = "{}/{}.png".format(output_directory_path, certiName)
	cv2.imwrite(certiPath, img)

cv2.destroyAllWindows()
