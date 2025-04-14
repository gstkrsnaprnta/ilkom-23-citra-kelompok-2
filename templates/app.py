from flask import Flask, request, render_template, jsonify, send_file
import os
from time import time
import logging

# Impor fungsi efek dari modul yang sudah diperbarui
from effects.monochrome_effect import convert_to_grayscale
from effects.line_art_effect import convert_to_line_art
from effects.toon_style_effect import convert_to_toon_style  
from effects.ink_blot_effect import convert_to_ink_blot
from effects.art_sketch_effect import convert_to_art_sketch
from effects.vintage_photo_effect import convert_to_vintage_photo
from effects.resize_image import resize_image

"""
Aplikasi web Sketchify untuk mengubah gambar dengan efek seni seperti sketsa, komik, dan lukisan.
Menerima unggahan gambar, menerapkan efek, dan menyediakan hasil untuk diunduh.
"""