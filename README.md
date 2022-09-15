# ASIFT pairwise sequential image matching

## Contents
There is the main script in this repo:

`cross-matching.py` : runs a sequential pairwise comparison of images with the ASIFT model.

## What do we get?
Images are processed and converted to B&W and PNG format before being transferred to [ASIFT](http://www.ipol.im/pub/art/2011/my-asift/).
For each pair of images (img1.png, img2.png) you will get:

1. **imgOutVert_{img1 index}_{img2 index}.png**, **imgOutHori_{img1 index}_{img2 index}.png**: 
Output images (vertical/horizontal concatenated). The detected matches are connected by write lines.

2. **matchings_{img1 index}_{img2 index}.txt**: The file format starts with 1 integer giving the total number of matches. Then each line specifies the coordinates (col1, row1, col2, row2) of a pair of matched points. (col: horizontal axis, from left to right. row: vertical axis, from top to bottom.)

3. **img1.png.txt**, **img2.png.txt**: ASIFT keypoints in the two images, in the same format as the SIFT keypoints of David Lowe. The file starts with 2 integers giving the total number of keypoints and the length of the descriptor vector for each keypoint (128). Then the location of each keypoint in the image is specified by 4 floating point numbers giving subpixel column and row location, scale, and orientation (in radians from -PI to PI). Finally, the invariant descriptor vector for the keypoint is given as a list of 128 integers in range [0,255]. 

### Run the demo:

Run the demo on the default images from table-dataset:

```sh
cross-matching.py
```


#### Additional useful command line parameters
* Use `--images_folder_input` to change the path to folder with the input images.
* Use `--images_folder_output` o change the path to folder with the output images (`B&W` and format to `PNG`).
* Use `--matchings_images_folder` to change the path to folder with output images of pairs with matches.
* Use `--keys_folder_output` to change the path to folder with output text files with image key points.
* Use `--matchings_folder_output` to change the path to the folder with output text files with matching key points of each image pair.

Run the demo on images from gerrard-hall-dataset:

```sh
 cross-matching.py --images_folder_input \assets\gerrard_hall\ --images_folder_output \assets\gerrard_hall_output\img\ 
--matchings_images_folder \assets\gerrard_hall_output\matchings_images\ --keys_folder_output \assets\gerrard_hall_output\keypoints\ 
--matchings_folder_output \assets\gerrard_hall_output\matchings\
```

