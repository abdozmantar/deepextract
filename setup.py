import warnings
import subprocess
import os
import sys
import urllib.request
from packaging import version as pv
from pathlib import Path
from tqdm import tqdm

warnings.filterwarnings("ignore", category=DeprecationWarning)

print(f"\n")
print(f"-----------------------------------------------------------------")
print(f"🌟 Welcome to the DeepExtract Vocal and Sound Separator Installer 🌟")
print(f"-----------------------------------------------------------------")
print(f"\n")

# Create a virtual environment
env_name = 'venv'
if not os.path.exists(env_name):
    print(f"🌱 Creating virtual environment '{env_name}'...")
    subprocess.run([sys.executable, '-m', 'venv', env_name])

models_dir = os.path.join(Path(__file__).resolve().parent, "models")

os.makedirs(models_dir, exist_ok=True)

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")
model_url = "https://github.com/facefusion/facefusion-assets/releases/download/models-3.0.0/kim_vocal_2.onnx"
model_name = os.path.basename(model_url)
model_path = os.path.join(models_dir, model_name) 

print(model_path)

def run_pip(*args):
    subprocess.run([os.path.join(env_name, 'Scripts', 'python.exe'), '-m', 'pip', 'install', '--no-warn-script-location', *args])

def is_installed(package: str, version: str = None, strict: bool = True):
    has_package = None
    try:
        from pkg_resources import get_distribution as distributions
        has_package = distributions(package)
        if has_package is not None:
            if version is not None:
                installed_version = has_package.version
                if (installed_version != version and strict) or (pv.parse(installed_version) < pv.parse(version) and not strict):
                    return False
                return True
            return True
        return False
    except Exception as e:
        print(f"Status: {e}")
        return False

if not is_installed("tqdm"):
    print("🔧 INSTALLING: tqdm...")
    run_pip("tqdm")

def download(url, path):
    request = urllib.request.urlopen(url)
    total = int(request.headers.get('Content-Length', 0))
    with tqdm(total=total, desc='Downloading', unit='B', unit_scale=True, unit_divisor=1024) as progress:
        urllib.request.urlretrieve(url, path, reporthook=lambda count, block_size, total_size: progress.update(block_size))

if not os.path.exists(model_path):
    print("📥 Downloading the model, please wait...")
    download(model_url, model_path)

with open(req_file) as file:
    try:
        print("🔧 INSTALLING: onnxruntime-gpu...")
        run_pip("onnxruntime-gpu", "--extra-index-url", "https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-cuda-11/pypi/simple/")
        
        print("🔧 INSTALLING: torch, torchvision, torchaudio...")
        run_pip("torch", "torchvision", "torchaudio", "--extra-index-url", "https://download.pytorch.org/whl/cu118")

    except Exception as e:
        print(f"❌------------------------!ERROR!--------------------------------------")
        print(f"MODULE: onnxruntime-gpu")
        print(f"DeepExtract may not work.")
        print(f"ERROR: ")
        print(e)
        print(f"---------------------------------------------------------------------")
        raise e
    
    strict = True
    for package in file:
        package_version = None
        try:
            print(f"🔧 INSTALLING PACKAGE: {package.strip()}")
            package = package.strip()
            if "==" in package:
                package_version = package.split('==')[1]
            elif ">=" in package:
                package_version = package.split('>=')[1]
                strict = False
            
            if not is_installed(package, package_version, strict):
                run_pip(package)
        except Exception as e:
            print(f"❌------------------------!ERROR!--------------------------------------")
            print(f"MODULE: {package.strip()}")
            print(f"DeepExtract may not work.")
            print(f"ERROR: ")
            print(e)
            print(f"---------------------------------------------------------------------")
            raise e

print("\n")
print(f"🎉-----------------------------------------------------------------")
print(f"🎉 DeepExtract Installation completed successfully! 🎉")
print(f"🔄 Please restart your application to access DeepExtract features. 🔄")

cli_script_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'main.py')
print(f"🚀 Starting the DeepExtract CLI...")
subprocess.run([os.path.join(env_name, 'Scripts', 'python.exe'), cli_script_path])
