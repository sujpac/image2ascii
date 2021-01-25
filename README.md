# :pencil: Image2Ascii

Image2Ascii is a Python script that converts your favorite image into corresponding ASCII art.

## Installation
### macOS
```bash
git clone https://github.com/sujpac/image2ascii.git
cd image2ascii
sudo python3 -m pip install Pillow
python3 main.py -i <image.jpg>
```

## Command-Line Usage
```bash
Usage: python3 main.py [-f] -i <image_file>

Options:
  -f        Fit ASCII output to terminal window (default True)
  -c        Colorful ASCII output (default False)
  -i string
            Filename of image to be converted into ASCII art (default 'docs/images/plane.jpg')
```

## License
This project is under the MIT License. See the [LICENSE](https://github.com/sujpac/image2ascii/blob/main/LICENSE) file for the full license text.
