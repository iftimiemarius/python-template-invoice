"""

    This application takes the template.docx file and replaces
    the tags with the data within the .json configuration files

"""

from docxtpl import DocxTemplate

import utils

COMPANY_DETAILS_PATH = 'company_details.json'
INVOICE_DETAILS_PATH = 'invoice_details.json'


def main():
    """

        Read the config files, compute additional fields and save the file

    """

    context = utils.read_details_json(COMPANY_DETAILS_PATH, INVOICE_DETAILS_PATH)

    total_amount = 0
    for index, service in enumerate(context['services']):
        service['index'] = index + 1
        service['amount'] = service['quantity'] * service['unit_price']
        total_amount += service['amount']

    context['total'] = total_amount

    template = DocxTemplate('template.docx')
    template.render(context)

    filename = context['invoice_number']
    template.save(f'{filename}.docx')


if __name__ == '__main__':
    main()
