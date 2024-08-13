## What this is:
Free, unencumbered NDA(s), employment agreement(s), and other legal contracts formatted with yaml-backed jinja2 templates. 

## Use at your own risk

`legal-docs-jinja` does not warrant that these are suitable for any purpose.
These do not replace an attorney. Any use of these contracts is at your
own risk and should be under the guidance of your own legal advisor.

## Use

Update `info.yml` inside a specific project and run `generate.py` for within the directory. 
Output artifacts will be created and added to `<project>/dist/output.html`. 
After generating, most browsers offer the ability to render the HTML and then print-to-pdf while 
adding custom margins if desired.