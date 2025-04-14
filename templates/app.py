from flask import Flask, request, render_template, jsonify, send_file
import os
from time import time
import logging

# Impor fungsi efek dari modul yang sudah diperbarui
from effects.monochrome_effect import convert_to_grayscale
from effects.line_art_effect import convert_to_line_art
from effects.toon_style_effect import convert_to_toon_style  
from effects.ink_blot_effect import convert_to_ink_blot