from docxtpl import DocxTemplate

import utils

COMPANY_DETAILS_PATH = 'company_details.json'
INVOICE_DETAILS_PATH = 'invoice_details.json'


if __name__ == '__main__':
    context = utils.read_details_json(COMPANY_DETAILS_PATH, INVOICE_DETAILS_PATH)

    total_amount = 0
    for index, service in enumerate(context['services']):
        service['index'] = index + 1
        service['amount'] = service['quantity'] * service['unit_price']
        total_amount += service['amount']

    context['total'] = total_amount

    template = DocxTemplate('template.docx')
    template.render(context)
    template.save('{}.docx'.format(context['invoice_number']))
