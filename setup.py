from setuptools import setup
import setuptools, os

descr = 'Image process framework based on plugin like imagej, it is esay to glue with scipy.ndimage, scikit-image, opencv, simpleitk, mayavi...and any libraries based on numpy'

def get_data_files():
    dic = {}
    for root, dirs, files in os.walk('bareditor', True):
        root = root.replace('/', '.').replace('\\', '.')
        files = [i for i in files if not '.py' in i]
        if len(files)==0:continue
        dic[root] = files
    return dic

if __name__ == '__main__':
    setup(name='bareditor',
        version='0.17',
        url='https://github.com/434625142/bareditor',
        description='interactive python image-processing plugin framework',
        long_description=descr,
        author='yxdragon',
        author_email='yxdragon@imagepy.org',
        
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
        packages=setuptools.find_packages(),
        package_data=get_data_files(),
        install_requires=[
            'wxpython',
            'numba',
            'pillow'
        ],
    )
