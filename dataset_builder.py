from VisualDS.Builder import VisualDSBuilder
from xml.etree import ElementTree as et
import cv2
import argparse
import ast

parser = argparse.ArgumentParser(description='Visual Dataset Builder')
parser.add_argument('--xml', help='Path to XML configuration file for building datasets')
args = parser.parse_args()

tree = et.parse(args.xml)
root = tree.getroot()

xmlfile = root.findall('datasetbuilder')
for params in xmlfile:
    frequency = float(params.find('frequency').text)  # This is the path of the configuration file
    dsfolder = params.find('dsfolder').text  # This is the path of where the images will be stored
    videopath = params.find('videopath').text  # Path of the video or camera stream
    width = int(params.find('width').text)  # W of the output saved file
    height = int(params.find('height').text) # H of the output saved file
    colorspace = params.find('colorspace').text 

size = (width, height)
# Dataset Builder
visDS = VisualDSBuilder(frequency, dsfolder, videopath, size, colorspace)  # visual dataset constructor
visDS.run()  # start the dataset builder