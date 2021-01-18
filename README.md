# :moon: Image2Ascii

Image2Ascii is a Python script that converts your favorite image into corresponding ASCII art.

## Installation
### macOS
```bash
git clone https://github.com/sujpac/image2ascii.git
cd image2ascii
sudo python3 -m install Pillow
python3 image2ascii.py -i <image.jpg>
```

## Command-Line Usage
```bash
Usage: image2ascii [-a] -i <img_filename>

Options:
  -a        Fit ascii output to terminal (default True)
  -c        Colored ascii output (default False)
  -i string
            Image file to be converted
```

## License
This project is under the MIT License. See the [LICENSE](https://github.com/sujpac/image2ascii/blob/main/LICENSE) file for the full license text.
