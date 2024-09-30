import os
import urllib.request

from separate import (
    SeparateMDX, verify_audio
)


class ModelData:

    def __init__(self, model_name: str, download_url: str = "https://github.com/facefusion/facefusion-assets/releases/download/models-3.0.0/kim_vocal_2.onnx"):
        self.model_name = model_name
        self.model_path = self.get_model_path()
        self.model_basename = os.path.splitext(
            os.path.basename(self.model_path))[0]

        # Settings specific to Kim_Vocal_2.onnx model
        self.compensate = 1.009
        self.mdx_dim_f_set = 3072
        self.mdx_dim_t_set = 8
        self.mdx_n_fft_scale_set = 6144
        self.primary_stem = 'Vocals'

        self.mdx_segment_size = 256
        self.mdx_batch_size = 1

        # Download the model if it does not exist
        if not os.path.exists(self.model_path) and download_url:
            print(f"Model not found, downloading: {download_url}")
            self.download_model(download_url)

    def get_model_path(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        model_path = os.path.join(script_dir, 'models', self.model_name)
        return model_path

    def download_model(self, url: str):
        try:
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)  # Create models directory
            urllib.request.urlretrieve(url, self.model_path)
            print(f"Model downloaded successfully: {self.model_path}")
        except Exception as e:
            raise Exception(f"An error occurred while downloading the model: {e}")
        
class VocalAndSoundRemover:

    def __init__(self, input_file, output_folder, model_name='Kim_Vocal_2.onnx'):
        self.input_file = input_file
        self.output_folder = output_folder
        self.model_name = model_name

    def execute(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        try:
            model = ModelData(self.model_name)

            if not verify_audio(self.input_file):
                return print(
                    f'{os.path.basename(self.input_file)} is not a valid .wav file')

            audio_file_base = os.path.splitext(
                os.path.basename(self.input_file))[0]

            process_data = {
                'export_path': self.output_folder,
                'audio_file_base': audio_file_base,
                'audio_file': self.input_file,
            }

            separator = SeparateMDX(model, process_data)
            separator.separate()

        except Exception as e:
            return print(f'An error occurred during vocal removal: {e}')

        return self.output_folder
