import os
import re
import win32com.client
import docx


class File:
    def __init__(self, media, appdir, year, filename):  # при исп. MEDIA удалить media
        self.directory = os.path.join(media, appdir, year)
        self.file_path = os.path.join(media, appdir, year, filename)


class WebFile(File):
    def __init__(self, file_href, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_href = file_href

    def download_file(self):
        if not os.path.exists(self.file_path):
            try:
                os.makedirs(self.directory)
            except FileExistsError:
                print(f'Закачка пропущена, файл существует: \n{self.file_path}')
            with open(self.file_path, 'wb') as f:
                f.write(self.file_href.content)
        else:
            print(f'Закачка пропущена, файл существует: \n{self.file_path}')


class DocxFile(File):
    def doc2docx(self):
        word = win32com.client.Dispatch("Word.application")
        for dir_path, dirs, files in os.walk(self.directory):
            for file_name in files:
                file_path = os.path.join(dir_path, file_name)
                file_name, file_extension = os.path.splitext(file_path)
                if file_extension.lower() == '.doc':
                    docx_file = '{0}{1}'.format(file_path, 'x')
                    # Skip conversion where docx file already exists
                    if not os.path.isfile(docx_file):
                        print('Преобразование в docx\n{0}\n'.format(file_path))
                        try:
                            word_doc = word.Documents.Open(file_path, False, False, False)
                            # Замена слеша в пути с / на \\, т.к. doc.SaveAs не отрабатывает /
                            docxf = re.sub('/', '\\\\', docx_file)
                            word_doc.SaveAs2(docxf, FileFormat=16)
                            word_doc.Close()
                        except Exception:
                            print('Failed to Convert: {0}'.format(file_path))

    def get_docx(self):
        if self.file_path.lower()[-1] == 'x':
            return docx.Document(self.file_path)
        DocxFile.doc2docx(self)
        return docx.Document(self.file_path+'x')
