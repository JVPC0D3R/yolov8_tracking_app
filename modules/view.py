import numpy as np
import matplotlib.pyplot as plt
import cv2

cmap = plt.get_cmap('Spectral')

colors = [cmap(i)[:3] for i in np.linspace(0, 1, 20)]



def draw_trasnparent_bbox( image, x0, y0, x1, y1, id = 0, thickness = 2, alpha = 0.5):
        
        overlay = image.copy()
        
        color = colors[int(id) % len(colors)]
        color = [i * 255 for i in color]

        cv2.rectangle(overlay, (x0,y0), (x1,y1), color, -1)
        cv2.rectangle(image, (x0,y0), (x1,y1), color, thickness)
            
        cv2.addWeighted(overlay, alpha, image, 1-alpha,0,image)
        

def draw_label( image, text, x0, y0, x1, y1, id = 0, thickness = 2, font_scale = 2.0):

        
        
        color = colors[int(id) % len(colors)]
        color = [i * 255 for i in color]
            
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
        text_x = int(x0 + (x1 - x0 - text_size[0]) // 2)
        text_y = y0 - 10
        cv2.putText(image, text, (text_x, text_y), font, font_scale, color, thickness)


def resize_img(image, scale):
    
    width = int(image.shape[1] * scale / 100)
    height = int(image.shape[0] * scale / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)