from pathlib import Path
import pytest
from dataframe_image import convert


filenames = ['tests/notebooks/Short.ipynb',
             'tests/notebooks/Test 1.ipynb',
             'tests/notebooks/Test 1 EXECUTED.ipynb']
tos = ['pdf', 'md']
executes = [False, True]

@pytest.mark.parametrize('filename', filenames)
@pytest.mark.parametrize('to', tos)
@pytest.mark.parametrize('execute', executes)
class TestConvert:    

    def test_same_folder(self, filename, to, execute):
        ex = ' executed' if execute else ' not_executed'
        document_name = Path(filename).stem + ex + ' NEW NAME'
        convert(filename, to=to, execute=execute, document_name=document_name)

class TestConvertOther:    

    def test_save_notebook(self):
        filename = 'tests/notebooks/Short.ipynb'
        to = 'pdf'
        document_name = Path(filename).stem + ' saved NEW NAME'
        convert(filename, to=to, save_notebook=True, execute=True, document_name=document_name)

    def test_output_dir(self):
        filename = 'tests/notebooks/Short.ipynb'
        to = 'pdf'
        document_name = Path(filename).stem + ' output_dir NEW NAME'
        convert(filename, to=to, output_dir='tests/test_output', document_name=document_name)