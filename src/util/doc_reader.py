import PyPDF2
import pdfplumber


class PDFDocument:

    def __init__(self, filepath):
        self.filepath = filepath
        self.pdf = pdfplumber.open(filepath)
        self.page_count = len(self.pdf.pages)

    def meta_data(self):
        print(f'Number of pages: {len(self.pdf.pages)}')
        print(f'Pages: {self.pdf.pages}')
        print()
        print('Document Information')
        print(self.pdf.metadata)
        print()
        print(f'Author: {self.pdf.metadata["Author"]}')

    def extract_first(self):
        page = self.pdf.pages[0]
        text = page.extract_text()
        print(text)
        return text

    def extract_whole(self):
        final = ''
        for page in range(self.page_count):
            data = self.pdf.pages[page].extract_text()
            final = final + "\n" + data
        print(final)
        return final

    def rotation_check(self):
        rot = int(self.pdf.pages[0].rotation)
        print(rot)
        if rot:
            return rot
        return None

    def rotate_back(self):
        pass

    def merger(self):
        pass

    def splitter(self):
        pass
