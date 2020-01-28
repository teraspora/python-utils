import os
import fnmatch

def get_files(pattern, basedir):
    for path, dirs, files in os.walk(basedir):
        for fname in fnmatch.filter(files, pattern):
            yield os.path.join(path, fname)


def choose_files(path, number):
    import os, random
    files = os.listdir(path)
    chosenfiles = random.choices(files, k = number)
    return chosenfiles   

# Notes:

    imgs = fu.get_files('*.png', '/media/john/sys2/web18/playground/visuals/imgs')

    with open('A0_images.txt', 'w') as f:
        for img in imgs:
            f.write(f'{int(os.stat(img).st_size / 1e6)} MB - {img[32:]}\n')

    total_size_MB = int(sum([os.stat(img).st_size for img in imgs]) / 1e6)


    # Run glslViewer from Python:

    os.system(f'cd /media/john/sys2/web18/playground/visuals/imgs/ && '
              f'glslViewer ../frag/production/blobacity.frag '
              f'../text/dance1024FB.png img5202.png img6798.png img8153.png img10415.png img11167.png img5263.png img4886.png img10493.png')



    imgs = ' '.join(os.listdir('/media/john/sys2/web18/playground/visuals/imgs/'))
        print(file)

    os.system(f'cd /media/john/sys2/web18/playground/visuals/imgs/ && '
              f'glslViewer ../frag/production/blobacity.frag '
              f'')








