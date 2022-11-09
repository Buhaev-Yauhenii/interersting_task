from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from user.models import User
from history.models import TransactionsHistory
import numpy as np
import os


def preset_email():
    user_data = User.objects.values('email', 'balance')
    try:

        for data in user_data:
            data_for_html = {'email': data['email'], 'balance': data['balance'], 'categories': []}
            if TransactionsHistory.objects.filter(email=User.objects.get(email=data['email'])).exists():
                data = TransactionsHistory.objects.filter(email=User.objects.get(email=data['email'])).select_related(
                    'email').values()
                all_categories = set(data.values_list('category'))
                for index, cat in enumerate(all_categories):
                    values_of_cat = np.array(data.filter(category=cat[0]).values_list('sum', flat=True))
                    data_for_html['categories'].append({f'cat': cat[0]})
                    data_for_html['categories'][index][f'{cat[0]}_mean'] = values_of_cat.mean()
                    data_for_html['categories'][index][f'{cat[0]}_sum'] = values_of_cat.sum()
                    data_for_html['categories'][index][f'{cat[0]}_max'] = values_of_cat.max()
                    data_for_html['categories'][index][f'{cat[0]}_min'] = values_of_cat.min()
            message = get_template("template/email_template.html").render(Context({
                'data_for_html': data_for_html
            }))
        mail = EmailMessage(
            subject="Order confirmation",
            body=message,
            from_email=os.environ.get('EMAIL_ADMIN'),
            to=[data_for_html.email],
            reply_to=[user_data['email']],
        )
        mail.content_subtype = "html"
        mail.send()
        print(data_for_html)
    except Exception as e:
        print(e)
        print("does not have any data")
