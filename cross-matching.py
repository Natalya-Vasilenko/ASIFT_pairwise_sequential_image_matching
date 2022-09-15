import os
import cv2
import argparse

'''
File paths must NOT contain Cyrillic characters.
'''

parser = argparse.ArgumentParser(
        description='ASIFT demo',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
     '--images_folder_input', type=str, default='\\assets\\table\\',
       help='Folder with input images in different formats (not only PNG).')

parser.add_argument(
     '--images_folder_output', type=str, default='\\assets\\table_output\\img\\',
       help='Folder of output images (B&W and PNG format).')

parser.add_argument(
     '--matchings_images_folder', type=str, default='\\assets\\table_output\\matchings_images\\',
       help='Folder of output matchings images.')

parser.add_argument(
     '--keys_folder_output', type=str, default='\\assets\\table_output\\keypoints\\',
       help='Folder of output key points of each image.')

parser.add_argument(
     '--matchings_folder_output', type=str, default='\\assets\\table_output\\matchings\\',
       help='Folder of output the matching key points of each image pair.')

opt = parser.parse_args()
print(opt)

file_path = os.path.abspath(__file__)
demo_path = file_path[:len(file_path) - 18] + '\\demo\\'
images_folder_input = file_path[:len(file_path) - 18] + opt.images_folder_input
images_folder_output = file_path[:len(file_path) - 18] + opt.images_folder_output
matchings_images_folder = file_path[:len(file_path) - 18] + opt.matchings_images_folder
keys_folder_output = file_path[:len(file_path) - 18] + opt.keys_folder_output
matchings_folder_output = file_path[:len(file_path) - 18] + opt.matchings_folder_output
images_names = os.listdir(images_folder_input)

for img_name in images_names:
    img = cv2.imread(images_folder_input + img_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(images_folder_output + img_name[:len(img_name) - 3] + 'png', gray)

images_names = os.listdir(images_folder_output)

for i in range(len(images_names) - 1):
    print(i, '/', len(images_names))
    name_i = images_names[i]
    name_j = images_names[i+1]
    s = f'{demo_path}ASIFT.exe {images_folder_output}{name_i} {images_folder_output}{name_j} ' \
        f'{matchings_images_folder}imgOutVert_{i}_{i+1}.png {matchings_images_folder}imgOutHori_{i}_{i+1}.png ' \
        f'{matchings_folder_output}matchings_{i}_{i+1}.txt {keys_folder_output}{name_i}.txt {keys_folder_output}{name_j}.txt'
    x = os.system(s) # x == 0 if success
    print(x)
    print(s)
    print(name_i, '; ', name_j, '->', i, i+1)
