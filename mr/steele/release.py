import os
import system
import re

def releaseTasks(data):
    
    packageName = data['name']
    newVersion = data['version']

    # Check out the core development build
    tagdir = "corebuild"
    print system("svn co https://svn.plone.org/svn/plone/buildouts/plone-coredev/branches/4.2/ %s" % tagdir)
    os.chdir(os.path.join(os.getcwd(), tagdir))

    # Update version
    versionsfile = os.path.join(os.getcwd(),'versions.cfg')
    f = open(versionsfile, 'r')
    versionstxt = f.read()
    f.close()

    reg = re.compile("(^%s[\s\=]*)[0-9\.abrc]*" % packageName, re.MULTILINE)
    newVersionsTxt = reg.sub(r"\g<1>%s" % newVersion, versionstxt)

    f = open(versionsfile, 'w')
    f.write(newVersionsTxt)
    f.close()

    # Remove from checkouts.cfg
    checkoutsfile = os.path.join(os.getcwd(),'checkouts.cfg')
    f = open(checkoutsfile, 'r')
    checkoutstxt = f.read()
    f.close()

    reg = re.compile("^[\s]*%s\n" % packageName, re.MULTILINE)
    newCheckoutsTxt = reg.sub('',checkoutstxt)

    f = open(checkoutsfile, 'w')
    f.write(newCheckoutsTxt)
    f.close()