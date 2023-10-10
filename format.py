#! env python
import img2pdf

imgs = [f"img/{i}.jp2" for i in [1, 296]]

dpix = dpiy = 600
layout_fun = img2pdf.get_fixed_dpi_layout_fun((dpix, dpiy))

with open("b.pdf", "wb") as f:
    f.write(img2pdf.convert(imgs, layout_fun=layout_fun))
