import os
import sys
import argparse
import torch
from vocal_and_sound_remover import VocalAndSoundRemover

def display_welcome_message():
    author = r"""

        ██████╗ ███████╗███████╗██████╗                           
        ██╔══██╗██╔════╝██╔════╝██╔══██╗                          
        ██║  ██║█████╗  █████╗  ██████╔╝                          
        ██║  ██║██╔══╝  ██╔══╝  ██╔═══╝                           
        ██████╔╝███████╗███████╗██║                               
        ╚═════╝ ╚══════╝╚══════╝╚═╝                               
                                                                
        ███████╗██╗  ██╗████████╗██████╗  █████╗  ██████╗████████╗
        ██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
        █████╗   ╚███╔╝    ██║   ██████╔╝███████║██║        ██║   
        ██╔══╝   ██╔██╗    ██║   ██╔══██╗██╔══██║██║        ██║   
        ███████╗██╔╝ ██╗   ██║   ██║  ██║██║  ██║╚██████╗   ██║   
        ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝         

                        D E E P E X T R A C T
                    Developed by Abdullah Ozmantar
    """
    
    colored_description = f"""
        \033[34mWelcome to DeepExtract!\033[0m
            
        \033[37mThis tool helps you separate vocals and sounds from audio files quickly and efficiently.
        You can easily input audio files and specify an output directory for the results.\033[0m
            
        \033[33mUsage examples:\033[0m

        \033[90m1. CLI - Separate vocals from an audio file:\033[0m
        \033[32m   python main.py --input test/test_sound.wav --output outputs/\033[0m  
        
        \033[90m2. Python - Separate vocals from an audio file:\033[0m
        \033[32m   from vocal_and_sound_remover import VocalAndSoundRemover
        \n           vocal_remover = VocalAndSoundRemover('test/test_sound.wav', 'outputs/')
        \n           result_folder = vocal_remover.execute()\033[0m  
    """
    
    colored_author = f"\033[36m{author}\033[0m"
    
    print(colored_author)
    print(colored_description)

def main():

    display_welcome_message()

    parser = argparse.ArgumentParser(description='Welcome to the DeepExtract Vocal and Sound Separator')
    parser.add_argument('input_file', type=str, nargs='?', help='Input audio file path (WAV format)')
    parser.add_argument('output_folder', type=str, nargs='?', help='Output folder to save separated audio files')

    args = parser.parse_args()

    if args.input_file and args.output_folder:
        input_file = args.input_file
        output_folder = args.output_folder
        print(f"Input file: {input_file}")
        print(f"Output folder: {output_folder}")
    else:
        input_file = input("Enter the path of the input audio file (e.g., test/test_sound.wav): ")
        output_folder = input("Enter the path of the output folder (e.g., outputs/): ")

    vocal_remover = VocalAndSoundRemover(input_file, output_folder)

    result_folder = vocal_remover.execute()

    if result_folder:
        print(f'Output files have been saved to {result_folder}.')

if __name__ == "__main__":
    main()
