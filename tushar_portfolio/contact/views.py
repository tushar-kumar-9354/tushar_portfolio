from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    success = False
    error = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                send_mail(
                    subject=f"Message from {form.cleaned_data['name']}",
                    message=form.cleaned_data['message'],
                    from_email=form.cleaned_data['email'],
                    recipient_list=['jangratushar348@example.com'],

                    fail_silently=False,
                )
                success = True
                form = ContactForm()  # Reset form after successful submit
            except BadHeaderError:
                error = "Invalid header found."
            except Exception as e:
                error = f"An error occurred: {e}"
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'success': success, 'error': error})
