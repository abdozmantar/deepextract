# DeepExtract 🎤

## Overview

**DeepExtract** is a powerful and efficient tool designed to separate vocals and sounds from audio files, providing an enhanced experience for musicians, producers, and audio engineers. With DeepExtract, you can quickly and effectively isolate vocals or instruments from mixed audio tracks, facilitating tasks like remixing, karaoke preparation, or audio analysis.

## Features

- **Easy to Use:** Simple command-line interface (CLI) for seamless operation.
- **High-Quality Audio Separation:** Utilizes advanced algorithms to ensure minimal loss of audio quality.
- **Versatile Input and Output Options:** Supports various audio formats with user-defined output directories.
- **Python Integration:** Easily incorporate DeepExtract into your Python projects with straightforward API access.

## Installation Guide 🛠️

Setting up **DeepExtract** is quick and straightforward! Simply follow the steps below to get started.

### Step 1: Clone the Repository

Clone the DeepExtract repository to your local machine:

```bash
git clone https://github.com/abdozmantar/deepextract.git
cd deepextract
```

### Step 2: Run the Setup Script

To install DeepExtract, simply run the setup script:

```bash
setup.bat
```

### OR

```bash
python setup.py
```

## Usage

### Command-Line Interface (CLI)

To separate vocals from an audio file using the CLI, use the following command:

```bash
python main.py --input path/to/input.wav --output path/to/output/
```

### Python Integration

You can also integrate DeepExtract into your Python projects as follows:

```python
from vocal_and_sound_remover import VocalAndSoundRemover

input_file = 'path/to/input.wav'
output_folder = 'path/to/output/'

vocal_remover = VocalAndSoundRemover(input_file, output_folder)
result_folder = vocal_remover.execute()
```

## Examples

- **CLI Example:**

```bash
python main.py --input test/test_sound.wav --output outputs/
```

- **Python Example:**

```python
from vocal_and_sound_remover import VocalAndSoundRemover

vocal_remover = VocalAndSoundRemover('test/test_sound.wav', 'outputs/')
result_folder = vocal_remover.execute()
```

## Contributing

We welcome contributions from the community! If you'd like to enhance DeepExtract, please fork the repository and submit a pull request.

### Guidelines

1. Fork the project.
2. Create a feature branch.
3. Commit your changes.
4. Push to the branch.
5. Submit a pull request.

### Author

👤 **Abdullah Ozmantar**  
[GitHub Profile](https://github.com/abdozmantar)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/abdozmantar/deepextract/blob/main/LICENSE) file for details.
