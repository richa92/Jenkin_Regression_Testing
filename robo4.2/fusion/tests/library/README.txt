This folder contains code which will allow you to generate a test case file for all keywords in the library.
Use it from the root of the fusion folder like so:
>python tests/library/generate_tests.python

This will generate one enormous test suite file called "keyword_tests.robot".  It contains calls to all of the keywords in the library and Resources folder with fake parameters.  As a result, these are not proper tests for the keywords, rather they allow the testing of the ability of the keywords to accept the parameters that they claim.
It makes basic assumptions about parameters and tries to provide the correct dummy parameters.

Then, run the tests like so:
>pybot -A tests/library/args.txt

You'll get a standard robot output.xml, report.html, and log.html detailing the execution of all keywords with the --dryrun option enabled.
