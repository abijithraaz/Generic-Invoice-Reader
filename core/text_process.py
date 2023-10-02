import re


def address_process(detect_text):
    '''
    Function for preprocessing the address in the invoice.
    '''
    res = re.sub("\n\n|\n\n\n|\n", ' ', detect_text)

    # Removal of unnecessary special characters
    res = re.sub("♀|$|#|%|,|'|", '', res)

    if (res != None):
        filt_address = str(res)
    else:
        filt_address = str(detect_text)
        
    print("Address", filt_address)
    return filt_address

def date_process(detect_text):
    # print("date", detect_text)
    
    return detect_text

def amound_process(detect_text):
    '''
    Function for preprocessing the price in the invoice.
    '''
    # Removal of unnecessary characters and lines
    res = re.sub("/s|,|'|_|-|\n|[a-zA-Z]|\n\n|~|\n\n\n|♀", '', detect_text)
    if res:
        filt_price = res
    else:
        filt_price = str(detect_text)

    print("filt_price:",filt_price)
    return filt_price

def company_name_process(detect_text):
    '''
    Function for preprocessing the company name in the invoice.
    '''
    # Removal of unnecessary new lines
    res = re.sub("\n|\n\n|\n\n\n|}", '', detect_text)

    # Removal of unnecessary special characters
    res = re.sub("♀|$|%|#|'|-", '', res)

    if (res != None):
        filt_name = str(res)
    else:
        filt_name = str(detect_text)

    print("filt_name:",filt_name)
    return filt_name

def invoice_no_process(detect_text):
    '''
    Function for preprocessing the invoice number in the invoice.
    '''
    # Removal of unnecessary characters and lines
    invoice_exp = "(\d+.\d+)"
    res = re.sub(" |,|\n|\n\n", '', detect_text)
    inv_no = re.search(invoice_exp, res)
    if (inv_no != None):
        filt_invoice = str(inv_no[0])
    else:
        filt_invoice = str(detect_text)
    print("filt_invoice:",filt_invoice)
    return filt_invoice