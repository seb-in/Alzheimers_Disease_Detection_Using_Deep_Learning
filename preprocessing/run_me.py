import preprocess

input_image = Preprocess()
input_image.strip_the_skull(initial_path,path_to_store_stripped_skull)
input_image.get_noiseless_image(path_to_store_stripped_skull,path_to_store_bias_corrected)
input_image.do_segmentation(path_to_store_bias_corrected,path_to_store_segmented_img)
input_image.return_2D_image(path_to_store_segmented_img,destination_path)
