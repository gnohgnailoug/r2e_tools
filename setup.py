from setuptools import setup, find_packages

setup(
    name="r2e-tools",
    version="0.1.0",
    packages=["tools"],
    install_requires=[
        "chardet",  
    ],
    entry_points={
        'console_scripts': [
            'finish = tools.finish:main',
            'file_editor = tools.file_editor:main',
            'execute_bash = tools.execute_bash:main',
            'search = tools.search:main',
        ],
    },
)
