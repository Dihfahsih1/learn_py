import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageOps

def remove_background():
    input_path = filedialog.askopenfilename(title='Select Input Image', filetypes=[('Image Files', '*.png *.jpg *.jpeg')])
    if not input_path:
        return
    # Get the directory path of the selected image
    directory = '/'.join(input_path.split('/')[:-1])
    try:
        input_image = Image.open(input_path).convert('RGBA')
        
        # Process the image to remove the background
        output_image = remove_bg(input_image)
        
        # Use the same file name as the original image, but with a "_bg_removed" suffix
        file_name = input_path.split('/')[-1]
        output_path = directory + '/' + file_name.split('.')[0] + '_bg_removed.png'
        
        output_image.save(output_path)
        print('Background removed successfully! Saved at:', output_path)
    except Exception as e:
        print('Error occurred during background removal:', str(e))

def remove_bg(image):
    # Create a mask of the image based on transparency
    alpha_mask = image.split()[3]
    
    # Invert the mask
    inverted_mask = ImageOps.invert(alpha_mask)
    
    # Apply the inverted mask to the original image
    background_removed = image.copy()
    background_removed.putalpha(inverted_mask)
    
    return background_removed

root = tk.Tk()
root.title('Background Removal Tool')

btn_select = tk.Button(root, text='Select Image', command=remove_background)
btn_select.pack(pady=10)

root.mainloop()
