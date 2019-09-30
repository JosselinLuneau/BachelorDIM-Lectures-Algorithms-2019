
import pytest
import S3_imgproc_tools as S3
import numpy as np

def test_invert_colors_manual_slow():
    img=np.array([[255,255,255], [255, 255, 255]])
    assert (S3.invert_colors_manual_fast(img) == np.array([[0,0,0], [0,0,0]])).prod()

def test_invert_colors_manual_fast():
    img=np.array([[255,255,255], [255, 255, 255]])
    assert (S3.invert_colors_manual_fast(img) == np.array([[0,0,0], [0,0,0]])).prod()
