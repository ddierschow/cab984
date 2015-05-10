bamca
=====

Bay Area Matchbox Collectors Association

This repository contains much of the source code that runs "bamca.org".
There is still much missing but this is a start.  This repository
does not, and will not, contain the pictures from the site.
Absent that, the goal is to have enough recorded here that the
site could be recreated.

Please note that this was written by one person, and was never
intended to be shared or passed on, so the documentation is rare
to nonexistant.  I will be fixing that as I can.

Milestones:

1996 - V1 - This project was started as a page of links to sites
that would be of interest to Matchbox collectors.

1998 - V2 - We bought the domain name, and I started working on the
lineup pages, writing the scripts in PERL.

2000 - V3 - I converted the entire site to Python.

2004ish - V4 - I substantially rewrote the site to use a web framework
and a more cohesive design.

2010 - V5 - The site was rewritten to run off of a MySql database.
There are still some old pages that run off of text files, but
almost everything that has to do with 3-inch models is in the DB.

    5.0 published Sunday, 11 July 2010 at 12:01 AM PDT
    5.1 published Monday, 12 April 2011 at 12:01 AM PDT
    5.2 published Monday, 16 May 2011 at 12:01 AM PDT
    5.3 published Monday, 01 August 2011 at 12:01 AM PDT
    5.4 published Monday, 07 September 2011 at 12:01 AM PDT
    5.5 published -- date not recorded
    5.6 published Sunday, 22 June 2014 at 12:01 AM PDT

There are many plans for things to add, but they require time, which
is in short supply.  I'll do them when I can.  The most pressing
projects are to fill in more variation and product pictures, and
to add more models and products to the database.

PEP8:

Most of the stylistic elements were set long before I ever heard
of PEP8, and I am only now updating the codebase.  Since there are
some things I'm not in agreement with for my own programming, you'll
find that there are lines up to 132 characters long, and I do
multiple imports of system libraries on one line.  I've made two
passes so far converting this codebase to PEP8 compliance, but I
still have quite a ways to go, and there are several stylistic
standards that I don't like so it will never get all the way there.

Current and planned projects:

   * Add more entries to the annual lineup pages
   * Allow multiple pictures per variation
   * Link related variations
   * Rearrange MAN pictures into directories for vehicle type
   * Add support for publications, playsets, etc.
   * Comparisons are a pain to work with and need fixing
   * Tables casting_compare and casting_related are too similar
   * Need to add support for packs limited to region

...BIG things:

   * Convert rendering code to Jinja2
   * Add an API
   * Create a mobile-frendly site
   * Redesign the database schema

Projects independent of software version:

   * Incorporate the missing variations from Charlie
   * Build out data for related castings
   * Add larger-scale castings
   * Document the BAMCA library
   * Add more pictures!


Dean Dierschow
BAMCA Webmaster
