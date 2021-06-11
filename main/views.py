from django.shortcuts import render
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime

# Webhook URL
# https://discord.com/api/webhooks/811043364748394596/SC9v_sVe-f5Jm8l0-oYrVqQR5Za-CpNb3L358VE28UOze3sUHeq4-ViMLtXPEwMD_n5-

_FORM_ARGUMENTS = ["fname", "lname", "email", "subject", "message"]

class Contact():
    def __init__(self, data):
        self.data = [point if point != '' else None for point in data]

    def check(self):
        error = False
        if '' in self.data: error = True
        return error

    def send(self):
        check = self.check()
        if not check:

            date = datetime.today().strftime('%Y-%m-%d')

            title = f"{self.data[0]} {self.data[1]} {date}"
            description = f"email: {self.data[2]}\nsubject: {self.data[3]}\nmessage: {self.data[4]}"

            webhook = DiscordWebhook(url="https://discord.com/api/webhooks/811043364748394596/SC9v_sVe-f5Jm8l0-oYrVqQR5Za-CpNb3L358VE28UOze3sUHeq4-ViMLtXPEwMD_n5-")
            embed = DiscordEmbed(title=title,
                                 description=description,
                                 color="242424")

            webhook.add_embed(embed)
            webhook.execute()
            return check
        else:
            return check

def execute_email(req):
    error = False

    try:
        form_data = dict(req.POST.lists())
        cleaned_form_data = [form_data[name][0] for name in _FORM_ARGUMENTS]
        form = Contact(cleaned_form_data)
        error = form.send()
    except KeyError:
        pass

    return error


def return_view(request):
    currentPath = request.path

    if currentPath == "/":
        error = execute_email(request)
        return render(request, 'main/index.html', context={"error": error})

    elif currentPath == "/summer-session-2020":
        return render(request, 'main/sessions/summer2020.html')

    elif currentPath == "/winter-session-2021":
        return render(request, 'main/sessions/winter2021.html')

    elif currentPath == "/spring-session-2021":
        return render(request, 'main/sessions/spring2021.html')

    elif currentPath == "/summer-session-2021":
        return render(request, 'main/sessions/summer2021.html')

