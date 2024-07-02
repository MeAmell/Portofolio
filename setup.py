from setuptools import setup, find_packages

setup(
    name='nama_proyek',
    version='1.0',
    packages=find_packages(),  # mencari semua paket di direktori proyek
    install_requires=[  # daftar dependencies yang dibutuhkan proyek
        'numpy>=1.22.0',
        'matplotlib>=3.5.1',
        'pandas>=1.3.5',
        'scikit-learn>=1.0.2',
        'scipy>=1.9.1',
        'seaborn>=0.11.2',
        'streamlit>=1.23.1',
        'joblib>=1.3.2',
        'plotly>=5.15.0',
    ],
    entry_points={  # entri titik untuk menjalankan skrip proyek
        'console_scripts': [
            'nama_skrip = nama_modul:main_function',
        ],
    },
    python_requires='>=3.10',  # versi Python minimal yang dibutuhkan
)
