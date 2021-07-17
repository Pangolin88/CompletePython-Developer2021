import sys
from pathlib import Path
from PIL import Image

src_dir = sys.argv[1]
dst_dir = sys.argv[2]

src_path = Path(src_dir)
dst_path = Path(dst_dir)

if not dst_path.exists():
    dst_path.mkdir(parents=True)

for img_file in list(src_path.glob('*.jpg')):
    img = Image.open(f'{src_dir}/{img_file.name}')
    new_name = img_file.name.replace('jpg', 'png')
    img.save((f'{dst_dir}/{new_name}'), 'png')
