from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna", "os", "PIL", "datetime", "csv", "PySimpleGUI", "pandas", "matplotlib.pyplot", "matplotlib.dates", "scipy.signal"]
options = {
    'build_exe': {    
        'packages':packages,
    }    
}

setup(
    name = "Boletim Diario",
    options = options,
    version = "0.1",
    description = 'Gerador de boletim diario',
    executables = executables
)