from django.http import Http404
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Post, Sponsor, Member, OutreachEvent, Document


def index(request):
    NUM_RECENT_POSTS = 3
    blog_posts = Post.objects.all().order_by('-pub_date')[:NUM_RECENT_POSTS]
    context = {'blog_posts': blog_posts}
    return render(request, 'pslt/index.html', context)


def sponsors(request):
    sponsors_list = Sponsor.objects.all()
    context = {'sponsors': sponsors_list}
    return render(request, 'pslt/sponsors.html', context)


def team(request):
    member_list = Member.objects.all().order_by('priority')
    context = {'members': member_list}
    return render(request, 'pslt/team.html', context)


def contact(request):
    return render(request, 'pslt/contact.html')


def donate(request):
    return render(request, 'pslt/donate.html')


def outreach(request):
    event_list = OutreachEvent.objects.all()
    context = {'events': event_list}
    return render(request, 'pslt/outreach.html', context)


def documents(request, year):
    documents_list = Document.objects.filter(year=year)
    if documents_list.count() == 0:
        if year >= timezone.now().year:
            # tried to access a future year with no documents
            return render(request, 'pslt/documents-empty.html', {'year': year})
        else:
            # tried to access a previous year with no documents
            raise Http404()

    proposal = documents_list.filter(type="Proposal").first()
    pdr = documents_list.filter(type="PDR")
    cdr = documents_list.filter(type="CDR")
    frr = documents_list.filter(type="FRR")
    plar = documents_list.filter(type="PLAR").first()
    newest = None
    newest_r = None
    newest_s = None
    newest_f = None
    if plar:
        newest = plar
    elif frr:
        newest = frr
        newest_r = newest.filter(subtype="Report").first()
        newest_s = newest.filter(subtype="Slides").first()
        newest_f = newest.filter(subtype="Flysheet").first()
    elif cdr:
        newest = cdr
        newest_r = newest.filter(subtype="Report").first()
        newest_s = newest.filter(subtype="Slides").first()
        newest_f = newest.filter(subtype="Flysheet").first()
    elif pdr:
        newest = pdr
        newest_r = newest.filter(subtype="Report").first()
        newest_s = newest.filter(subtype="Slides").first()
        newest_f = newest.filter(subtype="Flysheet").first()
    elif proposal:
        newest = proposal

    context = {
        "year": year,

        "proposal": proposal,

        "pdr_r": pdr.filter(subtype="Report").first(),
        "pdr_s": pdr.filter(subtype="Slides").first(),
        "pdr_f": pdr.filter(subtype="Flysheet").first(),

        "cdr_r": cdr.filter(subtype="Report").first(),
        "cdr_s": cdr.filter(subtype="Slides").first(),
        "cdr_f": cdr.filter(subtype="Flysheet").first(),

        "frr_r": frr.filter(subtype="Report").first(),
        "frr_s": frr.filter(subtype="Slides").first(),
        "frr_f": frr.filter(subtype="Flysheet").first(),

        "plar": plar,

        "other": documents_list.filter(type="Other"),

        "newest": newest,
        "newest_r": newest_r,
        "newest_s": newest_s,
        "newest_f": newest_f
    }
    return render(request, 'pslt/documents.html', context)


def current_documents(request):
    AUGUST = 8
    year = timezone.now().year
    if timezone.now().month >= AUGUST:
        documents_list = Document.objects.filter(year=year+1)
        if documents_list.count() > 0:
            # show next year's documents if it's August or later and any documents exist
            year += 1
    return redirect('documents', year=year)


def about(request):
    return render(request, 'pslt/about.html')
