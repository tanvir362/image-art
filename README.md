# image-art
image-art simulates image drawing, written in python. It uses OpenCV to precess images and simulates drawing using turtle module.

### Installation

1. Clone repo

    ```bash
    git clone https://github.com/tanvir362/image-art.git
    cd image-art
    ```

2. Create virtual enviroment and activate

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install dependent packages

    ```bash
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    ```

**Run**

```bash
python3 run.py path/to/image_file
```

The path to the image file can be both absolute and relative. You can also run ```python3 run.py``` which will draw default image