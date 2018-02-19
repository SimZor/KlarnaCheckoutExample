class TaxRate:
    name = None
    percentage = None

    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage


class Item:
    quantity = None
    reference = None
    name = None
    unit_price = None
    discount_rate = 0
    tax_rate = None

    def __init__(self, reference, name, unit_price, tax_rate: TaxRate, discount_rate=None, quantity=1):
        self.quantity = quantity
        self.reference = reference
        self.name = name
        self.unit_price = unit_price
        self.tax_rate = tax_rate.percentage

        if discount_rate is not None:
            self.discount_rate = discount_rate

    def __repr__(self):
        return '<Item: {0}>'.format(self.name)


class Merchant:
    def __init__(self, id, back_to_store_uri, terms_uri, checkout_uri, confirmation_uri, push_uri):
        self.id = id
        self.back_to_store_uri = back_to_store_uri
        self.terms_uri = terms_uri
        self.checkout_uri = checkout_uri
        self.confirmation_uri = confirmation_uri
        self.push_uri = push_uri

    @property
    def get_merchant_dict(self):
        return {'id': self.id,
                'back_to_store_uri': self.back_to_store_uri,
                'terms_uri': self.terms_uri,
                'checkout_uri': self.checkout_uri,
                'confirmation_uri': self.confirmation_uri,
                'push_uri': self.push_uri}


class KlarnaCheckout:
    def __init__(self, merchant: Merchant, purchase_country='SE', purchase_currency='SEK', locale='sv-se'):
        self.merchant = merchant
        self.locale = locale
        self.purchase_country = purchase_country
        self.purchase_currency = purchase_currency
