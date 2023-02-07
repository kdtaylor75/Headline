from mailmerge import MailMerge
from datetime import date
import os

from applicant_info import general_info, professional_experience

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'doc_templates')
FILE_OUTPUT_DIR = os.getcwd()

default_template_filepath = os.path.join(TEMPLATE_DIR, 'resume_template_2.docx')


def create_resume_from_template(output_filename='resume.docx', template=default_template_filepath):
    # Set output filepath
    output_filepath = os.path.join(FILE_OUTPUT_DIR, output_filename)

    # Load resume template file
    template = MailMerge(template)

    template.merge(**general_info)
    template.merge_rows('company_name', professional_experience)

    template.write(output_filepath)

create_resume_from_template()