#-*- coding: UTF-8 -*-
import arabic_reshaper

import pptx
from pptx import Presentation , text
from pptx.enum.shapes import MSO_SHAPE
import os
from pptx.util import Inches, Pt
from pptx.util import Inches
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE

from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.util import Pt , Cm
from pptx.enum.text import PP_ALIGN
from PIL import Image


l = 4455455454
print str("{:,}".format(float(unicode(l))))