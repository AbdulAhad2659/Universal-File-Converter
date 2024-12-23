import sys
import os
import logging
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QFileDialog, QComboBox, QProgressBar, QVBoxLayout, QHBoxLayout,
                             QMessageBox, QGroupBox, QCheckBox, QTabWidget, QTextEdit, QGridLayout)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from converters.document_converter import DocumentConverter
from converters.image_converter import ImageConverter
from converters.media_converter import MediaConverter
from converters.misc_converter import MiscConverter
from editors.video_editor import VideoEditor
from editors.audio_editor import AudioEditor
from editors.image_editor import ImageEditor
from utils.file_handler import FileHandler
from utils.cloud_integration import GoogleDriveIntegration

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConversionThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)

    def __init__(self, converter, input_path, output_path, conversion_type, options=None):
        super().__init__()
        self.converter = converter
        self.input_path = input_path
        self.output_path = output_path
        self.conversion_type = conversion_type
        self.options = options or {}

    def run(self):
        try:
            if self.conversion_type == 'word_to_pdf':
                DocumentConverter.word_to_pdf(self.input_path, self.output_path)
            elif self.conversion_type == 'pdf_to_word':
                DocumentConverter.pdf_to_word(self.input_path, self.output_path)
            elif self.conversion_type == 'excel_to_pdf':
                DocumentConverter.excel_to_pdf(self.input_path, self.output_path)
            elif self.conversion_type == 'pdf_to_excel':
                DocumentConverter.pdf_to_excel(self.input_path, self.output_path)
            elif self.conversion_type == 'excel_to_word':
                DocumentConverter.excel_to_word(self.input_path, self.output_path)
            elif self.conversion_type == 'word_to_excel':
                DocumentConverter.word_to_excel(self.input_path, self.output_path)
            elif self.conversion_type == 'txt_to_word':
                DocumentConverter.txt_to_word(self.input_path, self.output_path)
            elif self.conversion_type == 'word_to_txt':
                DocumentConverter.word_to_txt(self.input_path, self.output_path)
            elif self.conversion_type == 'csv_to_excel':
                DocumentConverter.csv_to_excel(self.input_path, self.output_path)
            elif self.conversion_type == 'excel_to_csv':
                DocumentConverter.excel_to_csv(self.input_path, self.output_path)
            elif self.conversion_type == 'pdf_to_html':
                DocumentConverter.pdf_to_html(self.input_path, self.output_path)
            elif self.conversion_type == 'pdf_to_md':
                DocumentConverter.pdf_to_md(self.input_path, self.output_path)
            elif self.conversion_type == 'jpeg_to_png':
                ImageConverter.jpeg_to_png(self.input_path, self.output_path)
            elif self.conversion_type == 'png_to_jpeg':
                ImageConverter.png_to_jpeg(self.input_path, self.output_path)
            elif self.conversion_type == 'jpeg_to_bmp':
                ImageConverter.jpeg_to_bmp(self.input_path, self.output_path)
            elif self.conversion_type == 'bmp_to_png':
                ImageConverter.bmp_to_png(self.input_path, self.output_path)
            elif self.conversion_type == 'png_to_webp':
                ImageConverter.png_to_webp(self.input_path, self.output_path)
            elif self.conversion_type == 'webp_to_png':
                ImageConverter.webp_to_png(self.input_path, self.output_path)
            elif self.conversion_type == 'pdf_to_images':
                ImageConverter.pdf_to_images(self.input_path, self.output_path)
            elif self.conversion_type == 'images_to_pdf':
                ImageConverter.images_to_pdf(self.input_path.split(';'), self.output_path)
            elif self.conversion_type == 'mp4_to_mp3':
                MediaConverter.mp4_to_mp3(self.input_path, self.output_path)
            elif self.conversion_type == 'mp3_to_wav':
                MediaConverter.mp3_to_wav(self.input_path, self.output_path)
            elif self.conversion_type == 'wav_to_mp3':
                MediaConverter.wav_to_mp3(self.input_path, self.output_path)
            elif self.conversion_type == 'mp4_to_gif':
                MediaConverter.mp4_to_gif(self.input_path, self.output_path)
            elif self.conversion_type == 'gif_to_mp4':
                MediaConverter.gif_to_mp4(self.input_path, self.output_path)
            elif self.conversion_type == 'avi_to_mp4':
                MediaConverter.avi_to_mp4(self.input_path, self.output_path)
            elif self.conversion_type == 'mp4_to_avi':
                MediaConverter.mp4_to_avi(self.input_path, self.output_path)
            elif self.conversion_type == 'flac_to_mp3':
                MediaConverter.flac_to_mp3(self.input_path, self.output_path)
            elif self.conversion_type == 'mp3_to_flac':
                MediaConverter.mp3_to_flac(self.input_path, self.output_path)
            elif self.conversion_type == 'aac_to_mp3':
                MediaConverter.aac_to_mp3(self.input_path, self.output_path)
            elif self.conversion_type == 'mp3_to_aac':
                MediaConverter.mp3_to_aac(self.input_path, self.output_path)
            elif self.conversion_type == 'json_to_csv':
                MiscConverter.json_to_csv(self.input_path, self.output_path)
            elif self.conversion_type == 'csv_to_json':
                MiscConverter.csv_to_json(self.input_path, self.output_path)
            elif self.conversion_type == 'yaml_to_json':
                MiscConverter.yaml_to_json(self.input_path, self.output_path)
            elif self.conversion_type == 'json_to_yaml':
                MiscConverter.json_to_yaml(self.input_path, self.output_path)
            elif self.conversion_type == 'xml_to_json':
                MiscConverter.xml_to_json(self.input_path, self.output_path)
            elif self.conversion_type == 'json_to_xml':
                MiscConverter.json_to_xml(self.input_path, self.output_path)
            elif self.conversion_type == 'html_to_markdown':
                MiscConverter.html_to_markdown(self.input_path, self.output_path)
            elif self.conversion_type == 'markdown_to_html':
                MiscConverter.markdown_to_html(self.input_path, self.output_path)
            elif self.conversion_type == 'trim_video':
                VideoEditor.trim_video(self.input_path, self.output_path, self.options['start_time'], self.options['end_time'])
            elif self.conversion_type == 'remove_sound':
                VideoEditor.remove_sound(self.input_path, self.output_path)
            elif self.conversion_type == 'merge_videos':
                VideoEditor.merge_videos(self.input_path.split(';'), self.output_path)
            elif self.conversion_type == 'add_audio':
                VideoEditor.add_audio(self.input_path, self.options['audio_path'], self.output_path)
            elif self.conversion_type == 'change_resolution':
                VideoEditor.change_resolution(self.input_path, self.output_path, self.options['new_resolution'])
            elif self.conversion_type == 'add_subtitles':
                VideoEditor.add_subtitles(self.input_path, self.options['srt_path'], self.output_path)
            elif self.conversion_type == 'extract_frames':
                VideoEditor.extract_frames(self.input_path, self.output_path, self.options['frame_times'], self.options['fps'])
            elif self.conversion_type == 'trim_audio':
                AudioEditor.trim_audio(self.input_path, self.output_path, self.options['start_time'], self.options['end_time'])
            elif self.conversion_type == 'remove_noise':
                AudioEditor.remove_noise(self.input_path, self.output_path, self.options['noise_reduction_amount'])
            elif self.conversion_type == 'change_speed':
                AudioEditor.change_speed(self.input_path, self.output_path, self.options['speed_factor'])
            elif self.conversion_type == 'merge_audio_files':
                AudioEditor.merge_audio_files(self.input_path.split(';'), self.output_path)
            elif self.conversion_type == 'extract_audio_from_video':
                AudioEditor.extract_audio_from_video(self.input_path, self.output_path)
            elif self.conversion_type == 'resize_image':
                ImageEditor.resize_image(self.input_path, self.output_path, self.options['size'])
            elif self.conversion_type == 'compress_image':
                ImageEditor.compress_image(self.input_path, self.output_path, self.options['quality'])
            elif self.conversion_type == 'rotate_image':
                ImageEditor.rotate_image(self.input_path, self.output_path, self.options['degrees'])
            elif self.conversion_type == 'flip_image':
                ImageEditor.flip_image(self.input_path, self.output_path, self.options['direction'])
            elif self.conversion_type == 'add_watermark':
                ImageEditor.add_watermark(self.input_path, self.output_path, self.options['watermark_text'], self.options['position'], self.options['font_size'], self.options['font_path'])
            elif self.conversion_type == 'convert_to_grayscale':
                ImageEditor.convert_to_grayscale(self.input_path, self.output_path)

            self.finished.emit("Conversion successful!")
        except Exception as e:
            self.finished.emit(f"Error: {e}")
            logging.error(f"Conversion error: {e}")

class FileConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Universal File Converter and Media Editor")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        self.tabs = QTabWidget()
        self.converter_tab = QWidget()
        self.editor_tab = QWidget()

        self.tabs.addTab(self.converter_tab, "Converter")
        self.tabs.addTab(self.editor_tab, "Media Editor")

        self.initConverterTab()
        self.initEditorTab()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)

        self.show()

    def initConverterTab(self):
        # Input file selection
        self.input_label = QLabel("Input File(s):")
        self.input_edit = QLineEdit()
        self.input_button = QPushButton("Browse")
        self.input_button.clicked.connect(self.browse_input)

        # Output file selection
        self.output_label = QLabel("Output Directory/File:")
        self.output_edit = QLineEdit()
        self.output_button = QPushButton("Browse")
        self.output_button.clicked.connect(self.browse_output)

        # Conversion type selection
        self.conversion_label = QLabel("Conversion Type:")
        self.conversion_combo = QComboBox()
        self.conversion_combo.addItems([
            "word_to_pdf", "pdf_to_word", "excel_to_pdf", "pdf_to_excel",
            "excel_to_word", "word_to_excel", "txt_to_word", "word_to_txt",
            "csv_to_excel", "excel_to_csv", "pdf_to_html", "pdf_to_md",
            "jpeg_to_png", "png_to_jpeg", "jpeg_to_bmp", "bmp_to_png",
            "png_to_webp", "webp_to_png", "pdf_to_images", "images_to_pdf",
            "mp4_to_mp3", "mp3_to_wav", "wav_to_mp3", "mp4_to_gif",
            "gif_to_mp4", "avi_to_mp4", "mp4_to_avi", "flac_to_mp3",
            "mp3_to_flac", "aac_to_mp3", "mp3_to_aac", "json_to_csv",
            "csv_to_json", "yaml_to_json", "json_to_yaml", "xml_to_json",
            "json_to_xml", "html_to_markdown", "markdown_to_html"
        ])

        # Batch processing checkbox
        self.batch_checkbox = QCheckBox("Batch Processing")

        # Cloud integration (Google Drive)
        self.cloud_group = QGroupBox("Cloud Integration")
        self.cloud_checkbox = QCheckBox("Use Google Drive")
        self.authenticate_button = QPushButton("Authenticate")
        self.authenticate_button.clicked.connect(self.authenticate_gdrive)
        cloud_layout = QVBoxLayout()
        cloud_layout.addWidget(self.cloud_checkbox)
        cloud_layout.addWidget(self.authenticate_button)
        self.cloud_group.setLayout(cloud_layout)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)

        # Convert button
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_file)

        # Log display
        self.log_label = QLabel("Log:")
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)

        # Layout
        layout = QGridLayout()
        layout.addWidget(self.input_label, 0, 0)
        layout.addWidget(self.input_edit, 0, 1)
        layout.addWidget(self.input_button, 0, 2)
        layout.addWidget(self.output_label, 1, 0)
        layout.addWidget(self.output_edit, 1, 1)
        layout.addWidget(self.output_button, 1, 2)
        layout.addWidget(self.conversion_label, 2, 0)
        layout.addWidget(self.conversion_combo, 2, 1)
        layout.addWidget(self.batch_checkbox, 3, 0)
        layout.addWidget(self.cloud_group, 3, 1, 1, 2)
        layout.addWidget(self.convert_button, 4, 1)
        layout.addWidget(self.progress_bar, 5, 0, 1, 3)
        layout.addWidget(self.log_label, 6, 0)
        layout.addWidget(self.log_text, 7, 0, 1, 3)

        self.converter_tab.setLayout(layout)

    def initEditorTab(self):
        # Input file selection
        self.editor_input_label = QLabel("Input File(s):")
        self.editor_input_edit = QLineEdit()
        self.editor_input_button = QPushButton("Browse")
        self.editor_input_button.clicked.connect(self.browse_editor_input)

        # Output file selection
        self.editor_output_label = QLabel("Output Directory/File:")
        self.editor_output_edit = QLineEdit()
        self.editor_output_button = QPushButton("Browse")
        self.editor_output_button.clicked.connect(self.browse_editor_output)

        # Editing type selection
        self.editing_label = QLabel("Editing Type:")
        self.editing_combo = QComboBox()
        self.editing_combo.addItems([
            "trim_video", "remove_sound", "merge_videos", "add_audio",
            "change_resolution", "add_subtitles", "extract_frames", "trim_audio",
            "remove_noise", "change_speed", "merge_audio_files", "extract_audio_from_video",
            "resize_image", "compress_image", "rotate_image", "flip_image",
            "add_watermark", "convert_to_grayscale"
        ])

        # Options for editing
        self.options_group = QGroupBox("Editing Options")
        self.options_layout = QGridLayout()
        self.options_group.setLayout(self.options_layout)

        self.editing_combo.currentIndexChanged.connect(self.update_editing_options)

        # Edit button
        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.edit_media)

        # Progress bar
        self.editor_progress_bar = QProgressBar()
        self.editor_progress_bar.setValue(0)

        # Layout
        layout = QGridLayout()
        layout.addWidget(self.editor_input_label, 0, 0)
        layout.addWidget(self.editor_input_edit, 0, 1)
        layout.addWidget(self.editor_input_button, 0, 2)
        layout.addWidget(self.editor_output_label, 1, 0)
        layout.addWidget(self.editor_output_edit, 1, 1)
        layout.addWidget(self.editor_output_button, 1, 2)
        layout.addWidget(self.editing_label, 2, 0)
        layout.addWidget(self.editing_combo, 2, 1)
        layout.addWidget(self.options_group, 3, 0, 1, 3)
        layout.addWidget(self.edit_button, 4, 1)
        layout.addWidget(self.editor_progress_bar, 5, 0, 1, 3)

        self.editor_tab.setLayout(layout)

    def update_editing_options(self):
        # Clear existing options
        for i in reversed(range(self.options_layout.count())):
            self.options_layout.itemAt(i).widget().setParent(None)

        # Get current editing type
        editing_type = self.editing_combo.currentText()

        # Add options based on editing type
        if editing_type == "trim_video" or editing_type == "trim_audio":
            self.start_time_label = QLabel("Start Time (s):")
            self.start_time_edit = QLineEdit()
            self.end_time_label = QLabel("End Time (s):")
            self.end_time_edit = QLineEdit()
            self.options_layout.addWidget(self.start_time_label, 0, 0)
            self.options_layout.addWidget(self.start_time_edit, 0, 1)
            self.options_layout.addWidget(self.end_time_label, 1, 0)
            self.options_layout.addWidget(self.end_time_edit, 1, 1)
        elif editing_type == "add_audio":
            self.audio_path_label = QLabel("Audio File:")
            self.audio_path_edit = QLineEdit()
            self.audio_path_button = QPushButton("Browse")
            self.audio_path_button.clicked.connect(self.browse_audio_path)
            self.options_layout.addWidget(self.audio_path_label, 0, 0)
            self.options_layout.addWidget(self.audio_path_edit, 0, 1)
            self.options_layout.addWidget(self.audio_path_button, 0, 2)
        elif editing_type == "change_resolution":
            self.resolution_label = QLabel("New Resolution (WxH):")
            self.resolution_edit = QLineEdit()
            self.options_layout.addWidget(self.resolution_label, 0, 0)
            self.options_layout.addWidget(self.resolution_edit, 0, 1)
        elif editing_type == "add_subtitles":
            self.srt_path_label = QLabel("SRT File:")
            self.srt_path_edit = QLineEdit()
            self.srt_path_button = QPushButton("Browse")
            self.srt_path_button.clicked.connect(self.browse_srt_path)
            self.options_layout.addWidget(self.srt_path_label, 0, 0)
            self.options_layout.addWidget(self.srt_path_edit, 0, 1)
            self.options_layout.addWidget(self.srt_path_button, 0, 2)
        elif editing_type == "extract_frames":
            self.frame_times_label = QLabel("Frame Times (s, comma-separated):")
            self.frame_times_edit = QLineEdit()
            self.fps_label = QLabel("Or, FPS:")
            self.fps_edit = QLineEdit()
            self.options_layout.addWidget(self.frame_times_label, 0, 0)
            self.options_layout.addWidget(self.frame_times_edit, 0, 1)
            self.options_layout.addWidget(self.fps_label, 1, 0)
            self.options_layout.addWidget(self.fps_edit, 1, 1)
        elif editing_type == "remove_noise":
            self.noise_reduction_label = QLabel("Noise Reduction Amount:")
            self.noise_reduction_edit = QLineEdit()
            self.options_layout.addWidget(self.noise_reduction_label, 0, 0)
            self.options_layout.addWidget(self.noise_reduction_edit, 0, 1)
        elif editing_type == "change_speed":
            self.speed_factor_label = QLabel("Speed Factor:")
            self.speed_factor_edit = QLineEdit()
            self.options_layout.addWidget(self.speed_factor_label, 0, 0)
            self.options_layout.addWidget(self.speed_factor_edit, 0, 1)
        elif editing_type == "resize_image":
            self.size_label = QLabel("New Size (WxH):")
            self.size_edit = QLineEdit()
            self.options_layout.addWidget(self.size_label, 0, 0)
            self.options_layout.addWidget(self.size_edit, 0, 1)
        elif editing_type == "compress_image":
            self.quality_label = QLabel("Quality (0-100):")
            self.quality_edit = QLineEdit()
            self.options_layout.addWidget(self.quality_label, 0, 0)
            self.options_layout.addWidget(self.quality_edit, 0, 1)
        elif editing_type == "rotate_image":
            self.degrees_label = QLabel("Degrees:")
            self.degrees_edit = QLineEdit()
            self.options_layout.addWidget(self.degrees_label, 0, 0)
            self.options_layout.addWidget(self.degrees_edit, 0, 1)
        elif editing_type == "flip_image":
            self.direction_label = QLabel("Direction (horizontal/vertical):")
            self.direction_edit = QLineEdit()
            self.options_layout.addWidget(self.direction_label, 0, 0)
            self.options_layout.addWidget(self.direction_edit, 0, 1)
        elif editing_type == "add_watermark":
            self.watermark_text_label = QLabel("Watermark Text:")
            self.watermark_text_edit = QLineEdit()
            self.position_label = QLabel("Position (x,y):")
            self.position_edit = QLineEdit()
            self.font_size_label = QLabel("Font Size:")
            self.font_size_edit = QLineEdit()
            self.font_path_label = QLabel("Font Path (Optional):")
            self.font_path_edit = QLineEdit()
            self.font_path_button = QPushButton("Browse")
            self.font_path_button.clicked.connect(self.browse_font_path)
            self.options_layout.addWidget(self.watermark_text_label, 0, 0)
            self.options_layout.addWidget(self.watermark_text_edit, 0, 1)
            self.options_layout.addWidget(self.position_label, 1, 0)
            self.options_layout.addWidget(self.position_edit, 1, 1)
            self.options_layout.addWidget(self.font_size_label, 2, 0)
            self.options_layout.addWidget(self.font_size_edit, 2, 1)
            self.options_layout.addWidget(self.font_path_label, 3, 0)
            self.options_layout.addWidget(self.font_path_edit, 3, 1)
            self.options_layout.addWidget(self.font_path_button, 3, 2)

    def browse_audio_path(self):
        audio_path, _ = QFileDialog.getOpenFileName(self, "Select Audio File")
        self.audio_path_edit.setText(audio_path)

    def browse_srt_path(self):
        srt_path, _ = QFileDialog.getOpenFileName(self, "Select SRT File")
        self.srt_path_edit.setText(srt_path)

    def browse_font_path(self):
        font_path, _ = QFileDialog.getOpenFileName(self, "Select Font File")
        self.font_path_edit.setText(font_path)

    def browse_input(self):
        if self.batch_checkbox.isChecked():
            dir_ = QFileDialog.getExistingDirectory(self, "Select Input Directory")
            self.input_edit.setText(dir_)
        else:
            file_filter = "All Files (*)"
            file, _ = QFileDialog.getOpenFileName(self, "Select Input File", "", file_filter)
            self.input_edit.setText(file)

    def browse_output(self):
        if self.conversion_combo.currentText() == 'images_to_pdf':
            file, _ = QFileDialog.getSaveFileName(self, "Select Output File", "", "PDF Files (*.pdf)")
            self.output_edit.setText(file)
        else:
            dir_ = QFileDialog.getExistingDirectory(self, "Select Output Directory")
            self.output_edit.setText(dir_)

    def browse_editor_input(self):
        editing_type = self.editing_combo.currentText()
        if editing_type == "merge_videos" or editing_type == "merge_audio_files":
            files, _ = QFileDialog.getOpenFileNames(self, "Select Input Files")
            self.editor_input_edit.setText(";".join(files))
        else:
            file_filter = "All Files (*)"
            file, _ = QFileDialog.getOpenFileName(self, "Select Input File", "", file_filter)
            self.editor_input_edit.setText(file)

    def browse_editor_output(self):
        dir_ = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        self.editor_output_edit.setText(dir_)

    def authenticate_gdrive(self):
        self.gdrive = GoogleDriveIntegration()
        self.gdrive.authenticate()
        QMessageBox.information(self, "Authentication", "Google Drive authenticated successfully!")

    def get_editing_options(self):
        editing_type = self.editing_combo.currentText()
        options = {}

        if editing_type == "trim_video" or editing_type == "trim_audio":
            options['start_time'] = float(self.start_time_edit.text())
            options['end_time'] = float(self.end_time_edit.text())
        elif editing_type == "add_audio":
            options['audio_path'] = self.audio_path_edit.text()
        elif editing_type == "change_resolution":
            options['new_resolution'] = tuple(map(int, self.resolution_edit.text().split('x')))
        elif editing_type == "add_subtitles":
            options['srt_path'] = self.srt_path_edit.text()
        elif editing_type == "extract_frames":
            if self.frame_times_edit.text():
                options['frame_times'] = [float(t) for t in self.frame_times_edit.text().split(',')]
            elif self.fps_edit.text():
                options['fps'] = float(self.fps_edit.text())
        elif editing_type == "remove_noise":
            options['noise_reduction_amount'] = int(self.noise_reduction_edit.text())
        elif editing_type == "change_speed":
            options['speed_factor'] = float(self.speed_factor_edit.text())
        elif editing_type == "resize_image":
            options['size'] = tuple(map(int, self.size_edit.text().split('x')))
        elif editing_type == "compress_image":
            options['quality'] = int(self.quality_edit.text())
        elif editing_type == "rotate_image":
            options['degrees'] = float(self.degrees_edit.text())
        elif editing_type == "flip_image":
            options['direction'] = self.direction_edit.text()
        elif editing_type == "add_watermark":
            options['watermark_text'] = self.watermark_text_edit.text()
            options['position'] = tuple(map(int, self.position_edit.text().split(',')))
            options['font_size'] = int(self.font_size_edit.text())
            options['font_path'] = self.font_path_edit.text() if self.font_path_edit.text() else None

        return options

    def edit_media(self):
        input_path = self.editor_input_edit.text()
        output_path = self.editor_output_edit.text()
        editing_type = self.editing_combo.currentText()
        options = self.get_editing_options()

        if not input_path or not output_path:
            QMessageBox.warning(self, "Error", "Please select input and output files.")
            return

        self.conversion_thread = ConversionThread(None, input_path, output_path, editing_type, options)
        self.conversion_thread.progress.connect(self.editor_progress_bar.setValue)
        self.conversion_thread.finished.connect(self.handle_edit_result)
        self.conversion_thread.start()

    def handle_edit_result(self, message):
        QMessageBox.information(self, "Editing Result", message)

    def convert_file(self):
        input_path = self.input_edit.text()
        output_path = self.output_edit.text()
        conversion_type = self.conversion_combo.currentText()

        # Check if input and output paths are selected
        if not input_path or not output_path:
            QMessageBox.warning(self, "Error", "Please select input and output files/directories.")
            return

        # Use Google Drive if enabled
        if self.cloud_checkbox.isChecked() and hasattr(self, 'gdrive'):
            if self.batch_checkbox.isChecked():
                # Batch processing with Google Drive
                folder_id = input_path  # Assuming input_path is a folder ID in this case
                files = self.gdrive.list_files_in_folder(folder_id)

                for file in files:
                    file_id = file['id']
                    file_name = file['name']
                    temp_file = os.path.join(os.path.expanduser("~"), file_name)  # Download to user's home dir

                    # Download file from Google Drive
                    self.gdrive.download_file(file_id, temp_file)

                    # Construct output file path in the specified Google Drive folder
                    output_file = os.path.join(output_path, os.path.splitext(file_name)[
                        0] + '_converted' + FileHandler.get_file_extension(file_name))

                    # Create and start conversion thread
                    self.conversion_thread = ConversionThread(None, temp_file, output_file, conversion_type)
                    self.conversion_thread.progress.connect(self.progress_bar.setValue)
                    self.conversion_thread.finished.connect(
                        lambda msg: self.handle_conversion_result(msg, temp_file, output_file))
                    self.conversion_thread.start()

            else:
                # Single file processing with Google Drive
                file_id = input_path  # Assuming input_path is a file ID
                file_name = self.gdrive.get_file_name(file_id)
                temp_file = os.path.join(os.path.expanduser("~"), file_name)  # Download to user's home dir

                # Download file from Google Drive
                self.gdrive.download_file(file_id, temp_file)

                # Construct output file path (you might need to adjust this based on your needs)
                output_file = os.path.join(output_path, os.path.splitext(file_name)[
                    0] + '_converted' + FileHandler.get_file_extension(file_name))

                # Create and start conversion thread
                self.conversion_thread = ConversionThread(None, temp_file, output_file, conversion_type)
                self.conversion_thread.progress.connect(self.progress_bar.setValue)
                self.conversion_thread.finished.connect(
                    lambda msg: self.handle_conversion_result(msg, temp_file, output_file))
                self.conversion_thread.start()

        else:
            # Local file processing
            if self.batch_checkbox.isChecked():
                # Batch processing
                files = FileHandler.list_files_in_directory(input_path)
                for file in files:
                    output_file = os.path.join(output_path, os.path.splitext(os.path.basename(file))[
                        0] + '_converted' + FileHandler.get_file_extension(file))
                    self.conversion_thread = ConversionThread(None, file, output_file, conversion_type)
                    self.conversion_thread.progress.connect(self.progress_bar.setValue)
                    self.conversion_thread.finished.connect(
                        lambda msg: self.handle_conversion_result(msg, file, output_file))
                    self.conversion_thread.start()
            else:
                # Single file processing
                if conversion_type == 'images_to_pdf':
                    input_files = input_path.split(';')
                    output_file = output_path  # Output is already a full path for this case
                else:
                    output_file = os.path.join(output_path, os.path.splitext(os.path.basename(input_path))[
                        0] + '_converted' + FileHandler.get_file_extension(input_path))

                self.conversion_thread = ConversionThread(None, input_path, output_file, conversion_type)
                self.conversion_thread.progress.connect(self.progress_bar.setValue)
                self.conversion_thread.finished.connect(
                    lambda msg: self.handle_conversion_result(msg, input_path, output_file))
                self.conversion_thread.start()

    def handle_conversion_result(self, message, input_file, output_file):
        self.log_text.append(message)

        # Clean up temporary file if using Google Drive
        if self.cloud_checkbox.isChecked() and hasattr(self, 'gdrive'):
            try:
                os.remove(input_file)  # Delete the temporary downloaded file
            except Exception as e:
                self.log_text.append(f"Error deleting temporary file: {e}")

        # Upload to Google Drive if conversion was successful and option is enabled
        if self.cloud_checkbox.isChecked() and hasattr(self, 'gdrive') and message == "Conversion successful!":
            try:
                # Upload the converted file to Google Drive
                self.gdrive.upload_file(output_file,
                                        self.output_edit.text())  # output_edit.text() should be the folder ID
                QMessageBox.information(self, "Conversion Result",
                                        "Conversion successful and uploaded to Google Drive!")
            except Exception as e:
                QMessageBox.warning(self, "Upload Error", f"Error uploading to Google Drive: {e}")
                self.log_text.append(f"Upload error: {e}")
        else:
            QMessageBox.information(self, "Conversion Result", message)
