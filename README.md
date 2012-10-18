Content Inventory
=================

The script is used to recursively list all files in a starting directory
and export them to an XLS file.  If the file is HTML, it will record
the value in the &lt;title&gt; element.

Usage:

`python get_dir_listing.py -p /path/to/starting/point/to/crawl -x nameofspreadsheet.xls`

Hat tip to the following projects for their inspiration:

* https://github.com/terryjbates/content-audit
* https://github.com/quakerpunk/content-audit